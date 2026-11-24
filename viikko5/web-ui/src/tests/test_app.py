import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from app import WarehouseStore, create_app


def client():
    app = create_app(WarehouseStore())
    app.config["TESTING"] = True
    return app.test_client()


def test_user_can_create_and_list_warehouse():
    test_client = client()
    test_client.post("/warehouses", data={"name": "Main warehouse", "capacity": "10"})
    response = test_client.post(
        "/warehouses",
        data={"name": "Cold storage", "capacity": "20"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Main warehouse" in response.data
    assert b"Cold storage" in response.data
    assert b"0/10" in response.data
    assert b"0/20" in response.data


def test_warehouse_names_are_escaped_in_html():
    response = client().post(
        "/warehouses",
        data={"name": "<script>alert('xss')</script>", "capacity": "10"},
        follow_redirects=True,
    )

    assert b"&lt;script&gt;" in response.data
    assert b"<script>" not in response.data


def test_user_can_add_and_remove_goods():
    test_client = client()
    test_client.post("/warehouses", data={"name": "Main", "capacity": "10"})

    test_client.post("/warehouses/1/add", data={"quantity": "4"})
    response = test_client.post(
        "/warehouses/1/remove",
        data={"quantity": "1"},
        follow_redirects=True,
    )

    assert b"3/10" in response.data


def test_removing_too_many_goods_keeps_balance_unchanged():
    test_client = client()
    test_client.post("/warehouses", data={"name": "Main", "capacity": "10"})
    response = test_client.post(
        "/warehouses/1/remove",
        data={"quantity": "1"},
        follow_redirects=True,
    )

    assert b"Cannot remove more goods" in response.data
    assert b"0/10" in response.data


def test_invalid_warehouse_data_is_rejected():
    response = client().post(
        "/warehouses",
        data={"name": "", "capacity": "0"},
        follow_redirects=True,
    )

    assert b"positive capacity" in response.data
    assert b"No warehouses yet." in response.data


def test_missing_warehouse_data_is_rejected():
    response = client().post("/warehouses", data={}, follow_redirects=True)

    assert b"positive capacity" in response.data
    assert b"No warehouses yet." in response.data


def test_invalid_quantities_are_rejected_without_changing_balance():
    test_client = client()
    test_client.post("/warehouses", data={"name": "Main", "capacity": "10"})
    test_client.post("/warehouses/1/add", data={"quantity": "3"})

    for path in ("/warehouses/1/add", "/warehouses/1/remove"):
        for data in ({}, {"quantity": "0"}, {"quantity": "-1"}, {"quantity": "invalid"}):
            response = test_client.post(path, data=data, follow_redirects=True)

            assert b"positive integer" in response.data
            assert b"3/10" in response.data


def test_unknown_warehouses_are_rejected():
    test_client = client()
    test_client.post("/warehouses", data={"name": "Main", "capacity": "10"})

    for path in ("/warehouses/999/add", "/warehouses/999/remove"):
        response = test_client.post(
            path,
            data={"quantity": "1"},
            follow_redirects=True,
        )

        assert b"Warehouse not found" in response.data
        assert b"0/10" in response.data

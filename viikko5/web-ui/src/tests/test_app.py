import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from app import WarehouseStore, create_app


def client():
    app = create_app(WarehouseStore())
    app.config["TESTING"] = True
    return app.test_client()


def test_user_can_create_and_list_warehouse():
    response = client().post(
        "/warehouses",
        data={"name": "Main warehouse", "capacity": "10"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Main warehouse" in response.data
    assert b"0/10" in response.data


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

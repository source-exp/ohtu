from dataclasses import dataclass

from flask import Flask, redirect, render_template_string, request, url_for


@dataclass
class Warehouse:
    name: str
    capacity: int
    balance: int = 0


class WarehouseStore:
    def __init__(self):
        self._warehouses = {}
        self._next_id = 1

    def create(self, name, capacity):
        warehouse_id = self._next_id
        self._next_id += 1
        self._warehouses[warehouse_id] = Warehouse(name, capacity)
        return warehouse_id

    def all(self):
        return self._warehouses.items()

    def get(self, warehouse_id):
        return self._warehouses.get(warehouse_id)

    def change_balance(self, warehouse_id, amount):
        warehouse = self.get(warehouse_id)
        if warehouse is None:
            raise ValueError("Warehouse not found")
        if warehouse.balance + amount < 0:
            raise ValueError("Cannot remove more goods than the current balance")
        if warehouse.balance + amount > warehouse.capacity:
            raise ValueError("Cannot exceed the warehouse capacity")
        warehouse.balance += amount


PAGE = """
<!doctype html>
<title>Warehouses</title>
<h1>Warehouses</h1>

{% if message %}<p role="status">{{ message }}</p>{% endif %}
{% if error %}<p role="alert">{{ error }}</p>{% endif %}

<h2>Create a warehouse</h2>
<form method="post" action="{{ url_for('create_warehouse') }}">
  <label>Name <input name="name" required></label>
  <label>Capacity <input name="capacity" type="number" min="1" required></label>
  <button type="submit">Create</button>
</form>

<h2>Current balances</h2>
{% if warehouses %}
<ul>
{% for warehouse_id, warehouse in warehouses %}
  <li>
    <strong>{{ warehouse.name }}</strong>:
    {{ warehouse.balance }}/{{ warehouse.capacity }}
    <form method="post" action="{{ url_for('add_goods', warehouse_id=warehouse_id) }}">
      <label>Quantity <input name="quantity" type="number" min="1" required></label>
      <button type="submit">Add</button>
    </form>
    <form method="post" action="{{ url_for('remove_goods', warehouse_id=warehouse_id) }}">
      <label>Quantity <input name="quantity" type="number" min="1" required></label>
      <button type="submit">Remove</button>
    </form>
  </li>
{% endfor %}
</ul>
{% else %}
<p>No warehouses yet.</p>
{% endif %}
"""


def create_app(store=None):
    app = Flask(__name__)
    app.config["STORE"] = store or WarehouseStore()

    @app.get("/")
    def index():
        return render_template_string(
            PAGE,
            warehouses=app.config["STORE"].all(),
            message=request.args.get("message"),
            error=request.args.get("error"),
        )

    @app.post("/warehouses")
    def create_warehouse():
        name = request.form.get("name", "").strip()
        capacity = _positive_integer(request.form.get("capacity"))
        if not name or capacity is None:
            return _redirect_with_error("Name and a positive capacity are required")
        app.config["STORE"].create(name, capacity)
        return _redirect_with_message("Warehouse created")

    @app.post("/warehouses/<int:warehouse_id>/add")
    def add_goods(warehouse_id):
        return _change_goods(warehouse_id, _positive_integer(request.form.get("quantity")))

    @app.post("/warehouses/<int:warehouse_id>/remove")
    def remove_goods(warehouse_id):
        quantity = _positive_integer(request.form.get("quantity"))
        return _change_goods(warehouse_id, -quantity if quantity is not None else None)

    def _change_goods(warehouse_id, amount):
        if amount is None:
            return _redirect_with_error("Quantity must be a positive integer")
        try:
            app.config["STORE"].change_balance(warehouse_id, amount)
        except ValueError as error:
            return _redirect_with_error(str(error))
        return _redirect_with_message("Balance updated")

    def _redirect_with_message(message):
        return redirect(url_for("index", message=message))

    def _redirect_with_error(error):
        return redirect(url_for("index", error=error))

    return app


def _positive_integer(value):
    try:
        number = int(value)
    except (TypeError, ValueError):
        return None
    return number if number > 0 else None


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

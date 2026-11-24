# Warehouse web UI

This is a small Flask web interface for creating warehouses and changing their
current balances. Data is kept in memory while the application is running.

## Run

From this directory, install the project and start Flask:

```bash
uv sync
uv run python src/app.py
```

Open <http://127.0.0.1:5000> in a browser.

## Tests

```bash
uv run pytest
```

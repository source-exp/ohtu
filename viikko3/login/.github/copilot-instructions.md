# Project instructions

- This is a `uv` project. Run project commands with `uv run ...`; install or
  synchronize dependencies with `uv sync`.
- Start the application with `uv run python3 src/index.py`. It listens on
  `http://localhost:5001`.
- Run the Robot Framework acceptance tests with `uv run robot src/tests`.
  The application must be running while the tests execute.
- User registration and credential validation are implemented in
  `src/services/user_service.py`, in `UserService.validate`.

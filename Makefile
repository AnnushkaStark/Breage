PYTHONPATH := $(shell pwd)/src
PYTHON := uv run



.PHONY: ruff tests up_home up_home_d down run_home venv

ruff:
	uv run ruff check src --config pyproject.toml --fix
	uv run ruff format src --config pyproject.toml

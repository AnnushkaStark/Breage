PYTHONPATH := $(shell pwd)/src
PYTHON := uv run



.PHONY: ruff tests up_home up_home_d down run_home venv

ruff:
	uv run ruff check src --config pyproject.toml --fix
	uv run ruff format src --config pyproject.toml



migration:
	PYTHONPATH=$(PYTHONPATH) uv run alembic revision --autogenerate

upgrade:
	PYTHONPATH=$(PYTHONPATH) uv run  alembic upgrade head


run_home:
	python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

up_home_d:
	docker compose up -d

up_home:
	docker compose up

down:
	docker-compose down -v

venv:
	uv python install 3.13
	uv sync --python 3.13
	@echo "✅ Environment is ready."


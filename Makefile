.PHONY: install setup start start-server migrate collectstatic lint test testcov check build render-start

install:
	uv sync

setup: install
	cp -n code-env .env || true
	uv run python manage.py migrate

PORT ?= 8000
start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

start-server:
	/project/.venv/bin/python manage.py runserver 0.0.0.0:3000

migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --no-input

lint:
	uv run ruff check task_manager

test:
	uv run pytest

testcov:
	uv run coverage run --source='.' manage.py test
	uv run coverage xml

check: lint test

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi:application
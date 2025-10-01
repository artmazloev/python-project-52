#!/usr/bin/env bash
set -o errexit

# Установка uv если еще не установлен
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.local/bin/env
fi

# Установка зависимостей и настройка
uv sync
uv run python manage.py collectstatic --no-input
uv run python manage.py migrate
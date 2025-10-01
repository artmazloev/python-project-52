# Менеджер задач (Task Manager)

## Статус проверок и качества кода:
[![Actions Status](https://github.com/artmazloev/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/artmazloev/python-project-52/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=artmazloev_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=artmazloev_python-project-52)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=artmazloev_python-project-52&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=artmazloev_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=artmazloev_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=artmazloev_python-project-52)

🔗 [Демо на Render](https://task-manager-art-mazloev.onrender.com/)

---

## 📌 О проекте

**Менеджер задач** — простое веб-приложение для управления задачами.

### Возможности:
- ✅ Регистрация и авторизация пользователей
- 📝 Создание, редактирование и удаление задач
- 📊 Настраиваемая система статусов
- 🏷️ Управление метками (категорирование задач)
- 🔍 Фильтры для поиска задач по параметрам
- 👤 Базовое управление профилем пользователя


---

## 🛠️ Технологии

- **Python 3.10+** — язык программирования
- **Django 5.1** — веб-фреймворк
- **PostgreSQL** — база данных
- **Bootstrap 5** — UI-фреймворк
- **Gunicorn** — WSGI сервер

---

## 📦 Установка и запуск

### Требования
- Python 3.10+
- uv

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/artmazloev/python-project-52.git
cd python-project-52
```
### 2. # Установка зависимостей и настройка
```bash
uv sync
uv run python manage.py collectstatic --no-input
uv run python manage.py migrate
```
### 3. # Создайте .env по образцу
```bash
SECRET_KEY=your_key
DEBUG=True
USE_SQLITE=True
DATABASE_URL=sqlite:///db.sqlite3
ROLLBAR_ACCESS_TOKEN=
```

### 4. # Запустите сервер
```bash
make setup
make start-server
```

## Разработчик:
В рамках учебного проекта лучшей школы программирования Hexlet
GitHub: [@artmazloev](https://github.com/artmazloev)

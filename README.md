# ReceptHub API (Учебный / pet-проект)

Кратко: REST API для управления рецептами (категории, ингредиенты, рецепты, пользователи) на базе **FastAPI** с асинхронным доступом к БД через **SQLAlchemy 2 (async)** и **asyncpg**. Проект содержит миграции (Alembic), тесты и Dockerfile.

## Стек
- Python 3.11+
- FastAPI (async)
- SQLAlchemy 2.0 (async)
- Pydantic (v2)
- Alembic (миграции)
- asyncpg (PostgreSQL driver)
- uvicorn
- Docker (опционально)
- pytest + httpx (тесты)

## Функционал
- CRUD для рецептов, категорий и ингредиентов
- Регистрация / логин пользователей (FastAPI Users)
- Ограничение доступа к созданию/редактированию через зависимости (Depends)
- Миграции базы через Alembic
- Dockerfile для контейнеризации

---

## Быстрый старт (локально)
> Предполагается, что у тебя установлен PostgreSQL и ты запускаешь команды из корня репозитория.

1. Клонируй/распакуй проект и перейди в корень:
```bash
cd /path/to/project
```

2. Устaнави зависимости
```bash
pip install -r requirements.txt
```
    - Опционально
        Создай виртуальное окружение и активируй ее
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Примени alembic миграции
    - Перейди в app
        ```bash
        cd app
        ```
    - Примени миграции
        ```bash
        alembic upgrade head
        ```
4. Отредактируй .env.template который лежит в корне проекта

5. Запусти
    - main.py
        ```bash
        python3 main.py
        ```
    - Dockerfile
        ```bash
        cd ..
        sudo docker build -t recipe_api_image .
        sudo docker run -d --name recipe_api_container -p 8000:8000 recipe_api_image
        ```

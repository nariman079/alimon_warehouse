FROM python:3.11.10

RUN pip  install poetry

WORKDIR /app/

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY ./src/ /app/src/
COPY ./tests/ /app/tests/
COPY ./migrations /app/migrations/
COPY ./alembic.ini /app/alembic.ini
COPY .env /app/
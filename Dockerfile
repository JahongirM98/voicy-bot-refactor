FROM python:3.12-slim

WORKDIR /app

# Устанавливаем uv — современный пакетный менеджер
RUN pip install --no-cache-dir uv

# Копируем только pyproject.toml для установки зависимостей
COPY pyproject.toml ./

# Устанавливаем зависимости через uv (в системный Python)
RUN uv pip install --system -r pyproject.toml

# Копируем всё приложение
COPY . .

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Запускаем Alembic миграцию и основной скрипт
CMD ["sh", "-c", "/wait-for-it.sh db:5432 -- alembic upgrade head && python main.py"]


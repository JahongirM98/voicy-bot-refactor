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

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]

COPY start_bot.sh /start_bot.sh
RUN chmod +x /start_bot.sh


# Запускаем Alembic миграцию и основнойl скрипт
CMD ["sh", "-c", "/entrypoint.sh && uvicorn interfaces.api.main:app --host 0.0.0.0 --port 8000"]


#!/bin/bash
/wait-for-it.sh db:5432 -t 60

# Попытки применить миграцию, если база ещё не готова
for i in {1..10}
do
  alembic upgrade head && break
  echo "Alembic failed, retrying in 5s..."
  sleep 5
done

exec uvicorn interfaces.api.main:app --host 0.0.0.0 --port 8000


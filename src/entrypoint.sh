#!/bin/sh
set -e

echo "Waiting connect to PostgreSQL..."

until pg_isready -h db -p 5432; do
  echo "Waiting access"
  sleep 1
done

echo "Database is available, run migrations"
alembic upgrade head

echo "Start uvicorn"
exec uvicorn src.main:app --host 0.0.0.0 --port 8919 --reload
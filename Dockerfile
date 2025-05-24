
# 1. Сборка фронта
FROM node:20 AS frontend-build

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build

# 2. Бэкенд + фронт + запуск
FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Копируем backend-код
COPY backend/ /app/backend/

# Копируем собранный фронт как статику
COPY --from=frontend-build /app/frontend/dist /app/frontend_dist

ENV PYTHONPATH="/app/backend:${PYTHONPATH}"

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

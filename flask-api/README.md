# Flask API

## Описание
REST API на Flask с PostgreSQL. Поддерживает отправку и получение результатов.

## Эндпоинты
- `POST /submit` — отправка JSON `{ "name": "Kirill", "score": 88 }`
- `GET /results` — список всех записей
- `GET /ping` — health-check

## Запуск
```bash
docker-compose up --build

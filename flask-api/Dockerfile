FROM python:3.10-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY . .

# Экспорт переменных окружения
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]

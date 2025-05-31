# Этап сборки
FROM golang:1.21 AS builder

WORKDIR /app

COPY main.go .

# Сборка бинарника в /bin/web
RUN go build -o /bin/web ./main.go

# Финальный минимальный образ
FROM alpine:latest

# Копируем собранный бинарник из стадии builder
COPY --from=builder /bin/web /bin/web

EXPOSE 8080

# Запуск бинарника
ENTRYPOINT ["/bin/web"]

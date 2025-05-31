FROM golang:1.21.5 as builder

WORKDIR /go-app

COPY go.mod go.sum ./
RUN go mod download

COPY cmd /go-app/cmd
COPY internal /go-app/internal
COPY docs /go-app/docs

RUN cd /go-app/cmd/demo/ && \
    CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /bin/go-app ./

# Минимальный образ
# Досуп в artifactory.lstprod.net не предоставили (воспользовался публичным образом)
# FROM artifactory.lstprod.net/midi_docker/golang:1.21.5-alpine3.19
FROM golang:1.21.5-alpine3.19

# Правильное объявление переменных окружения
ENV API_PORT="${API_PORT}" \
    DB_URL="${DB_URL}"

COPY --from=builder /bin/go-app /bin/go-app
RUN chmod +x /bin/go-app

CMD ["/bin/sh", "-c", "/bin/go-app"]

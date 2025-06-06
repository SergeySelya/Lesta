#!/bin/bash

TOKEN='7616687279:AAGpLoBW6Yx24FuVt0bDqi1-tcxS_o62tlE'
CHAT_ID='-4810009303'

TRIGGER_NAME="$1"
TRIGGER_STATUS="$2"
ITEM_NAME="$3"
ITEM_VALUE="$4"
EVENT_TIME="$5"

# Формируем сообщение
MESSAGE="👤 Author: Selivonchik S.%0A🚨 ${TRIGGER_NAME}: ${TRIGGER_STATUS}%0A📊 ${ITEM_NAME}: ${ITEM_VALUE}%0A🕒 Time: ${EVENT_TIME}"

# Отправляем сообщение
curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
     -d chat_id="$CHAT_ID" \
     -d text="$MESSAGE" \
     -d parse_mode="Markdown"

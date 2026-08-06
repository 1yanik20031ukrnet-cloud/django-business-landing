import logging
import os

import requests

logger = logging.getLogger(__name__)


def send_telegram_notification(lead):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        logger.warning(
            "Telegram notification skipped: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set"
        )
        return

    text = (
        f"Новая заявка: {lead.name}\n"
        f"Контакт: {lead.contact}\n"
        f"Услуга: {lead.get_service_display()}\n"
        f"Сообщение: {lead.message or '—'}"
    )

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        response = requests.post(url, data={"chat_id": chat_id, "text": text}, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        logger.exception("Failed to send Telegram notification")

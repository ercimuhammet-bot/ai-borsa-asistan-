import os
import urllib.request
import urllib.parse


def send_telegram_message(chat_id, message):
    """
    Telegram botuna mesaj gönderir.
    """

    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN bulunamadı."
        )

    url = (
        f"https://api.telegram.org/bot{token}/sendMessage"
    )

    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": message,
    }).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8")
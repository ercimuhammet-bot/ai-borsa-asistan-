from telegram import send_telegram_message


def send_signal_alert(results, chat_id):
    """
    Hisse tarama sonuçlarını Telegram'a gönderir.
    """

    lines = [
        "AI BORSA ASİSTANI",
        ""
    ]

    for result in results:
        lines.append(
            f"{result['symbol']} → "
            f"{result['display']}"
        )

    message = "\n".join(lines)

    return send_telegram_message(
        chat_id,
        message
    )

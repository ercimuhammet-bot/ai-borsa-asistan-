import pandas as pd


def calculate_support_resistance(df, window=20):
    """
    Son dönem fiyat hareketlerinden basit destek
    ve direnç seviyeleri hesaplar.

    Destek:
        Son dönemde görülen en düşük fiyat.

    Direnç:
        Son dönemde görülen en yüksek fiyat.
    """

    if len(df) < window:
        raise ValueError(
            f"Destek/direnç hesaplamak için en az "
            f"{window} fiyat verisi gerekli."
        )

    recent = df.tail(window)

    support = float(recent["low"].min())
    resistance = float(recent["high"].max())
    current_price = float(df["close"].iloc[-1])

    return {
        "support": support,
        "resistance": resistance,
        "current_price": current_price,
    }


def calculate_support_resistance_score(df, window=20):
    """
    Fiyatın destek ve direnç seviyelerine göre
    basit teknik skor üretir.

    0-100 arası skor döndürür.
    """

    levels = calculate_support_resistance(
        df,
        window
    )

    current_price = levels["current_price"]
    support = levels["support"]
    resistance = levels["resistance"]

    price_range = resistance - support

    if price_range <= 0:
        return 50

    position = (
        current_price - support
    ) / price_range

    if position <= 0.20:
        return 70

    elif position <= 0.40:
        return 80

    elif position <= 0.60:
        return 90

    elif position <= 0.80:
        return 75

    else:
        return 55
import pandas as pd


def calculate_rsi(prices, period=14):
    delta = prices.diff()

    gains = delta.clip(lower=0)
    losses = -delta.clip(upper=0)

    average_gain = gains.rolling(period).mean()
    average_loss = losses.rolling(period).mean()

    rs = average_gain / average_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi


def calculate_moving_averages(prices):
    return {
        "ma20": prices.rolling(20).mean(),
        "ma50": prices.rolling(50).mean(),
        "ma200": prices.rolling(200).mean(),
    }


def calculate_volume_change(volume):
    return volume.pct_change()


def calculate_macd(prices):
    """
    MACD hesaplar.

    MACD = EMA12 - EMA26
    Signal = MACD'nin 9 günlük EMA'sı
    Histogram = MACD - Signal
    """

    ema12 = prices.ewm(span=12, adjust=False).mean()
    ema26 = prices.ewm(span=26, adjust=False).mean()

    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()

    histogram = macd - signal

    return {
        "macd": macd,
        "signal": signal,
        "histogram": histogram,
    }


def calculate_momentum(prices, period=20):
    """
    Son fiyatın belirli bir dönem önceki fiyata
    göre değişimini hesaplar.
    """

    return prices.pct_change(periods=period)


def calculate_volatility(prices, period=20):
    """
    Günlük getirilerin hareketli standart sapmasını
    hesaplar.
    """

    returns = prices.pct_change()

    return returns.rolling(period).std()


def technical_summary(df):
    prices = df["close"]
    volume = df["volume"]

    ma = calculate_moving_averages(prices)
    rsi = calculate_rsi(prices)

    macd = calculate_macd(prices)

    momentum = calculate_momentum(prices)
    volatility = calculate_volatility(prices)

    return {
        "rsi": float(rsi.iloc[-1]),

        "ma20": float(ma["ma20"].iloc[-1]),
        "ma50": float(ma["ma50"].iloc[-1]),
        "ma200": float(ma["ma200"].iloc[-1]),

        "volume_change": float(
            calculate_volume_change(volume).iloc[-1]
        ),

        "macd": float(macd["macd"].iloc[-1]),
        "macd_signal": float(macd["signal"].iloc[-1]),
        "macd_histogram": float(
            macd["histogram"].iloc[-1]
        ),

        "momentum_20": float(
            momentum.iloc[-1]
        ),

        "volatility_20": float(
            volatility.iloc[-1]
        ),
    }


def calculate_technical_score(df):
    prices = df["close"]

    summary = technical_summary(df)

    score = 0

    # ==============================
    # RSI — 15 PUAN
    # ==============================

    rsi = summary["rsi"]

    if 50 <= rsi < 60:
        score += 10

    elif 60 <= rsi < 70:
        score += 15

    elif 70 <= rsi < 80:
        score += 11

    elif rsi >= 80:
        score += 6

    elif 40 <= rsi < 50:
        score += 6

    else:
        score += 2


    # ==============================
    # MA20 / MA50 — 15 PUAN
    # ==============================

    ma20 = summary["ma20"]
    ma50 = summary["ma50"]

    if ma20 > ma50:
        score += 15
    else:
        score += 4


    # ==============================
    # MA50 / MA200 — 20 PUAN
    # ==============================

    ma200 = summary["ma200"]

    if ma50 > ma200:
        score += 20
    else:
        score += 4


    # ==============================
    # FİYAT / MA200 — 15 PUAN
    # ==============================

    current_price = prices.iloc[-1]

    if current_price > ma200:
        score += 15
    else:
        score += 4


    # ==============================
    # MACD — 15 PUAN
    # ==============================

    macd = summary["macd"]
    signal = summary["macd_signal"]

    if macd > signal:
        score += 15
    else:
        score += 4


    # ==============================
    # MOMENTUM — 10 PUAN
    # ==============================

    momentum = summary["momentum_20"]

    if momentum > 0.10:
        score += 10

    elif momentum > 0:
        score += 7

    elif momentum > -0.10:
        score += 4

    else:
        score += 1


    # ==============================
    # HACİM — 5 PUAN
    # ==============================
        # ==============================
    # VOLATİLİTE — 5 PUAN
    # ==============================

    volatility = summary["volatility_20"]

    if volatility < 0.01:
        score += 5

    elif volatility < 0.02:
        score += 4

    elif volatility < 0.03:
        score += 2

    else:
        score += 1

    volume_change = summary["volume_change"]

    if volume_change > 0.20:
        score += 5

    elif volume_change > 0:
        score += 4

    elif volume_change > -0.20:
        score += 2

    else:
        score += 1


    return min(score, 100)
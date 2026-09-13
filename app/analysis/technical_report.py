from technical import (
    technical_summary,
    calculate_technical_score,
)

from support_resistance import (
    calculate_support_resistance,
    calculate_support_resistance_score,
)


def create_technical_report(df):
    """
    Bir hissenin teknik analiz sonuçlarını
    tek bir raporda birleştirir.
    """

    technical = technical_summary(df)

    levels = calculate_support_resistance(df)

    support_resistance_score = (
        calculate_support_resistance_score(df)
    )

    return {
        "rsi": technical["rsi"],

        "ma20": technical["ma20"],
        "ma50": technical["ma50"],
        "ma200": technical["ma200"],

        "macd": technical["macd"],
        "macd_signal": technical["macd_signal"],
        "macd_histogram": technical["macd_histogram"],

        "momentum_20": technical["momentum_20"],
        "volatility_20": technical["volatility_20"],
        "volume_change": technical["volume_change"],

        "support": levels["support"],
        "resistance": levels["resistance"],
        "current_price": levels["current_price"],

        "technical_score": calculate_technical_score(df),

        "support_resistance_score": (
            support_resistance_score
        ),
    }
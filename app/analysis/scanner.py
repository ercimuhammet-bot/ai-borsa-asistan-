from stock_score import calculate_stock_score, score_label
from fundamental import fundamental_score
from technical import calculate_technical_score
from investment_score import calculate_investment_score
from signal import create_signal_result


def scan_stock(
    symbol,
    price_data,
    financial_data,
    risk_score,
    kap_score=0
):
    """
    Bir hisseyi temel + teknik + risk + KAP
    analizi ile değerlendirir.
    """

    # Teknik analiz
    technical = calculate_technical_score(price_data)

    # Temel analiz
    fundamental = fundamental_score(financial_data)

    # Temel + teknik genel hisse skoru
    total = calculate_stock_score(
        fundamental,
        technical
    )

    # Risk + KAP + genel hisse skorundan
    # yatırım skoru
    investment = calculate_investment_score(
        total,
        risk_score,
        kap_score
    )

    # Nihai AL / TUT / SAT sinyali
    signal = create_signal_result(
        investment,
        risk_score,
        kap_score
    )

    return {
        "symbol": symbol,

        "fundamental_score": fundamental,
        "technical_score": technical,
        "total_score": total,

        "risk_score": risk_score,

        "kap_score": kap_score,

        "investment_score": investment,

        "label": score_label(total),

        "signal": signal["signal"],
        "signal_emoji": signal["emoji"],
        "display": signal["display"],
    }


def scan_stocks(stock_data):
    """
    Birden fazla hisseyi tarar.
    """

    results = []

    for symbol, data in stock_data.items():

        result = scan_stock(
            symbol,
            data["price_data"],
            data["financial_data"],
            data["risk_score"],
            data.get("kap_score", 0)
        )

        results.append(result)

    results.sort(
        key=lambda x: x["investment_score"],
        reverse=True
    )

    return results
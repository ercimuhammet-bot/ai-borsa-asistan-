def calculate_investment_score(
    stock_score,
    risk_score,
    kap_score=0
):
    """
    Hisse genel skoru + risk + KAP etkisini
    birleştirir.

    stock_score : 0-100
    risk_score  : 0-100
    kap_score   : -100 ile +100

    KAP etkisi toplam skorun küçük bir bölümünü
    etkiler.
    """

    # KAP etkisini 0-100 ölçeğine çeviriyoruz.
    kap_normalized = 50 + (kap_score / 2)

    score = (
        stock_score * 0.55 +
        risk_score * 0.25 +
        kap_normalized * 0.20
    )

    return round(
        max(0, min(score, 100)),
        2
    )


def investment_label(
    investment_score,
    stock_score,
    risk_score,
    kap_score=0
):
    """
    Genel yatırım değerlendirmesi.
    """

    if investment_score >= 85 and risk_score >= 75:
        return "ÇOK GÜÇLÜ"

    elif investment_score >= 75 and risk_score >= 60:
        return "GÜÇLÜ"

    elif investment_score >= 65:
        return "OLUMLU"

    elif investment_score >= 50:
        return "İZLE"

    else:
        return "ZAYIF"
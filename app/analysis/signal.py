def generate_signal(
    investment_score,
    risk_score,
    kap_score=0
):
    """
    Yatırım skoru + risk + KAP etkisine göre
    AL / TUT / SAT sinyali üretir.
    """

    if risk_score < 40:
        return "SAT"

    if investment_score >= 80 and risk_score >= 60:
        return "AL"

    elif investment_score >= 60 and risk_score >= 50:
        return "TUT"

    else:
        return "SAT"


def generate_signal_reason(
    investment_score,
    risk_score,
    kap_score=0
):
    """
    Sinyalin sistem içindeki nedenini açıklar.
    """

    if risk_score < 40:
        return "Risk çok yüksek"

    if investment_score >= 80 and risk_score >= 60:
        if kap_score > 0:
            return "Güçlü skor + uygun risk + pozitif KAP"
        elif kap_score < 0:
            return "Güçlü skor + uygun risk + negatif KAP"
        else:
            return "Güçlü skor + uygun risk"

    if investment_score >= 60 and risk_score >= 50:
        if kap_score > 0:
            return "Orta güçlü skor + pozitif KAP"
        elif kap_score < 0:
            return "Orta güçlü skor + negatif KAP"
        else:
            return "Orta güçlü skor"

    return "Yatırım skoru yetersiz"


def signal_emoji(signal):

    if signal == "AL":
        return "🟢"

    elif signal == "TUT":
        return "🟡"

    return "🔴"


def create_signal_result(
    investment_score,
    risk_score,
    kap_score=0
):
    """
    Kullanıcıya gösterilecek sinyal sonucunu oluşturur.
    """

    signal = generate_signal(
        investment_score,
        risk_score,
        kap_score
    )

    emoji = signal_emoji(signal)

    reason = generate_signal_reason(
        investment_score,
        risk_score,
        kap_score
    )

    return {
        "signal": signal,
        "emoji": emoji,
        "display": f"{emoji} {signal}",
        "reason": reason,
    }
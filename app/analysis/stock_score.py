def calculate_stock_score(
    fundamental_score,
    technical_score
):
    """
    İlk prototip hisse skoru.

    Şimdilik:
    Temel analiz: %60
    Teknik analiz: %40

    Momentum ve risk motorları
    sonraki aşamada eklenecek.
    """

    score = (
        fundamental_score * 0.60 +
        technical_score * 0.40
    )

    return round(score, 2)


def score_label(score):

    if score >= 85:
        return "ÇOK GÜÇLÜ"

    elif score >= 75:
        return "GÜÇLÜ"

    elif score >= 65:
        return "OLUMLU"

    elif score >= 50:
        return "İZLE"

    else:
        return "ZAYIF"
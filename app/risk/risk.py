def calculate_risk_score(
    volatility,
    net_debt_ebitda,
    interest_expense_to_ebitda,
    interest_income_ratio,
):
    """
    Hisse için temel risk skorunu hesaplar.

    100 = düşük risk
    0   = yüksek risk
    """

    score = 100

    # ==============================
    # VOLATİLİTE
    # ==============================

    if volatility <= 0.01:
        score -= 5

    elif volatility <= 0.02:
        score -= 15

    elif volatility <= 0.03:
        score -= 25

    elif volatility <= 0.05:
        score -= 40

    else:
        score -= 55


    # ==============================
    # NET BORÇ / FAVÖK
    # ==============================

    if net_debt_ebitda <= 1:
        score -= 0

    elif net_debt_ebitda <= 2:
        score -= 10

    elif net_debt_ebitda <= 3:
        score -= 20

    elif net_debt_ebitda <= 4:
        score -= 35

    else:
        score -= 50


    # ==============================
    # FAİZ GİDERİ / FAVÖK
    # ==============================

    if interest_expense_to_ebitda <= 0.10:
        score -= 0

    elif interest_expense_to_ebitda <= 0.20:
        score -= 5

    elif interest_expense_to_ebitda <= 0.35:
        score -= 15

    elif interest_expense_to_ebitda <= 0.50:
        score -= 25

    else:
        score -= 40


    # ==============================
    # FAİZ GELİRİNE BAĞIMLILIK
    # ==============================

    if interest_income_ratio <= 0.05:
        score -= 0

    elif interest_income_ratio <= 0.10:
        score -= 5

    elif interest_income_ratio <= 0.20:
        score -= 10

    elif interest_income_ratio <= 0.30:
        score -= 20

    else:
        score -= 30


    return max(0, min(score, 100))


def risk_label(score):

    if score >= 80:
        return "DÜŞÜK RİSK"

    elif score >= 60:
        return "ORTA RİSK"

    elif score >= 40:
        return "YÜKSEK RİSK"

    else:
        return "ÇOK YÜKSEK RİSK"
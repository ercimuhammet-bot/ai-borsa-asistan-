def growth_score(revenue_growth, profit_growth, ebitda_growth):
    score = 0

    # Ciro büyümesi — 30 puan
    if revenue_growth >= 0.30:
        score += 30
    elif revenue_growth >= 0.15:
        score += 24
    elif revenue_growth >= 0.05:
        score += 16
    elif revenue_growth >= 0:
        score += 8

    # Net kâr büyümesi — 40 puan
    if profit_growth >= 0.30:
        score += 40
    elif profit_growth >= 0.15:
        score += 32
    elif profit_growth >= 0.05:
        score += 22
    elif profit_growth >= 0:
        score += 10

    # FAVÖK büyümesi — 30 puan
    if ebitda_growth >= 0.30:
        score += 30
    elif ebitda_growth >= 0.15:
        score += 24
    elif ebitda_growth >= 0.05:
        score += 16
    elif ebitda_growth >= 0:
        score += 8

    return min(score, 100)


def profitability_score(roe, net_margin, roic):
    score = 0

    # ROE — 40 puan
    if roe >= 0.30:
        score += 40
    elif roe >= 0.20:
        score += 32
    elif roe >= 0.10:
        score += 22
    elif roe > 0:
        score += 10

    # Net kâr marjı — 30 puan
    if net_margin >= 0.20:
        score += 30
    elif net_margin >= 0.10:
        score += 24
    elif net_margin >= 0.05:
        score += 15
    elif net_margin > 0:
        score += 7

    # ROIC — 30 puan
    if roic >= 0.20:
        score += 30
    elif roic >= 0.12:
        score += 24
    elif roic >= 0.06:
        score += 15
    elif roic > 0:
        score += 7

    return min(score, 100)


def debt_score(net_debt_ebitda):
    if net_debt_ebitda < 0:
        return 100
    elif net_debt_ebitda <= 1:
        return 90
    elif net_debt_ebitda <= 2:
        return 75
    elif net_debt_ebitda <= 3:
        return 55
    elif net_debt_ebitda <= 4:
        return 35
    else:
        return 15


def valuation_score(pe, pb, ev_ebitda):
    score = 0

    # F/K
    if 0 < pe <= 8:
        score += 35
    elif pe <= 12:
        score += 28
    elif pe <= 18:
        score += 20
    elif pe <= 25:
        score += 10

    # PD/DD
    if 0 < pb <= 1:
        score += 35
    elif pb <= 2:
        score += 28
    elif pb <= 4:
        score += 18
    elif pb <= 6:
        score += 10

    # FD/FAVÖK
    if 0 < ev_ebitda <= 6:
        score += 30
    elif ev_ebitda <= 9:
        score += 24
    elif ev_ebitda <= 12:
        score += 16
    elif ev_ebitda <= 18:
        score += 8

    return min(score, 100)


def fundamental_score(data):
    growth = growth_score(
        data["revenue_growth"],
        data["profit_growth"],
        data["ebitda_growth"]
    )

    profitability = profitability_score(
        data["roe"],
        data["net_margin"],
        data["roic"]
    )

    debt = debt_score(
        data["net_debt_ebitda"]
    )

    valuation = valuation_score(
        data["pe"],
        data["pb"],
        data["ev_ebitda"]
    )

    total = (
        growth * 0.30 +
        profitability * 0.30 +
        debt * 0.20 +
        valuation * 0.20
    )

    return round(total, 2)
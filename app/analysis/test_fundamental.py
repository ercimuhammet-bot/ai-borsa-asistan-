from fundamental import fundamental_score


company = {
    "revenue_growth": 0.24,
    "profit_growth": 0.31,
    "ebitda_growth": 0.20,
    "roe": 0.28,
    "net_margin": 0.15,
    "roic": 0.18,
    "net_debt_ebitda": 1.2,
    "pe": 10,
    "pb": 1.8,
    "ev_ebitda": 7
}


score = fundamental_score(company)

print("==============================")
print("AI BORSA ASISTANI")
print("TEMEL ANALİZ TESTİ")
print("==============================")
print(f"TEMEL SKOR: {score}/100")
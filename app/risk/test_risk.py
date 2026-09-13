from risk import calculate_risk_score, risk_label


risk_score = calculate_risk_score(
    volatility=0.018,
    net_debt_ebitda=1.2,
    interest_expense_to_ebitda=0.12,
    interest_income_ratio=0.04,
)


print()
print("==============================")
print("AI BORSA ASISTANI")
print("RİSK MOTORU TESTİ")
print("==============================")

print(f"Risk Skoru: {risk_score}/100")
print(f"Risk Seviyesi: {risk_label(risk_score)}")
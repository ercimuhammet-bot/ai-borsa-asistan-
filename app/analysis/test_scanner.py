import pandas as pd
import numpy as np

from scanner import scan_stocks


np.random.seed(42)


def create_price_data():

    days = 250

    prices = 100 + np.cumsum(
        np.random.normal(0.3, 1.5, days)
    )

    volume = np.random.randint(
        100000,
        1000000,
        days
    )

    return pd.DataFrame({
        "high": prices + 2,
        "low": prices - 2,
        "close": prices,
        "volume": volume
    })


financial_data = {
    "revenue_growth": 0.24,
    "profit_growth": 0.31,
    "ebitda_growth": 0.20,
    "roe": 0.28,
    "net_margin": 0.15,
    "roic": 0.18,
    "net_debt_ebitda": 1.2,
    "pe": 10,
    "pb": 1.8,
    "ev_ebitda": 7,

    "interest_income": 1500000,
    "interest_expense": 500000,
    "interest_income_ratio": 0.15,
    "interest_income_to_profit": 0.75,
    "interest_expense_to_ebitda": 0.12,
}


stock_data = {

    "ASELS": {
        "price_data": create_price_data(),
        "financial_data": financial_data,
        "risk_score": 80,
        "kap_score": 50
    },

    "THYAO": {
        "price_data": create_price_data(),
        "financial_data": financial_data,
        "risk_score": 70,
        "kap_score": 0
    },

    "TUPRS": {
        "price_data": create_price_data(),
        "financial_data": financial_data,
        "risk_score": 55,
        "kap_score": -50
    }
}


results = scan_stocks(stock_data)


print()
print("==============================")
print("AI BORSA ASISTANI")
print("HİSSE TARAMA TESTİ")
print("==============================")


for result in results:

    print(
        f"{result['symbol']} | "
        f"Temel: {result['fundamental_score']} | "
        f"Teknik: {result['technical_score']} | "
        f"Genel: {result['total_score']} | "
        f"Risk: {result['risk_score']} | "
        f"KAP: {result['kap_score']:+} | "
        f"Yatırım: {result['investment_score']} | "
        f"SİNYAL: {result['display']}"
    )
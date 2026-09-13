from bist_data import (
    get_price_data,
    get_financial_data,
    get_company_info,
)


symbol = "THYAO"


print("==============================")
print("AI BORSA ASISTANI")
print("VERİ ALTYAPISI TESTİ")
print("==============================")


print("\n--- FİYAT VERİSİ ---")

prices = get_price_data(symbol)

print(prices)


print("\n--- FİNANSAL VERİ ---")

financials = get_financial_data(symbol)

for key, value in financials.items():
    print(f"{key}: {value}")


print("\n--- ŞİRKET BİLGİSİ ---")

company = get_company_info(symbol)

for key, value in company.items():
    print(f"{key}: {value}")
from data_provider import create_data_provider


provider = create_data_provider()

symbol = "THYAO"


print("==============================")
print("AI BORSA ASISTANI")
print("DATA PROVIDER TESTİ")
print("==============================")


print("\n--- ŞİRKET BİLGİSİ ---")

company = provider.get_company_info(symbol)

for key, value in company.items():
    print(f"{key}: {value}")


print("\n--- FİNANSAL VERİ ---")

financials = provider.get_financial_data(symbol)

for key, value in financials.items():
    print(f"{key}: {value}")


print("\n--- FİYAT VERİSİ ---")

prices = provider.get_price_data(symbol)

print(prices)
def create_stock_report(
    symbol,
    fundamental_score,
    technical_score,
    stock_score,
    risk_score,
    risk_label,
    investment_score,
    investment_label,
    kap_status,
    kap_score,
    financial_data,
):
    """
    Tek bir hisse için birleşik analiz raporu oluşturur.
    """

    print()
    print("=" * 50)
    print(f"{symbol} — AI BORSA ANALİZ RAPORU")
    print("=" * 50)

    print()
    print("SKORLAR")
    print("-" * 50)

    print(f"Temel Analiz Skoru : {fundamental_score}/100")
    print(f"Teknik Analiz Skoru: {technical_score}/100")
    print(f"Genel Hisse Skoru  : {stock_score}/100")

    print()
    print("RİSK")
    print("-" * 50)

    print(f"Risk Skoru         : {risk_score}/100")
    print(f"Risk Seviyesi      : {risk_label}")

    print()
    print("YATIRIM DEĞERLENDİRMESİ")
    print("-" * 50)

    print(f"Yatırım Skoru      : {investment_score}/100")
    print(f"Değerlendirme      : {investment_label}")

    print()
    print("FAİZ / FİNANSAL GÖSTERGELER")
    print("-" * 50)

    print(
        f"Faiz Geliri        : "
        f"{financial_data.get('interest_income')}"
    )

    print(
        f"Faiz Gideri        : "
        f"{financial_data.get('interest_expense')}"
    )

    print(
        f"Faiz Geliri Oranı  : "
        f"{financial_data.get('interest_income_ratio')}"
    )

    print(
        f"Faiz Geliri / Kâr  : "
        f"{financial_data.get('interest_income_to_profit')}"
    )

    print(
        f"Faiz Gideri/FAVÖK  : "
        f"{financial_data.get('interest_expense_to_ebitda')}"
    )

    print()
    print("KAP")
    print("-" * 50)

    print(f"KAP Durumu         : {kap_status}")
    print(f"KAP Etki Skoru     : {kap_score}")

    print()
    print("=" * 50)
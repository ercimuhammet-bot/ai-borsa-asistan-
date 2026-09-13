import pandas as pd


def get_price_data(symbol):
    """
    BIST hisse fiyat verisi için veri sağlayıcı arayüzü.

    Şimdilik test verisi döndürür.
    Daha sonra gerçek BIST veri sağlayıcısına bağlanacaktır.
    """

    data = {
        "date": [
            "2026-09-01",
            "2026-09-02",
            "2026-09-03",
            "2026-09-04",
            "2026-09-05",
        ],
        "open": [
            100,
            101,
            102,
            103,
            104,
        ],
        "high": [
            102,
            103,
            104,
            105,
            106,
        ],
        "low": [
            99,
            100,
            101,
            102,
            103,
        ],
        "close": [
            101,
            102,
            103,
            104,
            105,
        ],
        "volume": [
            500000,
            550000,
            600000,
            650000,
            700000,
        ],
    }

    df = pd.DataFrame(data)

    df["date"] = pd.to_datetime(df["date"])

    return df


def get_financial_data(symbol):
    """
    Finansal tablo verileri için veri sağlayıcı arayüzü.

    Daha sonra KAP / lisanslı veri sağlayıcısından
    gerçek finansal veriler alınacaktır.
    """

    return {
        "symbol": symbol,

        # Büyüme
        "revenue_growth": None,
        "profit_growth": None,
        "ebitda_growth": None,

        # Karlılık
        "roe": None,
        "net_margin": None,
        "roic": None,

        # Borçluluk
        "net_debt_ebitda": None,

        # Değerleme
        "pe": None,
        "pb": None,
        "ev_ebitda": None,

        # ==============================
        # FAİZ GELİRİ / GİDERİ
        # ==============================

        "interest_income": None,
        "interest_expense": None,

        # Faiz geliri / toplam gelir
        "interest_income_ratio": None,

        # Faiz geliri / net kâr
        "interest_income_to_profit": None,

        # Faiz gideri / FAVÖK
        "interest_expense_to_ebitda": None,
    }

    return {
        "symbol": symbol,
        "revenue_growth": None,
        "profit_growth": None,
        "ebitda_growth": None,
        "roe": None,
        "net_margin": None,
        "roic": None,
        "net_debt_ebitda": None,
        "pe": None,
        "pb": None,
        "ev_ebitda": None,
    }


def get_company_info(symbol):
    """
    Şirket temel bilgileri.
    """

    return {
        "symbol": symbol,
        "name": None,
        "sector": None,
    }
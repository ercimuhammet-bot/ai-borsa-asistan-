from bist_data import (
    get_price_data,
    get_financial_data,
    get_company_info,
)


class BISTDataProvider:
    """
    BIST veri sağlayıcısı için standart arayüz.

    Şimdilik mevcut test veri kaynağını kullanır.
    Daha sonra gerçek veri sağlayıcısı buraya bağlanacaktır.
    """

    def get_price_data(self, symbol):
        return get_price_data(symbol)

    def get_financial_data(self, symbol):
        return get_financial_data(symbol)

    def get_company_info(self, symbol):
        return get_company_info(symbol)


def create_data_provider():
    return BISTDataProvider()
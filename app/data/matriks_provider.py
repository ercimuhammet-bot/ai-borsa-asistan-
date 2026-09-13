import os


class MatriksDataProvider:
    """
    Matriks API için veri sağlayıcı.

    API bağlantısı aktif olduğunda gerçek verileri
    bu sınıf üzerinden alacağız.
    """

    def __init__(self):
        self.api_key = os.getenv("MATRIKS_API_KEY")
        self.base_url = os.getenv(
            "MATRIKS_BASE_URL",
            ""
        )

    def is_configured(self):
        """
        Matriks API bilgilerinin girilip
        girilmediğini kontrol eder.
        """

        return bool(
            self.api_key and
            self.base_url
        )

    def get_price_data(self, symbol):
        """
        Gerçek fiyat verisi daha sonra burada alınacak.
        """

        if not self.is_configured():
            raise RuntimeError(
                "Matriks API henüz yapılandırılmadı."
            )

        raise NotImplementedError(
            "Matriks fiyat API bağlantısı "
            "henüz eklenmedi."
        )

    def get_financial_data(self, symbol):
        """
        Gerçek finansal veriler daha sonra burada alınacak.
        """

        if not self.is_configured():
            raise RuntimeError(
                "Matriks API henüz yapılandırılmadı."
            )

        raise NotImplementedError(
            "Matriks finansal veri bağlantısı "
            "henüz eklenmedi."
        )

    def get_kap_news(self, symbol):
        """
        KAP haberleri daha sonra burada alınacak.
        """

        if not self.is_configured():
            raise RuntimeError(
                "Matriks API henüz yapılandırılmadı."
            )

        raise NotImplementedError(
            "Matriks KAP bağlantısı "
            "henüz eklenmedi."
        )
from data_provider import create_data_provider
from matriks_provider import MatriksDataProvider


def create_best_provider():
    """
    Kullanılabilir en iyi veri sağlayıcısını seçer.

    Matriks API yapılandırılmışsa:
        Matriks kullanılır.

    Matriks yapılandırılmamışsa:
        Test veri sağlayıcısı kullanılır.
    """

    matriks = MatriksDataProvider()

    if matriks.is_configured():
        return matriks

    return create_data_provider()
def classify_kap_event(title, content=""):
    """
    KAP açıklamasını basit şekilde sınıflandırır.
    """

    text = f"{title} {content}".lower()

    positive_keywords = [
        "ihale",
        "yatırım",
        "yeni sipariş",
        "sözleşme",
        "temettü",
        "kapasite artışı",
        "geri alım",
    ]

    negative_keywords = [
        "zarar",
        "borç",
        "finansman",
        "dava",
        "ceza",
        "sermaye azaltımı",
        "temerrüt",
    ]

    positive = sum(
        1 for word in positive_keywords
        if word in text
    )

    negative = sum(
        1 for word in negative_keywords
        if word in text
    )

    if positive > negative:
        return "POZİTİF"

    elif negative > positive:
        return "NEGATİF"

    return "NÖTR"


def kap_score(title, content=""):
    """
    KAP açıklaması için -100 / +100 arasında
    basit etki skoru üretir.
    """

    classification = classify_kap_event(
        title,
        content
    )

    if classification == "POZİTİF":
        return 50

    elif classification == "NEGATİF":
        return -50

    return 0
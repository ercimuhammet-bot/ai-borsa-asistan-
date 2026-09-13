from matriks_provider import MatriksDataProvider


provider = MatriksDataProvider()

print("==============================")
print("MATRİKS VERİ SAĞLAYICI TESTİ")
print("==============================")

print()
print("API yapılandırıldı mı?:", provider.is_configured())

print()
print("API anahtarı mevcut mu?:", bool(provider.api_key))
print("Base URL mevcut mu?:", bool(provider.base_url))
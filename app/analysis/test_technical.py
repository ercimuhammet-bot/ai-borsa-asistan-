import pandas as pd
import numpy as np

from technical import technical_summary, calculate_technical_score


# Test amaçlı örnek fiyat verisi
np.random.seed(42)

days = 250

prices = 100 + np.cumsum(
    np.random.normal(0.3, 1.5, days)
)

volume = np.random.randint(
    100000,
    1000000,
    days
)

df = pd.DataFrame({
    "close": prices,
    "volume": volume
})


result = technical_summary(df)


print("\n===== AI BORSA ASİSTANI =====")
print("TEKNİK ANALİZ TESTİ")
print("==============================")

for key, value in result.items():
    print(f"{key}: {value:.4f}")
    technical_score = calculate_technical_score(df)

print("\n------------------------------")
print(f"TEKNİK SKOR: {technical_score}/100")
print("------------------------------")
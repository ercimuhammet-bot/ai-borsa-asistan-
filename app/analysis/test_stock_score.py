from stock_score import calculate_stock_score, score_label


fundamental = 81.4
technical = 83


score = calculate_stock_score(
    fundamental,
    technical
)

label = score_label(score)


print("==============================")
print("AI BORSA ASISTANI")
print("HİSSE SKORU")
print("==============================")

print(f"Temel Analiz : {fundamental}/100")
print(f"Teknik Analiz: {technical}/100")
print("------------------------------")
print(f"GENEL SKOR   : {score}/100")
print(f"SONUÇ        : {label}")
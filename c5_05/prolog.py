# Przeprowadź analizę eksploracyjną zbioru danych dotyczących pacjentów korzystających z ubezpieczenia zdrowotnego.
# Zbiór danych jest stosunkowo mały. Zawiera 1338 obserwacji oraz 7 cech. Oto one:

# Wiek
# Płeć
# BMI
# Liczba dzieci
# Czy palacz
# Region
# Opłaty za leczenie
# Ostatnia cecha to nasza zmien
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dane = pd.read_csv("./data/insurance.csv")

print(dane.head())

print(f'Ten zbiór zawiera {dane.shape[0]} obserwacji oraz {dane.shape[1]} cech')
print(dane.dtypes)
print(dane.describe(include=object))

print(dane.sex.value_counts().rename("Plec"))
print(dane.smoker.value_counts())
print(dane.region.value_counts())
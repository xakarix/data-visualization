# Sprawdź czy pomiędzy zmiennymi ilościowymi zachodzi współliniowość.
# Wskazówka: należy wyświetlić mapę ciepła dla macierzy korelacji pomiędzy zmiennymi ilościowymi

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dane = pd.read_csv("./data/insurance.csv")

corr = dane.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='RdBu', fmt=".2f", linewidths=0.5, vmin=-1, vmax=1)
plt.show()


#?
plt.figure(figsize=(10, 10))
dane_encoded = dane.copy()
dane_encoded['sex'] = dane_encoded['sex'].map({'male': 0, 'female': 1})
dane_encoded['smoker'] = dane_encoded['smoker'].map({'no': 0, 'yes': 1})
dane_encoded['region'] = dane_encoded['region'].astype('category').cat.codes
corr_matrix = dane_encoded.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Mapa ciepła korelacji")
plt.show()


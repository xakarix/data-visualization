# Sprawdź jak kształtuje się rozkład zmiennej objąśnianej.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dane = pd.read_csv("./data/insurance.csv")

plt.figure(figsize=(10,6))
sns.histplot(dane['charges'], kde=True, color='royalblue', bins=10)
plt.title("Rozkład zmiennej objaśniającej")
plt.ylabel('Liczba obserwacji')
plt.xlabel('Opłata za leczenie')

plt.show()
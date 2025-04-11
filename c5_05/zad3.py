# Przeprowadź wizualną analizę statystyczną pozostałych zmiennych ilościowych. Wizualizacje powinny odpowiadać na pytania:

# Jaki jest rozkładem danej zmiennej?
# Czy zmiany danej zmiennej wyjaśniają zmiany zmiennej objaśnianej?
# Wskazówka: należy sprawdzić rozkład danej zmiennej oraz w jakiej pozostaje relacji ze zmienną objaśnianą

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dane = pd.read_csv("./data/insurance.csv")

variables = ['age', 'bmi', 'children']

for var in variables:
    plt.figure(figsize=(12,6))

    #rozkład
    plt.subplot(1,2,1)
    sns.histplot(dane[var], kde=True, color='royalblue', bins=30)
    plt.title(f"Rozkład zmiennej {var}")
    plt.xlabel(var)
    plt.ylabel('Częstotliwość')

    #relacja
    plt.subplot(1,2,2)
    sns.scatterplot(x=dane[var], y=dane['charges'], color='darkorange')
    plt.title(f'Relacja zmiennej {var} z charges')
    plt.xlabel(var)
    plt.ylabel('Opłata za leczenie')

    plt.tight_layout()
    plt.show()
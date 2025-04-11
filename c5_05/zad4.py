# Przeprowadź wizualną analizę statystyczną zmiennych jakościowych. Wizualizacje powinny odpowiedzieć na pytania:

# Czy zmienne skokowe dzielą zbiór danych na zbalansowane ilościowo części?
# Czy podział po zmiennej skokowej jest w stanie wyjaśnić zmiany wartości zmiennej objaśnianej?
# Wskazówka: należy sprawdzić rozkład danej zmiennej oraz w jakiej pozostaje relacji ze zmienną objaśnianą

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dane = pd.read_csv("./data/insurance.csv")

variables = ['sex', 'smoker', 'region']

plt.figure(figsize=(16,12))

for i, var in enumerate(variables,1):
    plt.subplot(2,3,i)

    #rozkład
    sns.barplot(x=dane[var].value_counts().index, y=dane[var].value_counts(), palette='Set2')
    plt.title(f'Rozkład zmiennej {var}')
    plt.xlabel(var)
    plt.ylabel('Częstotliwość')

    #relacja
    plt.subplot(2,3,i+3)
    sns.boxplot(data=dane, x=var, y='charges', palette='Set2')
    plt.title(f"Relacja zmiennej {var} z charges")
    plt.xlabel(var)
    plt.ylabel('Opłata za leczenie')

plt.tight_layout
plt.show()

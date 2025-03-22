# a)
# Korzystając z danych znajdujących się w pliku dane.csv wczytaj dane a nastepnie wyświetl informacje o miesiącu i sprzedaży 
# produktu A większej od średniej sprzedaży tego produktu wyniki uporządkuj po miesiącu zachowując porządek zgodny z kolejnością miesięcy
#  a w obrębie miesiąca po wielkości sprzedaży.

# b)
# Zlicz ile było dni ze sprzedażą powyżej średniej, wyniki przedstaw na wykresie.

import matplotlib.pyplot as plt
import pandas as pd
import random
from math import floor, ceil

dane = pd.read_csv('c3_03/dane.csv', sep=';', decimal=',', index_col = 0)

miesiace = ['styczen', 'luty', 'marzec']

srednia_prodA = dane['prodA'].mean()
pow_sredniej = dane[dane['prodA'] > srednia_prodA]

filtrowane_dane = pow_sredniej[['Miesiac', 'prodA']]

filtrowane_dane['Miesiac'] = pd.Categorical(filtrowane_dane['Miesiac'], categories = miesiace, ordered = True)
filtrowane_dane = filtrowane_dane.sort_values(['Miesiac', 'prodA'], ascending = [True, False])

print(filtrowane_dane)

# liczba_dni = pow_sredniej['Miesiac'].value_counts().reindex(['styczen', 'luty', 'marzec'], fill_value=0)
dni = pow_sredniej['Miesiac'].value_counts().reindex(['styczen', 'luty', 'marzec'], fill_value = 0)

fig, ax = plt.subplots(figsize=(8,6))
dni.plot(kind='bar', ax=ax)

plt.title('Liczba dni ze sprzedażą powyżej średniej wielkości sprzedaży')
plt.xlabel('')
plt.ylabel('Liczba dni')

plt.grid(axis='y', color='gray', linestyle='-', linewidth=0.5)
plt.yticks([1,18,24])
plt.xticks(rotation=0)


plt.show()
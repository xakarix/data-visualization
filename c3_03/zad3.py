# Korzystając z danych znajdujących się w pliku dane.csv wczytaj dane a nastepnie dla sprzedaży z marca wyświetl kolumny sprzedaży produktów A i B,
# wiersze uporządkuj malejąco dla produktu A.
# Wyniki przedstaw na wykresie punktowym.

import matplotlib.pyplot as plt
import pandas as pd
import random
from math import floor, ceil

dane = pd.read_csv('c3_03/dane.csv', sep=';', decimal=',', index_col = 0)

sprzedaz_marzec = dane[dane['Miesiac'] == 'marzec']

sprzedaz_marzec= sprzedaz_marzec.sort_values(by='prodA', ascending = False)

plt.figure(figsize=[8,5])
plt.scatter(sprzedaz_marzec['prodA'], sprzedaz_marzec['prodB'], color='royalblue')

plt.xlabel('ProdA')
plt.ylabel('ProdB')
plt.title('Sprzedaż produktów A i B w marcu')

plt.show()
# Korzystając z danych znajdujących się w pliku dane.csv wczytaj dane a nastepnie wyznacz sumaryczną sprzedaż dla produktów w każdym miesiącu, 
# wyniki przedstaw na wykresie.

import matplotlib.pyplot as plt
import pandas as pd
import random
from math import floor, ceil

dane = pd.read_csv('c3_03/dane.csv', sep=';', decimal=',', index_col = 0)

suma = dane.groupby('Miesiac')[['prodA', 'prodB']].sum()

sort = suma.sort_values(by='prodA', ascending=True)

sort.plot(kind = 'bar', figsize=(7,6), color = ['royalblue', 'orange'])

plt.title('Sprzedaż produktów A i B w kolejnych miesiącach')
plt.xticks(rotation=0)
plt.legend(loc = 'upper left')

plt.show()
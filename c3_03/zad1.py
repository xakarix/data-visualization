# Korzystając z danych znajdujących się w pliku dane.csv wczytaj dane a nastepnie stwórz nową kolumnę Sprzedaz calkowita. 
# Następnie utworz nową ramkę danych (sprzedaz) bez kolumn sprzedaży poszczególnych produktów.

# Wyświelt sprzedaż całkowitą za pomocą wykresu liniowego.

import matplotlib.pyplot as plt
import pandas as pd
import random
from math import floor, ceil

dane = pd.read_csv('c3_03/dane.csv', sep = ';', decimal = ',', index_col=0)
dane['Sprzedaz całkowita'] = dane['prodA'] + dane['prodB']
sprzedaz = dane.drop(['prodA', 'prodB'], axis = 1)
sprzedaz['mies_cat'] = pd.Categorical(sprzedaz.Miesiac,
                      categories=["styczen","luty","marzec"],
                      ordered=True)

sprzedaz.sort_values(['mies_cat', 'dzien'], inplace = True, ignore_index = True)

s_min = floor(dane['Sprzedaz całkowita'].min())
s_max = ceil(dane['Sprzedaz całkowita'].max())
s_half = round((s_min + s_max) /2)
print(s_min,s_max, s_half)
skala = [s_min, s_min + 2, s_half, s_max -2, s_max]

fig, ax = plt.subplots(figsize = [15, 5])

sprzedaz['Sprzedaz całkowita'].plot(color='blue')
sprzedaz['Sprzedaz całkowita'].plot(title="Sprzeda całkowita w kolejnych dniach kwartału 1.",
                                    xlabel="Dzień",
                                    ylabel="Sprzedaż w tyś.",
                                    ylim=(skala[0], skala[-1]));



plt.xticks([0,30,31,58, 59, 89], labels=[1,31,1, 28, 1, 31])
plt.yticks(ticks = skala, labels=[f'{int(s)}k' for s in skala])

# plt.grid(axis = 'y', linestyle = "--");

ax.axhline(skala[1], color = "gray", linestyle="--", alpha = 0.5);
ax.axhline(skala[2], color = "gray", linestyle="--", alpha = 0.5);
ax.axhline(skala[-2], color = "gray", linestyle="--", alpha = 0.5);

plt.show()

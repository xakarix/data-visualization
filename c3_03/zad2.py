# Z ramki sprzedaz usuń dane z lutego.

import matplotlib.pyplot as plt
import pandas as pd
import random
from math import floor, ceil

dane = pd.read_csv('c3_03/dane.csv', sep = ';', decimal = ',', index_col=0)

dane['Sprzedaz calkowita'] = dane['prodA'] + dane['prodB']
sprzedaz = dane.drop(['prodA', 'prodB'], axis = 1)

sprzedaz = sprzedaz[sprzedaz['Miesiac'] != 'luty']

mies_sprzedaz = sprzedaz.groupby('Miesiac')['Sprzedaz calkowita'].sum()

fig, ax = plt.subplots(figsize = [8,5])
mies_sprzedaz.plot(kind='barh', color='royalblue', ax=ax)
mies_sprzedaz.plot(title = "Sprzeda całkowita w styczniu i w marcu",
                    ylabel = "Miesiąc",
                    xlabel = "")

plt.xticks([50,100,300,350], labels=['50k', '100k', '300k', '350k'])


plt.show()

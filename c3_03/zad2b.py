# Z ramki sprzedaz usuń dane z lutego.

import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv('c3_03/dane.csv', sep = ';', decimal = ',', index_col=0)
dane['Sprzedaz calkowita'] = dane['prodA'] + dane['prodB']
sprzedaz = dane.drop(['prodA', 'prodB'], axis = 1)


mies_sprzedaz = sprzedaz.groupby('Miesiac')['Sprzedaz calkowita'].sum()
dane_styczen = mies_sprzedaz.get('styczen', 0)  
dane_marzec = mies_sprzedaz.get('marzec', 0)


fig, ax = plt.subplots(figsize=[8,5])
ax.barh(['Sprzedaż'], [dane_marzec], color='green', label='marzec')

# Dodanie sprzedaży stycznia na końcu sprzedaży marca
ax.barh( ['Sprzedaż'],[dane_styczen], color='blue', left=[dane_marzec], label='styczen')
plt.ylim(-1, 2)
plt.title('Sprzedaż calkowita w styczniu i marcu')
plt.legend()

plt.grid(axis='x', color='gray', linestyle='-', linewidth=0.5)
plt.xticks([50, 100, 150,  200, 250, 300, 350, 400])
plt.yticks([])

plt.show()
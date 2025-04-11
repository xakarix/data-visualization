import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

np.random.seed(42)

okres = 61
data = pd.date_range(start='2024-05-01', periods=okres)
wartosci = np.random.randn(okres, ).cumsum()
dane = pd.DataFrame({'Wartość' : wartosci, 'Data' : data})
dane.index = dane.Data

fig, ax = plt.subplots(figsize=(12, 6))

dane.plot(y='Wartość', ax=ax)
ax.set_title('Wykres liniowy zmian zjawiska w czasie')
ax.set_xlabel('Data')
ax.set_ylabel('Wartość');

ciecie = 0

ax.axhline(y=ciecie, color = 'red', linestyle = '--', label= f'Linia {ciecie: .2f}');

ax.fill_between(x = dane.index, y1 = dane.Wartość, y2 = ciecie,
                where = dane.Wartość > ciecie, color = 'green', label = 'Wartości dodatnie')
ax.fill_between(x = dane.index, y1 = dane.Wartość, y2 = ciecie,
                where = dane.Wartość < ciecie, color = 'red', label = 'Wartości ujemne')

ax.legend(loc = "lower left")

plt.show()
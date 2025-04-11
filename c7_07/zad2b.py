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

np.random.seed(41)
dane['Inne'] = np.random.randn(okres, ).cumsum()

fig, ax = plt.subplots(figsize=(12, 6))

dane.plot(y=['Wartość', 'Inne'], ax=ax)
ax.set_title('Wykres liniowy zmian zjawiska w czasie')
ax.set_xlabel('Data')
ax.set_ylabel('Wartość');

ax.fill_between(x = dane.index, y1 = dane.Inne, y2 = dane.Wartość,
                where = dane.Wartość > dane.Inne, color = 'green', label = 'Wartości nadwyżka')

ax.fill_between(x = dane.index, y1 = dane.Wartość, y2 = dane.Inne,
                where = dane.Wartość < dane.Inne, color = 'red', label = 'Wartości deficyt')

ax.legend(loc = "lower left")

plt.show()
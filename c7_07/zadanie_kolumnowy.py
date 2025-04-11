import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# Ceny utrzymania nieruchomości (2011)
rok = ['I', 'II','III','IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
y = [205,205.8,206,206.6,205,208,209,210,211,212]

plt.figure(figsize=[8,5])
plt.barh(rok, y , color="royalblue");

plt.show()
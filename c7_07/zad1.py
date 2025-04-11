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

dane.plot(x = "Data", y = "Wartość", color="royalblue", figsize=(12,6));

plt.show()
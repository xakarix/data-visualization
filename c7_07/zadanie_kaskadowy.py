import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# Ceny utrzymania nieruchomości (2011)
rok = ['I', 'II','III','IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
y = [205,205.8,206,206.6,205,208,209,210,211,212]

seria = pd.Series(y)

zmiany = [y[0]] + [y[i] - y[i-1] for i in range(1,len(y))]
# zmiany = seria.diff().fillna(seria[0]).tolist()

fig = go.Figure(go.Waterfall(

    x=rok + ["Bilans"],
    y=zmiany + [0],

    measure= ["absolute"] + ["relative"] * (len(rok)-1) + ['total'] ,
    # measure= ["absolute"] + ["relative"] * (len(rok)-2) ,


    connector={"line":{"color":"rgb(63, 63, 63)", "width": 0.5, "dash":"dot"}},
    increasing={"marker": {"color": "darkorange"}},
    decreasing={"marker": {"color": "darkblue"}},
    totals={"marker": {"color": "skyblue"}}
))

fig.update_layout(
    title="Koszty utrzymania nieruchomości (rok 2011)",
    showlegend=False,
    xaxis_title="Miesiące",
    yaxis_title="Koszty",
    yaxis_ticksuffix = " zł",
    template = 'simple_white'
)

fig.show()
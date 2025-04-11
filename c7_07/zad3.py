import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Bilans sprzedaży
miesiace = ['Start', 'Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Bilans']
sprzedaz = pd.Series([100, 244, 354, 287, 159, 234, 345, 456,0])


zmiany = sprzedaz.diff(-1).fillna(sprzedaz)

fig = go.Figure(go.Waterfall(

    x=miesiace,
    y=zmiany,

    measure= ["absolute"] + ["relative"] * (len(miesiace)-2) + ['total'] ,

    connector={"line":{"color":"rgb(63, 63, 63)", "width": 0.5, "dash":"dot"}},
    increasing={"marker": {"color": "lime"}},
    decreasing={"marker": {"color": "magenta"}},
    totals={"marker": {"color": "skyblue"}}
))

fig.update_layout(
    title="Wykres kaskadowy (z total) – analiza sprzedaży",
    showlegend=False,
    xaxis_title="Miesiące",
    yaxis_title="Spzredaż",
    yaxis_ticksuffix = " zł",
    template = 'simple_white'
)

fig.show()
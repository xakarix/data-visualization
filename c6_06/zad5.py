import numpy as np
import pandas as pd
import plotly.graph_objects as go

x = list(range(1, 101))
y2 = np.log2(x)
y10 = np.log10(x)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y2,
    mode='lines+markers',
    name='log2(x)',
    marker=dict(color='royalblue')
))

fig.add_trace(go.Scatter(
    x=x,
    y=y10,
    mode='lines+markers',
    name='log10(x)',
    marker=dict(color='darkorange')
))

fig.update_layout(
    title = 'Porównanie przekształcanie logarytmicznego przy podstawie 2 i 10',
    xaxis_title = 'x',
    yaxis_title = 'Log',
    template ='plotly_white',
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=True,
        ticks='outside',  
        ticklen=10, 
        linewidth=1,
        linecolor='black',
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=True,
        ticks='outside', 
        ticklen=10,
        linewidth=1,
        linecolor='black',
    ),
)

fig.show()
import pandas as pd
import plotly.graph_objects as go

sprzedaz = pd.DataFrame({
    'Miasto': ['Katowice', 'Kraków', 'Wrocław'],
    'Desktop': [2, 7, 3],
    'Laptop': [12, 7, 13]
})

fig = go.Figure()

fig.add_trace(go.Bar(
    x=sprzedaz['Miasto'],
    y=sprzedaz['Desktop'],
    name='Desktop',
    marker_color='royalblue'
))

fig.add_trace(go.Bar(
    x=sprzedaz['Miasto'],
    y=sprzedaz['Laptop'],
    name='Laptop',
    marker_color = 'darkorange'
))

fig.update_layout(
    title="Rozkład sprzedaży produktów w miastach",
    title_x=0.5,
    xaxis_title="Miasto",
    yaxis_title="Sprzedaż",
    barmode='group',
    template='plotly_white',
    xaxis_tickangle = 0,
    yaxis_tickformat = '0.f',
    yaxis_ticksuffix='k'
)

fig.show()
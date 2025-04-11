import pandas as pd
import plotly.graph_objects as go

sprzedaz = pd.DataFrame({
    'Miasto': ['Katowice', 'Kraków', 'Wrocław'],
    'Desktop': [2, 7, 3],
    'Laptop': [12, 7, 13]
})

fig = go.Figure()

# Słupki Desktop
fig.add_trace(go.Bar(
    x=sprzedaz['Miasto'],
    y=sprzedaz['Desktop'],
    name='Desktop',
    marker_color=['#A8D5BA','#A8D5BA','#A8D5BA']
))

# Słupki Laptop
fig.add_trace(go.Bar(
    x=sprzedaz['Miasto'],
    y=sprzedaz['Laptop'],
    name='Laptop',
    marker_color=['#A9C7E8', '#A9C7E8', '#A9C7E8']
))

fig.update_layout(
    title="Rozkład sprzedaży produktów w miastach",
    title_x = 0.5,
    legend_title_text="Produkty",
    xaxis_title="Miasto",
    yaxis_title="Sprzedaż",
    yaxis_ticksuffix='k',
    barmode = 'group',
    template='plotly_white', 
    xaxis_tickangle=0, 
)

fig.show()

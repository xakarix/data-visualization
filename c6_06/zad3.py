import pandas as pd
import plotly.graph_objects as go

sprzedaz_dl = pd.DataFrame({
    'Miasto': ['Katowice', 'Kraków', 'Wrocław'] * 2,
    'Produkty': ['Monitor21'] * 3 + ['Monitor24'] * 3,
    'Sprzedaż': [2, 7, 3, 12, 7, 13]
})

fig = go.Figure()

miasta = sprzedaz_dl['Miasto'].unique()

kolory = {
    'Katowice': 'royalblue',
    'Kraków': 'darkorange',
    'Wrocław': 'green'
}

for miasto in miasta:
    df_miasto = sprzedaz_dl[sprzedaz_dl['Miasto'] == miasto]
    fig.add_trace(go.Bar(
        x=df_miasto['Produkty'],
        y=df_miasto['Sprzedaż'],
        name=miasto,
        marker_color=kolory[miasto]
    ))

fig.update_layout(
    barmode='stack',
    title = 'Rozkład sprzedaży produktów w miastach',
    title_x=0.5,
    xaxis_title = 'Produkt',
    yaxis_title = 'Sprzedaż',
    template = 'plotly_white'
)

fig.show()
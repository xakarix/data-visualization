import pandas as pd
import plotly.graph_objects as go

sprzedaz_dl = pd.DataFrame({
    'Miasto': ['Katowice', 'Kraków', 'Wrocław'] * 2,
    'Produkty': ['Desktop'] * 3 + ['Laptop'] * 3,
    'Sprzedaż': [2, 7, 3, 12, 7, 13]
})

sprzedaz_dl['Procent'] = sprzedaz_dl.groupby('Produkty')['Sprzedaż'].transform(lambda x: (x/x.sum()) * 100)

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
        x=df_miasto['Procent'],
        y=df_miasto['Produkty'],
        name=miasto,
        orientation='h',
        marker_color=kolory[miasto]
    ))

fig.update_layout(
    barmode='stack',
    title = 'Rozkład sprzedaży produktów w miastach',
    title_x=0.5,
    xaxis=dict(
        title='Procent sprzedaży (%)',
        tickvals=[0, 50, 100],
        ticktext=['0%', '50%', '100%'],
        range=[0, 100]
    ),
    yaxis_title = 'Sprzedaż',
    template = 'plotly_white'
)

fig.show()
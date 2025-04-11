import plotly.express as px
import pandas as pd

gap = px.data.gapminder()
gap_2007 = gap[gap['year'] == 2007]

fig = px.scatter(
    gap_2007,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    facet_col="continent",
    facet_col_wrap=2,
    hover_name="country",
    size_max=60,
    log_x=True,
    labels={
        "gdpPercap": "PKB per capita (log)",
        "lifeExp": "Długość życia",
        "continent": "Region"
    },
    title="Zależność oczekiwanej długości życia od PKB per capita w poszczególnych regionach świata"
)

fig.update_layout(title_font_size=20)
fig.show()

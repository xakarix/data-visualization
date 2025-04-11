import plotly.express as px
import pandas as pd

# Wczytanie danych
gap = px.data.gapminder()

# Filtracja danych - tylko Europa, rok 2007
data = gap[(gap['year'] == 2007) & (gap['continent'] == 'Europe')]

# Oczekiwana długość życia w Polsce
poland_life_expectancy = data[data['country'] == 'Poland']['lifeExp'].values[0]

# Dodanie kolumny do kolorowania: "higher", "poland", "lower"
def categorize(row):
    if row['lifeExp'] > poland_life_expectancy:
        return 'higher'
    elif row['country'] == 'Poland':
        return 'poland'
    else:
        return 'lower'

data['category'] = data.apply(categorize, axis=1)

# Tworzenie wykresu
fig = px.bar(data,
             y="country",  # Nazwa kraju na osi Y
             x="lifeExp",  # Oczekiwana długość życia na osi X
             color="category",  # Kolorowanie w zależności od kategorii
             color_discrete_map={"higher": "green", "poland": "red", "lower": "lightcoral"},
             labels={"lifeExp": "Oczekiwana długość życia", "country": "Kraj"},
             title="Oczekiwana długość życia w krajach europejskich (2007)")

# Ustawienia wykresu
fig.update_layout(
    height=600,  # Wysokość wykresu
    xaxis_title="Oczekiwana długość życia",  # Tytuł osi X
    yaxis_title="Kraj",  # Tytuł osi Y
    yaxis=dict(categoryorder='total ascending'),  # Sortowanie krajów od dołu w górę
)

# Dostosowanie ticków osi X do wartości 0, 40, 80
fig.update_xaxes(
    tickvals=[0, 40, 80],
    ticktext=["0", "40", "80"]
)

# Pokaż wykres
fig.show()

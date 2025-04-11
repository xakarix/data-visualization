import pandas as pd
import plotly.express as px

quiz = pd.DataFrame({'Odpowiedź' : ['Tak','Nie'],
                     'Wartość' : [4532,2497]})

fig = px.pie(quiz, names='Odpowiedź', values='Wartość', color_discrete_sequence=['green', 'red'])
fig.update_traces(textinfo='label', textposition='inside', pull=[0.01, 0],textfont=dict(size=20))
fig.show()
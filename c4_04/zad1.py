import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dane = pd.DataFrame({
    'Miesiąc': ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze", "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"],
    'SmartTV': [159, 187, 245, 151, 181, 160, 142, 217, 152, 143, 157, 175],
    'TV': [159, 187, 246, 151, 181, 150, 134, 149, 131, 105, 129, 142]
})

split = 4  # maj, rozdziela linie
fig, ax = plt.subplots(figsize=[9, 5])

#Prawo kontynuacji: wzrok uzytkowanika jest prowadzony poprzed zmianę koloru linii
#Prawo podobienstwa: kolory linni nie roznia sie, zachowane zostaly w jednej tonacji
#gray lines
ax.plot(dane['Miesiąc'][:split + 1], dane['SmartTV'][:split + 1], color='lightgray', linestyle='-')
ax.plot(dane['Miesiąc'][:split + 1], dane['TV'][:split + 1], color='lightgray', linestyle='-')

# darkblue lines
ax.plot(dane['Miesiąc'][split:], dane['SmartTV'][split:], color='navy', linestyle='-')
ax.plot(dane['Miesiąc'][split:], dane['TV'][split:], color='navy', linestyle='-')

# prawo domykania: wyzaczenie punktow na koncu linii
ax.scatter(dane['Miesiąc'].iloc[-1], dane['SmartTV'].iloc[-1], color='navy')
ax.scatter(dane['Miesiąc'].iloc[-1], dane['TV'].iloc[-1], color='navy')

# FactorInk: usuniecie zbedych krawędzi i siatek
titlesize = 14
ax.spines['top'].set_visible(False)  
# ax.spines['left'].set_visible(False)  
ax.spines['right'].set_visible(False)  
ax.yaxis.set_ticks_position('none') 

#Prawo kontynuacji: uzytkownik nie musi przenosic wzroku, by odczytac o czym informuja go dane
ax.text(len(dane) - 1, dane['SmartTV'].iloc[-1] + 5, 'SmartTV', color='navy', fontsize=12)
ax.text(len(dane) - 1, dane['TV'].iloc[-1] + 5, 'TV', color='navy', fontsize=12)

plt.title("Sprzedaż telewizorów w 2016", fontsize=titlesize)
ax.set_xticks(range(len(dane)))
ax.set_xticklabels(dane["Miesiąc"], fontsize=10)

plt.show()
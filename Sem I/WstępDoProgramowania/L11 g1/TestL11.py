import random

# Wygeneruj dane dotyczące liczby ludności w Polsce
lata = list(range(1950, 2023))
liczba_ludnosci = [random.randint(20000000, 40000000) for _ in range(len(lata))]

# Zapisz dane do pliku CSV
with open('dane.csv', 'w') as f:
    f.write('rok,liczba_ludnosci\n')
    for i in range(len(lata)):
        f.write(f'{lata[i]},{liczba_ludnosci[i]}\n')

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Wczytaj dane z pliku CSV
data = pd.read_csv('dane.csv')

# Utwórz podwykres
fig, ax = plt.subplots()

# Funkcja, która będzie wywoływana w każdej klatce animacji
def animate(i):
    # Wybierz dane z kolejnego okresu
    subset = data[data['rok'] == i]
    
    # Wyświetl wykres słupkowy
    ax.bar(subset['rok'], subset['liczba_ludnosci'])
    # Ustaw tytuł wykresu
    ax.set_title(f'Liczba ludności w Polsce w {i} roku')

# Utwórz animację
ani = animation.FuncAnimation(fig, animate, frames=data['rok'].unique(), interval=500)

# Wyświetl animację
plt.show()


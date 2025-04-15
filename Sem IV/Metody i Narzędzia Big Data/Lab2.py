import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bisect
def zad2():
    tablica = np.arange(1, 11)
    print("Tablica:", tablica)
    maks = np.max(tablica)
    min_ = np.min(tablica)
    print("Maksymalna wartość:", maks)
    print("Minimalna wartość:", min_)
    srednia = np.mean(tablica)
    odchylenie = np.std(tablica)
    print("Średnia:", srednia)
    print("Odchylenie standardowe:", odchylenie)

def zad3():
    tablica = np.arange(12).reshape(3, 4)
    print("Tablica:\n", tablica)
    element = tablica[1, 2]
    print("Element o indeksie (1, 2):", element)
    podtablica = tablica[:2, -2:]
    print("Podtablica:\n", podtablica)

def zad4():
    tablica = np.arange(10)
    print("Tablica:\n", tablica)
    tablica = tablica.reshape(2, 5)
    print("Tablica po zmianie kształtu:\n", tablica)
    tablica_transponowana = tablica.T
    print("Tablica transponowana:\n", tablica_transponowana)
    print("Kształt tablicy transponowanej:", tablica_transponowana.shape)

def zad5():
    tablica1 = np.arange(6).reshape(2, 3)
    tablica2 = np.arange(6, 12).reshape(2, 3)
    print("Tablica 1:\n", tablica1)
    print("Tablica 2:\n", tablica2)
    suma = tablica1 + tablica2
    print("Suma:\n", suma)
    iloczyn = tablica1 * 2
    print("Iloczyn:\n", iloczyn)

def zad6():
    tablica = np.arange(9).reshape(3, 3)
    print("Tablica:\n", tablica)
    wiersz = np.array([1, 2, 3])
    tablica += wiersz
    print("Tablica po dodaniu wiersza:\n", tablica)
    kolumna = np.array([1, 2, 3]).reshape(3, 1)
    tablica *= kolumna
    print("Tablica po pomnożeniu przez kolumnę:\n", tablica)

def zad7():
    tablica = np.random.rand(100)
    print("Tablica:\n", tablica)
    suma = np.sum(tablica)
    print("Suma:", suma)
    srednia = np.mean(tablica)
    print("Średnia:", srednia)
    odchylenie = np.std(tablica)
    print("Odchylenie standardowe:", odchylenie)
    skumulowana_suma = np.cumsum(tablica)
    print("Skumulowana suma:\n", skumulowana_suma)
    skumulowany_iloczyn = np.cumprod(tablica)
    print("Skumulowany iloczyn:\n", skumulowany_iloczyn)

def zad8():
    tablica = np.random.randint(0, 100, 10)
    print("Tablica:\n", tablica)
    posortowana_tablica = np.sort(tablica)
    print("Posortowana tablica:\n", posortowana_tablica)
    indeks = bisect.bisect_left(posortowana_tablica, 50)
    print("Indeks liczby 50 w posortowanej tablicy:", indeks)
    
data = {'Imię': ['Jan', 'Anna', 'Piotr','Anna', 'Marek'],
        'Nazwisko': ['Kowalski', 'Nowak', 'Zieliński','Nowak',np.NaN],
        'Wiek': [25, 31, 42,31, np.NaN]}
df = pd.DataFrame(data)

# Zapisywanie do pliku CSV
df.to_csv('p.csv', index=False)

def zad9():
    dane = pd.read_csv('p.csv')
    print("Wymiary danych:", dane.shape)
    print("Przykdladowe wiersze:\n", dane.head())

def zad10():
    dane = pd.read_csv('p.csv')
    wybrane_kolumny = dane[['Imię','Nazwisko']]
    print("Kolumny:\n", wybrane_kolumny)
    warunek = dane['Imię'] == 'Jan'
    print("Filtrowanie warunkowe:\n", dane[warunek])
    wybrane_wiersze = dane.loc[warunek, ['Nazwisko', 'Wiek']]
    print("Wiersze na podstawie kryterium:\n", wybrane_wiersze)

def zad11():
    dane = pd.read_csv('p.csv')
    print("Liczba brakujących wartości w danych:\n", dane.isnull().sum())
    dane = dane.dropna()
    print("Dane po usunięciu brakujących wartości:\n", dane)
    dane = dane.drop_duplicates()
    print("Dane po usunięciu duplikatów:\n", dane)
    dane['Wiek'] = pd.to_numeric(dane['Wiek'])
    print("Dane po konwersji kolumny:\n", dane)

def zad12():
    dane = pd.read_csv('car_price_dataset.csv')
    grupowane_dane = dane.groupby('Brand')
    print("Grupowane dane suma (nie ma sensu):\n", grupowane_dane.sum())
    print("Średnia wartość Ceny dla każdej grupy:\n", grupowane_dane['Price'].mean().round(2))
    print("Liczba wierszy w każdej grupie:\n", grupowane_dane.size())
    print(grupowane_dane.agg({'Price' : 'mean','Owner_Count' : 'mean'}))

def zad13():
    dane = pd.read_csv('car_price_dataset.csv')
    dane['Brand and Model'] = dane['Brand'] + dane['Model']
    print("Dane z nową kolumną:\n", dane['Brand and Model'])
    dane['Price^2'] = dane['Price'].apply(lambda x: x**2)
    print("Dane po zastosowaniu funkcji:\n", dane)
    dane['Brand'] = dane['Brand'].str.upper()
    print("Dane po zastosowaniu funkcji na kolumnie tekstowej:\n", dane)

def zad14():
    dane = pd.read_csv('car_price_dataset.csv')
    df = dane.groupby("Brand")
    d = df['Price'].mean().round(2)
    plt.figure(figsize=(12, 8))
    plt.bar(dane['Brand'].unique(), d)
    
    plt.xlabel('Brand')
    plt.ylabel('Price')
    plt.title('Średnia cena marki')
    
    plt.show()
    plt.figure(figsize=(12, 8))
    plt.scatter(dane['Mileage'], dane['Price'])
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('stosunek ceny do ')
    plt.show()

def zad16():
    x = np.arange(10)
    y = np.random.rand(10)
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Wykres liniowy')
    plt.show()

def zad17():
    x = np.random.rand(10)
    y = np.random.rand(10)
    plt.scatter(x, y, color = 'g')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Wykres punktowy')
    plt.show()

def zad18():
    kategorie = ['A', 'B', 'C', 'D']
    wartosci = [10, 20, 30, 40]
    plt.bar(kategorie, wartosci,color='g')
    plt.xlabel('Kategorie')
    plt.ylabel('Wartości')
    plt.title('Wykres słupkowy')
    plt.show()
    

def zad19():
    dane = np.random.randn(1000)
    plt.hist(dane, bins=30, alpha=0.7, color='g',edgecolor = 'black')
    plt.xlabel('Wartość')
    plt.ylabel('Częstotliwość')
    plt.title('Histogram danych')
    plt.show()

def zad20():
    etykiety = ['Kategoria A', 'Kategoria B', 'Kategoria C']
    wartosci = [25, 35, 40]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    plt.pie(wartosci, labels=etykiety, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Wykres kołowy kategorii')
    plt.show()

def zad21():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(2*x)
    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    axs[0, 0].plot(x, y1)
    axs[0, 0].set_title('Wykres liniowy')
    axs[0, 1].scatter(x, y2)
    axs[0, 1].set_title('Wykres punktowy')
    axs[1, 0].plot(x, y3)
    axs[1, 0].set_title('Wykres liniowy 2')
    axs[1, 1].hist(y1, bins=30)
    axs[1, 1].set_title('Histogram')
    plt.tight_layout()
    plt.show()


def zad22():
    dane = pd.read_csv('car_price_dataset.csv')
    brands = dane['Brand'].unique()
    x = dane['Year'].unique()
    print(dane.groupby(['Brand','Year'])['Price'].mean().round(2)['Audi'])
    plt.figure(figsize=(12, 8))
    for brand in brands:
        y = dane.groupby(['Brand','Year'])['Price'].mean().round(2)[brand]
        plt.scatter(x, y, label=brand)
    plt.title('Wykres liniowy')
    plt.legend()
    plt.show()
    

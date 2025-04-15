import numpy as np
# Zadanie 1.

# a)

# Odległość Hamminga jest stosowana dla dwóch ciągów znaków o równej długości. Liczy się ją na podstawie ilośći róznych znaków

def calculate_distance(base_string, another_string):
    
    # A jest rózne od a, więc zamieniamy wszystkie znaki na duze litery
    base_string = base_string.upper()
    another_string = another_string.upper()
    
    # Jezeli ktoś jest głupi i wprowadzi ciągi znaków o róznej długości, to funkcja zwróci tekst. Nie ma tego w zadaniu, ale to zawarłem
    
    if len(base_string) != len(another_string):     
        return "Strings have diffrent lenghts"
        
    else:
        
        # Dla znaków na poszczególnych pozycjach sprawdzane jest czy są takie same. Jezeli nie, to dystans zwiększany jest o 1
        # Np. Sprawdzane jest dla słów "sowa" i "kawa" s != k, więc distance +=1
        
        distance = 0
        for i in range(len(base_string)):           
            if base_string[i] != another_string[i]:
                distance +=1
        return distance     # Program zwraca odległość Hamminga
    
# print(calculate_distance("aabbcc","aabcvb"))

# b)

# Program działa tak samo, tylko sprawdza odległość na klawiaturze na podstawie macierzy


def calculate_distance_with_multipliers(base_string, another_string):
    
    # Deklaryjemy macierz z literami z klawiatury
    
    keyboard = np.array([ 
      ["Q","W","E","R","T","Y","U","I","O","P"],
      ["A",'S','D','F','G','H','J','K','L',''],
      ['Z','X','C','V','B','N','M','','','']    
    ])
    
    
    if len(base_string) != len(another_string):
        return "Strings have diffrent lenghts"
    
    
    
    else:
        distance = 0
        for i in range(len(base_string)):
            if base_string[i] != another_string[i]:
                
                
                bs_index = np.where(keyboard == base_string[i].upper())     # Funkcja, która wyszukuje indeks w macierzy 
                bs_index = (bs_index[0][0],bs_index[1][0])      # Wydobycie z wartosci jaką zwraca funkcja idneksu i umieszcenie go w krotce
                
                
                is_close = False
                
                # Przeszukujmy dla litery wszystkie mozliwe pola obok, by zwrócić dystans +1, jezeli nie znajdziemy takiej, to dystans ma wartość +2
                
                for indexY in range(bs_index[0]-1,bs_index[0]+2):
                    for indexX in range(bs_index[1]-1,bs_index[1]+2):
                        try:    # W przypadku nieistniejących indeksów macierzy (np. [-1,0]) po prostu ich nie sprawdzamy 
                            if keyboard[indexY,indexX] == another_string[i].upper():
                                is_close = True
                        except Exception:
                            pass
                
                if is_close:
                    distance +=1
                else: distance +=2
                
                
        return distance
    
print(calculate_distance_with_multipliers("s","c"))

# c)

dictionary = [
    "telefon", "motor", "klawiatura", "kamera", "komputer", "internet", "program", "ekran", "strona", "dysk",
"klikanie", "folwark", "sklepik", "kod", "grafika", "formatowanie", "ramka", "stacja", "wirus", "auto", "serwer",
"hasło", "login", "system", "klucz", "backup", "folder", "zasilacz", "procesor", "port", "Polska",
"stylus", "router", "adres", "mail", "folderek", "drukarka", "skaner", "sterownik", "aplikacja", "spacja",
"antena", "smartfon", "aparat", "platforma", "fotografia", "monitor", "plik", "lupa", "kompilator", "obraz",
"połączenie", "serwis", "antywirus", "pop-up", "browser", "rejestr", "ciastko", "klik", "transfer", "oko",
"gitara", "studio", "mikrofon", "słuchawki", "notebook", "tablet", "konsola", "kontakt", "kalendarz", "sklep",
"programista", "test", "projekt", "edycja", "licencja", "upał", "analog", "cyfrowy", "model", "prototyp",
"numer", "kodowanie", "klasa", "tekst", "interfejs", "wydruk", "obliczenia", "import", "eksport", "łącz",
"zestaw", "baza", "format", "link", "atlas", "prezentacja", "info", "instrukcja", "monitoring", "analogia"
]


def get_similar(word):
    if word in dictionary:
        return "OK"
    else:
        
        # Przesiewamy słownik zostawiając tylko słowa o takiej samej długości jak wprowadzony ciąg znaków
        
        similar_dictionary = []
        for i in range(len(dictionary)):
            if len(word) == len(dictionary[i]):
                similar_dictionary.append(dictionary[i])
                
        # Znajdujemy najbardziej podobne słowo za pomocą odległości Hamminga
        
        similar = similar_dictionary[0]   
        for i in range(len(similar_dictionary)):
            if calculate_distance(word,similar) > calculate_distance(word,similar_dictionary[i]):
                similar = similar_dictionary[i]
        return similar
    
word = "gracz"
similar_words = []

# Wyszukujemy najbardziej podobne słowo trzy razy 
for i in range(3):
    try:
        similar_words.append(get_similar(word))
        if get_similar(word) == "OK":
            break  
        else:
            dictionary.remove(get_similar(word))
    except Exception:
        break
   
       
# print(similar_words)

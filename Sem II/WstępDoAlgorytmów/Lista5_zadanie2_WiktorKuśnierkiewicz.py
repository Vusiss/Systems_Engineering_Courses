import numpy as np

# a)

# Otwieramy plik z danymi z wikipedii, a następnie usuwamy z końca kazdej komórki znak procentu, by móc zamienić typ danych na float

frequency_of_letters_in_languagues = np.loadtxt(open("/Users/vusis/Documents/Program/WstępDoAlgorytmów/LetterFrequency.csv", "rb"), delimiter=";", dtype=str)
for i in range(len(frequency_of_letters_in_languagues)):
    for j in range(3):
        frequency_of_letters_in_languagues[i,j] = frequency_of_letters_in_languagues[i,j][:-1]
frequency_of_letters_in_languagues = frequency_of_letters_in_languagues.astype(float)       


# b)



text = "In a quaint village nestled between rolling hills, lived a woman named Emily. She had a garden filled with vibrant flowers of every hue, creating a breathtaking display of colors. Each morning, she would stroll through the garden, inhaling the sweet scent of blooming roses and listening to the chirping of birds overhead. One day, Emily decided to embark on a journey to the nearby mountains, drawn by the allure of their majestic peaks. As she hiked higher, the air became crisper, and panoramic views unfolded before her. The mountains whispered tales of ancient times, and Emily felt a profound connection to the natural world around her. Her expedition became a source of inspiration for the villagers, who marveled at the stories she brought back from the mountains."
special_characters = [".",",","'",";",":","?","!","(",")"," ",'"']
languages = ["english","german","polish"]

# Funkcja usuwa znaki specjalne i spacje oraz zmienia wszystkie litery na duze
def prepare_text(text): 
    for i in special_characters:
        text = text.replace(i,"")
        
    text = text.upper()
    return text

text = prepare_text(text)

# Funkcja w tablicy jednowymiarowej zlicza częstotliwośc pojawiania się kadzego znaku. (A znajduje się na indeksie 0, B na 1, C na 2, itd.) 
def get_frequency(text):
    frequency_in_text = np.zeros((26,1))

    for i in text:
        if ord(i)-65<26: frequency_in_text[ord(i)-65] += 1  # Ignorujemy litery ą, ę itp., dlatego mamy "if ord(i)-65<26"
    frequency_in_text = (frequency_in_text/len(text))*100   # Zamieniamy wartości zliczonych liczb na procentowe występowanie
    frequency_in_text= np.round(frequency_in_text,3)
    return frequency_in_text

frequency_from_text = get_frequency(text)

# Funkcja sprawdza jaki język jest najbardziej podobny poprzez zsumowanie rónic w procentowym występowaniu liter. Wprowadzane są dwie zmienne "frequency_in_text", która wprowadza częstotliwośc liter w tekście, "frequency", która oznacza częstotliwość liter w językach. Mozna potem uzyć tej funkcji przy sprawdzaniu częstotliwości głosek.

def get_similar_language(frequency_in_text, frequency):
    difference = [0,0,0]
    for i in range(len(frequency_in_text)):
        for j in range(3):
            difference[j] += (abs(frequency_in_text[i]- frequency[i,j]))[0] # Sprawdź co robi to zero

    low = difference[0]
    index_low = 0

    for index, element in enumerate(difference):
        if element < low:
            low = element
            index_low = index
    
    return languages[index_low]  
        


print("Used language:",get_similar_language(frequency_from_text, frequency_of_letters_in_languagues))

# c)

# Funkcja zamienia tablicę z częstotliwością liter na tablicę z czestotliwością samogłosek i spółgłosek. Zwyczajnie dodawane są wartości procentowe samogłosek, a pozostały procent to spółgłoski.

def get_sounds(frequency):
    vowels = frequency[0] + frequency[4] + frequency[8] + frequency[14] + frequency[20] + frequency[24]
    consonants = np.array([round(100-vowels[i],3) for i in range(len(frequency[0]))])   # To wygląda dziwnie, ale to jest uogólnienie, by tworzyć tabele równiez dla wielu języków (print w linijce 80 pomaga zrozumieć o co chodzi)
    sounds = np.vstack((vowels,consonants))
    return sounds

frequency_of_sounds = get_sounds(frequency_from_text)
frequency_of_sounds_in_languages = get_sounds(frequency_of_letters_in_languagues)

print(frequency_of_sounds,frequency_of_sounds_in_languages)

print("Language with similar sounds:",get_similar_language(frequency_of_sounds,frequency_of_sounds_in_languages))
import json
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def read_config(file_path):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
        return config 

def read_data(file_path):
    arkusz = 'TABLICA'
    wb = openpyxl.load_workbook(file_path)
    data = wb[arkusz]
    return data

def plot_graph(data, config):
    
    # Deklaracja wszystkich list
    Kod = []
    Nazwa = []
    ŚU = []
    NPKB = []
    NA1 = []
    UN = []
    Etykiety = [ŚU, NPKB, NA1, UN]
    EtykietyNazwy = ['ŚU', 'NPKB', 'NA1', 'UN']
    kody_obszaru = config['kody obszaru']
    lata = config['lata']
    wskaźniki = config['wskaźniki']
    
    # Uzupełnienie list danymi
    for cell in data["A"][3:]:
        Kod.append([cell.value,cell.row])
    for kod_ in Kod:
        if kod_[0] in kody_obszaru:
            Nazwa.append(data["B"][kod_[1]-1].value)
    for i in wskaźniki:
        for kod_ in Kod:
            if kod_[0] in kody_obszaru:
                numbers = []
                for rok in lata:
                    column = chr(int(rok) - 1951 + (int(i)-1)*5)
                    numbers.append(data[column][kod_[1]-1].value)
                Etykiety[i-1].append(numbers)
    
    # Wygenerownie wykresów dla wybranych wskaźników
    for j in wskaźniki:
        f, ax = plt.subplots()
        width = 0.25
        x = np.arange(len(lata))
        
        lenNazwa = []
        for i in range(len(Nazwa)):lenNazwa.append(i)
        
        ax.set_xticks(x + width / 2)
        ax.set_xticklabels(lata)
        title = EtykietyNazwy[j-1]
        plt.title(title)
        
        def anim(i):
            ax.bar(x + i*width, Etykiety[j-1][i],width, label=Nazwa[i])
            ax.legend()    
        
        ani = animation.FuncAnimation(f, anim,frames=lenNazwa, interval=500, repeat=False)
            
        plt.show()
        
     
config_file_path = '/Users/vusis/Documents/Program/WstępDoProgramowania/L11 g1/konf.json'
data_file_path = '/Users/vusis/Documents/Program/WstępDoProgramowania/L11 g1/dane_g1.xlsx'

config = read_config(config_file_path)
data = read_data(data_file_path)

plot_graph(data, config)
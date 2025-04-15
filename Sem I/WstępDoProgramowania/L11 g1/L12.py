import json
import copy
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import ttk

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
    lata = [2018, 2019, 2020, 2021, 2022]
    
    for cell in data["A"][3:]:
        Kod.append([cell.value,cell.row])
    for kod_ in Kod:
        Nazwa.append([data["B"][kod_[1]-1].value,kod_[1]-1])
    
    
    
    root = tk.Tk()
    root.title("Konfiguracja wykresów")
    # root.geometry("800x800")
    
    
    
    # Kontrolki konfiguracyjne
        
    labelE = []
    entryE = []
    labelN = []
    entryN = []
    labelL = []
    entryL = []
    def graf(i,j):
        if i == 1:
            wskaźniki.append(j+1)
        if i == 3:
            kody_obszaru.append(Nazwa[j])
        if i == 5:
            lata_kopia.append(lata[j])
            
    kody_obszaru = []
    lata_kopia = []
    wskaźniki = []
    
    
    for j in range(len(EtykietyNazwy)):
        E = tk.Label(root, text=EtykietyNazwy[j]).grid(row=0, column=j)
        EE = tk.Checkbutton(root, command = graf(1,j)).grid(row=1, column=j)
    for j in range(len(Nazwa)):
        N = tk.Label(root, text=Nazwa[j][0]).grid(row=2, column=j)
        NN = tk.Checkbutton(root,command = graf(3,j)).grid(row=3, column=j)    
    for j in range(len(lata)):
        L = tk.Label(root, text=lata[j]).grid(row=4, column=j)
        LL = tk.Checkbutton(root, command = graf(5,j)).grid(row=5, column=j)
    
    
    
    
    # button = tk.Button(root, text="Generuj wykres") #command=generate_graph)
    # button.grid(column = 3, row = 9)
    
    # root.mainloop()
    

    
    # print(wskaźniki,lata,Nazwa)
    
    
    # kody_obszaru = config['kody obszaru']
    # lata = config['lata']
    # wskaźniki = config['wskaźniki']
    
    # Uzupełnienie list danymi
    
        
        
        
        
    # for kod_ in Kod:
    #     if kod_[0] in kody_obszaru:
    #         Nazwa.append(data["B"][kod_[1]-1].value)
            
            
    # for i in wskaźniki:
    #     for kod_ in Kod:
    #         if kod_[0] in kody_obszaru:
    #             numbers = []
    #             for rok in lata:
    #                 column = chr(int(rok) - 1951 + (int(i)-1)*5)
    #                 numbers.append(data[column][kod_[1]-1].value)
    #             Etykiety[i-1].append(numbers)
    
    # Tworzenie interfejsu użytkownika
    def generate_graph():
        
        print(Nazwa)
        
        for i in Nazwa:
            if i[0] not in kody_obszaru:
                Nazwa.pop(Nazwa.index(i))
        for i in lata:
            if i not in lata_kopia:
                lata.pop(lata.index(i))    
        
        for i in wskaźniki:
            for kod_ in Nazwa:
                if kod_[0] in kody_obszaru:
                    numbers = []
                    for rok in lata:
                        column = chr(int(rok) - 1951 + (int(i)-1)*5)
                        numbers.append(data[column][kod_[1]-1].value)
                    Etykiety[i-1].append(numbers)
        
        print(Nazwa, wskaźniki, lata)
        
        
        
        
        
        
        
        
        
        
        
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

            def anim(g):
                ax.bar(x + g*width, Etykiety[j-1][i],width, label=Nazwa[i][0])
                ax.legend()    

            ani = animation.FuncAnimation(f, anim,frames=lenNazwa, interval=500, repeat=False)

            plt.show()
    
    # root = tk.Tk()
    # root.title("Konfiguracja wykresów")
    # root.geometry("400x400")
    
    # # Kontrolki konfiguracyjne
    # for i in wskaźniki:
    #     label = tk.Label(root, text=EtykietyNazwy[i-1])
    #     label.pack()
    #     for rok in lata:
    #         var = tk.StringVar(value="1")
    #         entry = tk.Entry(root, textvariable=var)
    #         entry.pack()
    button = tk.Button(root, text="Generuj wykres", command=generate_graph)
    button.grid(column = 3, row = 9)
    
    root.mainloop()
    


config_file_path = '/Users/vusis/Documents/Program/WstępDoProgramowania/L11 g1/konf.json'
data_file_path = '/Users/vusis/Documents/Program/WstępDoProgramowania/L11 g1/dane_g1.xlsx'

config = read_config(config_file_path)
data = read_data(data_file_path)

plot_graph(data, config)

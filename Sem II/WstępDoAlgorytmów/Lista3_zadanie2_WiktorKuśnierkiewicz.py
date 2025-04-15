from Lista3_classes_WiktorKuśnierkiewicz import Urząd,Czas_na_wykonanie_zadań
import random as r
import matplotlib.pyplot as plt


typy_urzędów = [[3, 3, 3],[2, 2, 2, 3],[1, 2, 3, 1]]
ilość_cykli = 1000

def Działanie_urzędów():
    czasy = [0,0,0]
    
    for typ in typy_urzędów:
        x = [ i for i in range(ilość_cykli) ]
        y = []
        
        
        for cykl in range(ilość_cykli):
            
            klienci = [
                        (klient := r.choice(["A","B","C"]), 
                        (int(ord(klient)) - 65)*4 + r.randint(1,4)) 
                        for i in range(30)
                        ]
            
            urząd = Urząd(typ)
            czas = Czas_na_wykonanie_zadań(urząd,klienci)[0]
            czasy[typy_urzędów.index(typ)] += czas
            y.append(czas)
        
        plt.subplot(1, 3, typy_urzędów.index(typ)+1)
        plt.bar(x,y)
        plt.xlabel("Kolejka")
        plt.ylabel('Czas obsługi')
        plt.ylim(0, 70)
        
    return czasy

def Działanie_urzędów_rosnąco():
    czasy = [0,0,0]
    
    for typ in typy_urzędów:
        x = [ i for i in range(ilość_cykli) ]
        y = []
        
        
        for cykl in range(ilość_cykli):
            
            
            klienci = [
                        (klient := r.choice(["A","B","C"]), 
                        (int(ord(klient)) - 65)*4 + r.randint(1,4)) 
                        for i in range(30)
                        ]
            
            klienci = sorted(klienci, key=lambda x: x[1])
            
            urząd = Urząd(typ)
            czas = Czas_na_wykonanie_zadań(urząd,klienci)[0]
            czasy[typy_urzędów.index(typ)] += czas
            y.append(czas)
        
        plt.subplot(1, 3, typy_urzędów.index(typ)+1)
        plt.bar(x,y)
        plt.xlabel("Kolejka")
        plt.ylabel('Czas obsługi')
        plt.ylim(0, 70)
        
    return czasy

def Działanie_urzędów_malejąco():
    czasy = [0,0,0]
    
    for typ in typy_urzędów:
        x = [ i for i in range(ilość_cykli) ]
        y = []
        
        
        for cykl in range(ilość_cykli):
            
            
            klienci = [
                        (klient := r.choice(["A","B","C"]), 
                        (int(ord(klient)) - 65)*4 + r.randint(1,4)) 
                        for i in range(30)
                        ]
            
            klienci = sorted(klienci, key=lambda x: x[1])
            klienci.reverse()
            
            urząd = Urząd(typ)
            czas = Czas_na_wykonanie_zadań(urząd,klienci)[0]
            czasy[typy_urzędów.index(typ)] += czas
            y.append(czas)
        
        plt.subplot(1, 3, typy_urzędów.index(typ)+1)
        plt.bar(x,y)
        plt.xlabel("Kolejka")
        plt.ylabel('Czas obsługi')
        plt.ylim(0, 70)

    return czasy

def Wyświetl_wykres():
    
        
    plt.tight_layout()    
    plt.show()    

def Wyświetl_czas(czasy):
    
    for i in range(3):
        czasy[i] /= ilość_cykli
    print(czasy)



Wyświetl_czas(Działanie_urzędów())

Wyświetl_czas(Działanie_urzędów_rosnąco())

Wyświetl_czas(Działanie_urzędów_malejąco())

Wyświetl_wykres()

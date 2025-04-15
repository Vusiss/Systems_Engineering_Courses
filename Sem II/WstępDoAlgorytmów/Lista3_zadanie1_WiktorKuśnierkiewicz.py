from Lista3_classes_WiktorKuśnierkiewicz import Urząd,Czas_na_wykonanie_zadań
import random as r

klienci = [
    (klient := r.choice(["A","B","C"]), 
    (int(ord(klient)) - 65)*4 + r.randint(1,4)) 
    for i in range(40)
    ]

liczba_okien_kazdego_typu = [3, 3, 3, 1]    # [A,B,C,E]

urząd1 = Urząd(liczba_okien_kazdego_typu)

czas,obsłuzeni = Czas_na_wykonanie_zadań(urząd1,klienci)


print("Czas trwania obsługi:",czas,"\nIlość klientów dla poszczególnych okienek:", obsłuzeni)

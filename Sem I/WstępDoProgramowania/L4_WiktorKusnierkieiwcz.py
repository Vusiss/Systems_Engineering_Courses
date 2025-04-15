# zadanie 1

def wszystkie_perm(krotka):
    
    if len(krotka) == 0:
        return []
    elif len(krotka) == 1:
        return tuple([krotka])
    
    lista = list(krotka)
    listaZastąp = [] 
    
    for i in range(len(lista)):
        baza = lista[i]
        reszta = lista[:i] + lista[i+1:]
        
        for j in wszystkie_perm(reszta):
           if tuple([baza]) + tuple(j) not in listaZastąp: 
               listaZastąp.append(tuple([baza]) + tuple(j))
    return tuple(listaZastąp)

krotka = (1,4,6,6)
print(wszystkie_perm(krotka))   
    
krotka = ("Ala",)
print(wszystkie_perm(krotka))

krotka = ("Ala", "Cezary")
print(wszystkie_perm(krotka))

krotka = ("Ala", "Cezary", "Monika")
print(wszystkie_perm(krotka))

krotka = ("Ala", "Cezary", "Monika", "Dawid")
print(wszystkie_perm(krotka))

# zadanie 2

import functools

def saper(klatka,a,b):
    if klatka[a][b] == "*":
        return "*" 
    else:
        bomb = 0
        for i in range(a-1,a+2):
            for j in range(b-1,b+2):
                if 0 <= i < w and 0 <= j < h:
                    if klatka[i][j] == "*": bomb += 1 
        return bomb
    
def tłumacz(mapa,wysokość,szerokosć):
    for i in range(0,wysokość):
            for j in range(0,szerokosć):
                mapa[i][j] = str(saper(mapa,i,j))
    return mapa

w = int(input("Podaj ilość wierszy: "))
h = int(input("Podaj ilość kolumn: "))

Map = []
Wiersz = []
for i in range(0,w):
    for j in range(0,h):
        Wiersz += input(f"Podaj element planszy (* lub .) o indeksie [{i},{j}]: ")
    Map.append(Wiersz)
    Wiersz = []
        
Map = tłumacz(Map,w,h)

for i in range(len(Map)):
    print(functools.reduce(lambda a,b : a+b, Map[i]))
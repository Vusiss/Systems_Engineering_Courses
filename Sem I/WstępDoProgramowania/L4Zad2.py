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
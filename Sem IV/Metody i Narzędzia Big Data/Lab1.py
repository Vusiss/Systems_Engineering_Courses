# 1

# 2
def zad_2():
    for i in range(1,31):
        if i % 2 != 0:
            continue
        print(i)
# 3

def zad_3(x):
    s = 0
    i = 1
    while i<x:
        s+=i
        i+=1
    return s

# 4

def parzyste(x):
    s = 0
    for i in range(1,x+1):
        if i % 2 == 0:
            s+=i
        
    return s

# 5
def zad_5():
    for i in range(100, -101, -1):
        if i % 2 != 0:
            continue
        if i % 3 == 0 or i % 8 == 0:
            continue
        print(i)
        
# 6

def zad_6(n):
   
    tablica = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            tablica[i][j] = min(i,j) + 1
            
    for wiersz in tablica:
        print(' '.join(map(str, wiersz)))

# 7

def zad_7(lista,n):
    
    wynik = [[] for _ in range(n)]
    for i, element in enumerate(lista):
        wynik[i % n].append(element)
    print(wynik)

dane = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
n = 4
# zad_7(dane, n)


# 8

def zad_8(l1,l2):
    if len(l1) > 0:
        l1[-1:] = l2
    print(l1)

dane1 = [100, 90, 80, 70, 60, 50]
dane2 = [49, 39, 29, 19]
# zad_8(dane1, dane2)


# 9

def zad_9(lista, lancuch):
    return [lancuch + ' ' + element for element in lista]

dane = ['A', 'B', 'C', 'D']
# lancuch = input("Podaj łańcuch znakowy: ")
# wynik = zad_9(dane, lancuch)


# 10

def zad_10(list):
    print( [krotka[:-1] + (0,) for krotka in list])

list2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# zad_10(list2)


# 11

def zad_11(l):
    print([krotka for krotka in l if krotka])

l = [(), (), ('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), ('i4')]
# zad_11(l)


# 12

def zad_12(sl : dict):
    il = 1
    for i in sl.values():
        il *= i
    print(il)
    
sl = {'f1': 4.8, 'f2': 2.4, 'f3': 1.2, 'f4': 0.6}
# zad_12(sl)


# 13

def zad_13(n):
    sl = {}
    for i in range(1,n+1):
        sl[i] = i**4
    print(sl.items())
    
# zad_13(6)

# 14

def zad_14(d):
    unique_values = set(d.values())
    print(sorted(unique_values))


input_dict = {1: 'A201', 2: 'B218', 3:'H018', 4:'B218', 5:'H018', 6: 'G123', 7: 'A007', 8: 'G230'}
zad_14(input_dict)
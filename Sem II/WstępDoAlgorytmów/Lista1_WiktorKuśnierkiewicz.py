import random as r
import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1.

m = 6
n = 4
marks = [2,3,3.5,4,4.5,5,5.5]
    
l = [r.choice(marks) for i in range(m*n)]
    
matrix = np.array(l).reshape(m,n)   # macierz z losowymi ocenami
  
# Wyznaczyć liczbę studentów, którzy nie zaliczyli co najmniej n przedmiotów
k=0 
liczbaStudentów=0
liczbaN = 2

for i in range(m):
    for j in range(n):
        if 2.0 == matrix[i,j]:
            k+=1                    # Zlicza liczbę niezdanych przedmiotów przez studenta
    if k >= liczbaN:
        liczbaStudentów+=1
    k=0

print(liczbaStudentów)

# Oceny studentów z najniższą i najwyższą średnią

avg = [sum(matrix[i])/n for i in range(m)]  # średnie studentów

print(matrix[avg.index(max(avg))])
print(matrix[avg.index(min(avg))])

# Studenta (numer wiersza lub cały wiersz) z najwyższą liczbą ocen najwyższych (to niekoniecznie w danej tabeli musi być 5.5)

highScore = matrix.flatten()[np.argmax(matrix)]
highScoreCount = [list(matrix[i]).count(highScore) for i in range(m)]

print(matrix[highScoreCount.index(max(highScoreCount))])

# Histogramy (numpy.histogram) ocen z poszczególnych przedmiotów

for i in range(n):
    ocenyStud = matrix[:, i]
    hist, bins = np.histogram(ocenyStud, bins=10, range=(2.0, 5.5))
    plt.hist(ocenyStud, bins=bins)
    plt.title(f"Przedmiot {i + 1}")
    plt.xlabel("Oceny")
    plt.ylabel("Liczba studentów")
    plt.show() 


# Listę studentów ze średnimi nie niższymi niż 4.5

greatStudents = []

for i in range(m):
    if avg[i]>=4.5:
        greatStudents.append(i) # Studenci są reprezentowani poprzez indeksy

print(greatStudents)

# Zadanie 2

L = 5
M = 4

def odległośćSymetryczna(P,Q):
    sum = 0
    for i in range(L):
        for j in range(M):
            sum+= abs(P[i,j] - Q[i,j])
    return sum
            
P = np.arange(10,30).reshape(L,M)        # Przykładowe macierze
Q = np.arange(20).reshape(L,M)
print(odległośćSymetryczna(P,Q))

# Zadanie 3

N = 6
M = N+1


mat = np.random.random_integers(1,40,(N,M))
mat = mat.astype(float)

for i in range(N):
    if i >= M or i >= N: break
    a=1
    while mat[:,i].any() == 0:
        mat = np.delete(mat,i,1)
        M-=1
    while mat[i].any() == 0:
        mat = np.delete(mat,i,0)
        N-=1
    while mat[i,i] == 0:
        mat[[i,i+a]] = mat[[i+a,i]]
        a+=1
    
    mat[i]/=mat[i,i]
    for j in range(i+1,N):
        mat[j] -= mat[j,i]*mat[i]

print(mat)

# Zad 4


kupione = 4
wSklepie = 5

paragon = np.array([[1243,1222,4434,5446],["124","456","789","102"],[2.0,6.0,5.7,9.7]]).T
opisyTowarów = np.array([["123","456","789","102","543"],[2.79,3.00,10.99,5.00,12.99],["na sztuki","na wagę","na wagę","na sztuki","na sztuki"]]).T


def sprawdzenieParagonu(paragon,opisyTowarów):
    for i in range(kupione):
        
        
        if paragon[i,1] not in opisyTowarów[:,0]:
            return ("Produkt nie znajduje się w sklepie")
        tow = np.where(opisyTowarów == paragon[i,1])
        nrTowaru = (tow[0][0],tow[1][0])  
        if float(paragon[i,2]) != int(float(paragon[i,2])) and opisyTowarów[nrTowaru[0],2] == "na sztuki": 
            print("Produkt jest sprzedawany na wagę")
        else:
            print("Paragon został wydany poprawnie")
               
    cena = 0
    for i in range(kupione):
        tow = np.where(opisyTowarów == paragon[i,1])
        nrTowaru = (tow[0][0],tow[1][0])
        cena += round(float(paragon[i,2]) * float(opisyTowarów[nrTowaru[0],1]),2)

    return cena

print(sprawdzenieParagonu(paragon,opisyTowarów))

# Zadanie 1

a = (5 + 6) * 3

b = (6.893 + 5.74) * 3

c = 6 + 5 * 3 

d = 41 / 6

e = 41 // 6

f = 41 % 6

# zadanie 2

print(8**21, pow(8,21))

# zadanie 3



if a == b:
    print("Równe")
else:
    print("Nierówne")
    
# zadanie 4

liczba = float(input("Podaj liczbę: "))

dz = liczba/6

print(f"Wpisano liczbę: {liczba}, a jeśli ją podzielimy przez 6 to otrzymamy {dz:.3}")

# zadanie 5

wyr1 = (3+1.0==4 and not 5>7)
wyr2 = (3+1.0==4 and 5>7)
wyr3 = (3+1.0==4 or 5>7)
wyr4 = (3+1.0==4 or not 5>7)
print(type(wyr1),wyr1,type(wyr2),wyr2,type(wyr3),wyr3,type(wyr4),wyr4)

# zadanie 6

a = float(input())

if a == int(a):
    print("liczba jest całkowita")
else:
    print("liczba nie jest całkowiat lub nie jest liczbą")
    
# zadanie 7

a = int(input())

if a < 6 :
    print("Liczba jest za mała")
elif a == 24:
    print("liczba nie moe być równa 24")
elif a == 43: 
    print("liczba nie moe być równa 43")
else:
    print("liczba jest prawidłowa")
    
#zadanie 8

a = int(input())

while a > 2:
    a -= 7
    if a == 13:
        break
    
print(a)    
    
# zadanie 9

for i in range(6,52):
    print(i)
    
# zadanie 10

for i in range(7,52,2):
    print(i)
    
# zadanie 11

s = 0

for i in range(6,52):
    s+=i

print(s)

    

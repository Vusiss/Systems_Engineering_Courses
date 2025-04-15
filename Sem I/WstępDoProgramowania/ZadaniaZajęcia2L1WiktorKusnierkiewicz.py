#Zadanie 1.

print("Nazywa","się","Monty","Python.",sep="-")

#Zadanie 2.

s = '"świecie"'
print(f"Witaj {s} Pythona")
print('Witaj "świecie" Pythona')

#Zadanie 3.

print("""pierwszy wiersz
 drugi wiersz
  trzeci wiersz""") 

#Zadanie 4.

print("Jan"*12)

#Zadanie 5.

a = int(input("Podaj pierwszy składnik dodawania:"))
b = int(input("Podaj drugi składnik dodawania:"))
print(f"Wynik dodawania {a} + {b} to {a+b}")

#Zadanie 6.


liczba1 = 3.14159
liczba2 = 3
liczba3 = 7.12
liczba4 = "5"
print("{:.4}".format(liczba1),f"{type(liczba1)}")
print("%.3f"%(liczba2),f"{type(liczba2)}")
print("%.3f"%(liczba3),f"{type(liczba3)}")
print("%.3f"%(float(liczba4)),f"{type(liczba4)}")

#Zadanie 7.

osoba1 = "Anna Cis"
osoba2 = "Konstanty Mączyński"
stanowisko1 = "kierowniczka działu HR"
stanowisko2 = "kierowca"
pensja1 = 7500
pensja2 = 12000
print("{}{:\t^16}{:\t>6}".format("Osoba", "Stanowisko", "Pensja"))
print("{}{:\t^26}{:\t>4}".format(osoba1, stanowisko1, pensja1))
print("{}{:\t^11}{:\t>6}".format(osoba2, stanowisko2, pensja2))


#Zadanie 8.


a = "Programowanie "
b = "jest "
c = "fajne"

print("\033[94m",a+"\033[91m",b,"\033[92m","\033[3m",c,"\033[m"".",sep="")
print("\033[94m",a+"\033[91m",b,"\033[1m","\033[92m","\033[3m","\033[51m",c,"\033[m"".",sep="")
print("\033[43m","\033[94m",a+"\033[1m","\033[91m",b,"\033[3m","\033[92m",c,"\033[m"".",sep="")
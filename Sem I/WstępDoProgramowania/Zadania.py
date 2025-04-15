#zadanie 1.1

print("Monty Python")

#zadanie 1.2

print("")

#zadanie 1.3

print()
print("\n")
print(end="\n")
print("")
print("{}".format("\n"))

#zadanie 2

print("Nazywa","się","Monty","Python.",sep="-")

#zadanie 3

s = '"świecie"'
print(f"Witaj {s} Pythona")
print('Witaj "świecie" Pythona')

#zadanie 4

print("pierwszy wiersz",
" drugi wiersz",
"  trzeci wiersz",sep="\n") #nie wiem jak to rozwiazać inaczej

#zadanie 5

print("Jan"*12)

#zadanie 6

kierownik = "Emil"
pracownik = "Daniel"

print(f"Kierownikiem firmy jest {kierownik}, a pracownikiem jest {pracownik}.")

#zadanie 7

liczba1 = 3.14159
liczba2 = 3
liczba3 = 7.12
liczba4 = "5"
print(liczba1,f"{type(liczba1)}")
print(liczba2,f"{type(liczba2)}")
print(liczba3,f"{type(liczba3)}")
print(liczba4,f"{type(liczba4)}")

#zadanie 8

osoba1 = "Anna Cis"
osoba2 = "Konstanty Mączyński"
stanowisko1 = "kierowniczka działu HR"
stanowisko2 = "kierowca"
pensja1 = 7500
pensja2 = 12000
print("{:<30}{:^30}{:>30}".format("Osoba", "Stanowisko", "Pensja"))
print("{:<30}{:^30}{:>30}".format(osoba1, stanowisko1, pensja1))
print("{:<30}{:^30}{:>30}".format(osoba2, stanowisko2, pensja2))
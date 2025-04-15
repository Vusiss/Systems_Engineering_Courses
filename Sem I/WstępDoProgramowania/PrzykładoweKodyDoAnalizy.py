""" Wskazówki dotyczące stylu kodu – PEP8
   https://www.python.org/dev/peps/pep-0008/"""

print("Lubię programować w Pythonie")
print("Lubię\t programować\t w Pythonie")
print("Lubię\n programować\t w Pythonie")
# r-String
print(r"Lubię\n programować\t w Pythonie")
print("Lubię", "programować", "w Pythonie")
print("Lubię" + "programować", "w Pythonie")
print("Lubię", "programować", "w Pythonie", sep="**", end="^^^")

print("\n\n")

print("*"*20, "Gwiazdkowanie", "*"*20)

print("Jego imię to %s i zarabia on %d złotych." % ("Andrzej", 3500))
print("Jego imię to {} i zarabia on {} złotych.".format("Andrzej", 3500))
print("Jego imię to {:^30} i zarabia on {} złotych.".format("Andrzej", 3500))

print("\n"*3)

print("Programowanie".format)
print("Programowanie {}".format("w Pythonie"))

print("Lubię {}, {} oraz {}.".format("programować", "czytać", "śpiewać"))
print("Lubię {0}, {1} oraz {2}.".format("programować", "czytać", "śpiewać"))
print("Lubię {1}, {2} oraz {0}.".format("programować", "czytać", "śpiewać"))
print("Lubię {hobby_dom}, {hobby_praca} oraz {hobby_wyjazd}.".format(hobby_praca="programować", hobby_dom="czytać", hobby_wyjazd="śpiewać"))

print("\n"*3)
co_lubię = "programować"
print("Lubię",co_lubię)
co_lubię="spać"
print("Lubię",co_lubię)

print("\n"*3)
co_lubię = "programować"
print("Lubię"+co_lubię)
co_lubię="spać"
print("Lubię"+co_lubię)

# f-Stringi
print()
co_lubię = "programować"
print(f"Lubię {co_lubię}")
co_lubię="spać"
print(f"Lubię {co_lubię}")

# sprawdzenie typu danych
print(f"Typem danych 'co_lubię' jest {type(co_lubię)}.")
liczba1 = 3.14159
print(f"Typem danych 'liczba1' jest {type(liczba1)}.")
liczba2 = 3
print(f"Typem danych 'liczba2' jest {type(liczba2)}.")
czy_tak = True
print(f"Typem danych 'czy_tak' jest {type(czy_tak)}.")
typ_None = None
print(f"Typem danych 'typ_None' jest {type(typ_None)}.")

print("\n"*3)
liczba1 = 3.14159
print(f"Typem danych 'liczba1' jest {type(liczba1)}.")
liczba1 = "programowanie"
print(f"Typem danych 'liczba1' jest {type(liczba1)}.")

# https://www.python.org/dev/peps/pep-0484/
# Adnotacja typów
print("\n"*3)
liczba1: float = 3.14159
print(f"Typem danych 'liczba1' jest {type(liczba1)}.")
liczba1 = "programowanie"
print(f"Typem danych 'liczba1' jest {type(liczba1)}.")
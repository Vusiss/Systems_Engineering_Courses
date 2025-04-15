#zadanie 1
def dodaj(a, b=7):
    return(a + b)

def wywolaj(func,*parametry):
    if callable(func):
        print("wywołuję funkcję {}({})".format(func.__name__,parametry))
        return func(*parametry)
    else: print("Nie można wywołać {}({})".format(str(func),parametry))

    

wywolaj(print, "Programowanie jest fajne")
wywolaj(print, "Programowanie", "jest fajne")
wywolaj(print)
wywolaj(5, "Programowanie", "jest fajne")
wywolaj(5)
print(wywolaj(dodaj, 2, 13))

#zadanie 2

def debuguj(func):
    def argumenty(*args):
        print("*"*20,"funkcja",func.__name__,"*"*20)
        print("argumenty pozycyjne:", args)
        print("wynik:", func(*args))
        print("\n"*4)
    return argumenty


@debuguj
def dodaj(a, b=7):
    return(a + b)


dodaj(5, 3) 
dodaj(3)
def rozstrzygnij_A(alfabet, slowo):
    if 'x' not in slowo:
        return "język nierozstrzygnięty (brak symbolu 'x' w słowie)"

    #podział słowa na część przed i po 'x'
    czesci = slowo.split('x')

    # Jeśli x jest na początku lub końcu lub jest więcej niż jedno; nie spełnia warunków
    if len(czesci) != 2 or czesci[0] == "" or czesci[1] == "":
        return "język nierozstrzygnięty (błędna struktura słowa)"

    a, b = czesci

    #sprawdzenie czy a i b składają się tylko z symboli z alfabetu
    if not set(a).issubset(alfabet) or not set(b).issubset(alfabet):
        return "język nierozstrzygnięty (słowo zawiera znaki spoza alfabetu)"

    #sprawdzenie warunku |a| = |b|
    if len(a) == len(b):
        return "język rozstrzygnięty (słowo należy do A)"
    else:
        return "język rozstrzygnięty (słowo nie należy do A)"


alfabet = {'e', 'h', 'f'}

#test
testy = ["x", "hexhf", "hexhff"]

for test in testy:
    wynik = rozstrzygnij_A(alfabet, test)
    print(f"Słowo: {test} -> {wynik}")
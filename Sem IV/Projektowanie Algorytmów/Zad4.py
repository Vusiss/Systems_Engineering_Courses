#Maszyna Turinga na wejściu otrzymuje ciąg znaków reprezentujący listę wierzchołków w postaci:
# [v1, v2, v3, ..., vn] gdzie każdy wierzchołek vi składa się z cyfr (0-9) a elementy oddziela przecinek
#Poprawny format:
#Początek to znak [ a koniec ]
#Wierzchołki są poprawnymi liczbami
#Przecinki występują tylko między wierzchołkami
#Brak pustych wartości (nie może wystąpić [,])

#1. Przejdź na początek taśmy i odczytaj pierwszy znak:
#   a) Jeśli to `[`, przejdź do kroku 2.
#   b) W przeciwnym razie ODRZUĆ wejście.

#2. Przejdź do następnego znaku i sprawdzaj kolejne symbole:
#   a) Jeśli to cyfra (0-9), przejdź do kroku 3.
#   b) Jeśli to `]` i wcześniej były poprawne wierzchołki, PRZYJMIJ wejście.
#   c) W przeciwnym razie ODRZUĆ wejście.

#3. Odczytuj kolejne cyfry (tworząc liczbę):
#   a) Jeśli natrafisz na kolejną cyfrę (0-9), kontynuuj.
#   b) Jeśli natrafisz na `,`, przejdź do kroku 4.
#   c) Jeśli natrafisz na `]`, przejdź do kroku 5.
#   d) Jeśli natrafisz na inny znak, ODRZUĆ wejście.

#4. Sprawdź, czy po `,` jest kolejna cyfra:
#   a) Przejdź do następnego znaku.
#   b) Jeśli to cyfra (0-9), wróć do kroku 3.
#   c) Jeśli to inny znak, ODRZUĆ wejście.

#5. Sprawdź, czy `]` jest poprawnym zakończeniem:
#   a) Jeśli wcześniej był przynajmniej jeden poprawny wierzchołek, PRZYJMIJ wejście.
#   b) W przeciwnym razie ODRZUĆ wejście.


#Przykłady poprawnych wejść:
#[1, 23, 456]
#[10]
#[5, 6, 7, 8, 9]
#Przykłady błędnych wejść:
#[1,,2]
#[1,]
#[1, 2
#1,2,3]

#Przykłady testowe:
#w1 = [0107, 999422, 3] POPRAWNE
#w2 = [0107 999422, 3] NIEPOPRAWNE
#w3 = [0107, 999a22, 3] NIEPOPAWNE
# a)
dane <- read.csv("/Users/vusis/Documents/Program/StatystykaR/mieszkania.csv", header = TRUE, sep = ";")

# b)
print(dane[0:6, 0:5])

# c)
print(str(dane))


# d)
print(mean(dane$Metraz))
print(mean(dane$Cena))

# e)
dane$Cena_m2 <- (dane$Cena / dane$Metraz)

# f)
psie_pole <- dane[dane$Dzielnica == "Psim Polu" & dane$Cena < 400000, ]

# g)
srodmiescie <- dane[dane$Dzielnica == "Śródmieście" & dane$Metraz > 60, ]

# h)
liczba_mieszkan <- sum(dane$Metraz > 60 & dane$Cena < 350000)
print(liczba_mieszkan)

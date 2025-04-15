# Zadanie 3

ilość_rzutów <- 180
szansa_na_jedynkę <- 1 / 6

a1 <- dbinom(27, ilość_rzutów, szansa_na_jedynkę)

a2 <- 1 - pbinom(31, ilość_rzutów, szansa_na_jedynkę)

a3 <- pbinom(28, ilość_rzutów, szansa_na_jedynkę)

a4 <- pbinom(33, ilość_rzutów, szansa_na_jedynkę) - pbinom(24, ilość_rzutów, szansa_na_jedynkę)

# Zadanie 4

intensywnosc <- 3.5
czas <- 5

b1 <- dpois(16, intensywnosc * czas)

b2 <- 1 - ppois(19, intensywnosc * czas)

b3 <- ppois(11, intensywnosc * czas)

b4 <- ppois(21, intensywnosc * czas) - ppois(13, intensywnosc * czas)

# Zadanie 5


n <- 100  
p <- 0.02 
x <- 0:n

plot(dbinom(x, n, p), type = "h")

lambda <- 2

lines(dpois(x, lambda), col = "red")

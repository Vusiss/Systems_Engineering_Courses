#1

min <- 4
max <- 12
a1 <- punif(7,min, max)
cat(a1,"\n")

b1 <- punif(11,min, max) - punif(5, min, max)
cat(b1,"\n")

c1 <- 1 - punif(10, min, max)
cat(c1,"\n")

d1 <- 1 - qunif(0.6, min, max)
cat(d1,"\n")

#2

lambda <- 4/60
a2 <- 1 - pexp(30, lambda)
cat(a2,"\n")

b2 <- pexp(20, lambda)
cat(b2,"\n")

c2 <- pexp(80, lambda) - pexp(40, lambda)
cat(c2,"\n")

d2 <- qexp(0.2, lambda)
cat(d2,"\n")

wartość <- seq(0,3,0.1)
gęstość <- dexp(wartość, lambda)

# Trzeba odkomentować wykres, by go wyswietlić
# plot(wartość, gęstość, type = "l", xlab = "Sekundy", ylab = "Gęsetosc p'stwa", main = "Zmienność T")

#3

lambda <- 1/3
a3 <- 1 - pexp(2, lambda)
cat(a3,"\n")

b3 <- pexp(4, lambda)
cat(b3,"\n")

c3 <- pexp(5, lambda) - pexp(3, lambda)
cat(c2,"\n")

d3 <- qexp(0.4, lambda)
cat(d3,"\n")

#4

oczekiwane <- 170
odchylenie <- 12
a4 <- 1 - pnorm(180, oczekiwane, odchylenie)
cat(a4,"\n")

b4 <- pnorm(165, oczekiwane, odchylenie)
cat(b4,"\n")

c4 <- pnorm(190, oczekiwane, odchylenie) - pnorm(155, oczekiwane, odchylenie)
cat(c4,"\n")

przedział <- seq(130, 210, 1)
gęstość <- dnorm(przedział, oczekiwane, odchylenie)

# Trzeba odkomentować wykres, by go wyswietlić
# plot(przedział, gęstość, type = "l", xlab = "Dlugosc (cm)", ylab = "Gestosc", main = "Gestosc zmiennej X")
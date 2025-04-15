# nośniki zmiennych
x <- c(0, 1) # Definicja wektorów x i y
y <- c(0, 1, 2)

# rozmiary macierzy
m <- length(x) 
n <- length(y) 

pxy <- matrix(c(1/8, 1/6, 1/4, 1/6, 1/8, 1/6), nrow = m) # Utworzenie macierzy pxy o wymiarach m x n i przypisanie jej wartości.

# rozkłady brzegowe
px <- array(0, dim = m) 
py <- array(0, dim = n)

# rozkłady warunkowe y - pierwszy wiersz P(Y=y|X=0), drugi P(Y=y|X=1)
pyc <- array(0, dim = c(m, n)) 
for (i in 1:m) {
  px[i] <- sum(pxy[i, 1:n]) 
}
for (j in 1:n) {
  py[j] <- sum(pxy[1:m, j]) 
}
px 
py 

# wartości oczekiwane
ex <- sum(x * px)
ey <- sum(y * py) 
ex2 <- sum(x * x * px)
ey2 <- sum(y * y * py) 
varx <- ex2 - ex^2 # Obliczenie wariancji zmiennej x 
vary <- ey2 - ey^2 # Obliczenie wariancji zmiennej y 

# rozkład oraz wartości x, y w postaci wektorowej
(xv <- rep(x, times = n)) # Wygenerowanie wektorów zawierających elementy wektorów x i y powtórzone n razy
(yv <- rep(y, each = m)) 
(pv <- c(pxy)) # Przekształcenie macierzy pxy do postaci wektora
exy <- sum(pv * xv * yv) # Obliczenie wartości oczekiwanej iloczynu x i y przy użyciu wektora pv, xv i yv
covxy <- exy - ex * ey # Obliczenie kowariancji między x i y

# współczynnik korelacji
(rhoxy <- covxy / (varx * vary)^0.5) # Obliczenie współczynnika korelacji

for (i in 1:m) {
  pyc[i, ] <- pxy[i, ] / px[i] # Obliczenie rozkładu warunkowego y dla każdego x
}
pyc

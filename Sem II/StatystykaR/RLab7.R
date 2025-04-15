
k <-pnorm(164,170,12)
l <-1-pnorm(188,170,12)
m <- pnorm(185,170,12) - pnorm(158,170,12)

q <- qnorm(1- 0.15,170,12)



#2
U1 <- runif(10000)
U2 <- runif(10000)
Z <- cos(2 * pi * U1) * sqrt(-2 * log(U2))

est_Z <- density(Z)
# curve(dnorm(x), -10, 10, col = 'red', lwd = 3)
# lines(est_Z, col = 'black', lwd = 3)

Y <- 100 + 15 * Z

est_Y <- density(Y)

# curve(dnorm(x, mean = 100, sd = sqrt(15)), 0, 300, col = "red", lwd = 2, main = "Porownanie estymatora jadrowego gestosci dla Y z gestoscia rozkladu normalnego")
# lines(est_Y, col = "black", lwd = 2)





#3
X <- rnorm(2000, mean = 170, sd = 12)
Z <- (X - 170) / 12
estym_j_Z <- density(Z)

# curve(dnorm(x), -4, 4, col = "red", lwd = 2, main = paste("Por, n =", 2000))
# lines(estym_j_Z, col = "black", lwd = 2)

X <- rnorm(500, mean = 170, sd = 12)
Z <- (X - 170) / 12
estym_j_Z <- density(Z)

# curve(dnorm(x), -4, 4, col = "red", lwd = 2, main = paste("Por 1, n =", 500))
# lines(estym_j_Z, col = "black", lwd = 2)

X <- rnorm(100, mean = 170, sd = 12)
Z <- (X - 170) / 12
estym_j_Z <- density(Z)

# curve(dnorm(x), -4, 4, col = "red", lwd = 2, main = paste("Por 2, n =", 100))
# lines(estym_j_Z, col = "black", lwd = 2)

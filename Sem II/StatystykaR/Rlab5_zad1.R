random_J <- runif(min = 0, max = 1, n = 5000)
random_N <- rnorm(3000, 100, 15)





hist_J <- hist(random_J, breaks = 30, main = "Histogram - Rozkład Jednostajny", xlab = "Wartości", ylab = "Gęstość", freq = FALSE)
hist_N <- hist(random_N, breaks = 30, main = "Histogram - Rozkład Normalny", xlab = "Wartości", ylab = "Gęstość", freq = FALSE)
density_J <- density(randomJ)
density_N <- density(randomN)

par(mfrow = c(2, 2))
plot(hist_J, main = "Histogram - Rozkład Jednostajny")
plot(hist_N, main = "Histogram - Rozkład Normalny")
plot(density_J, main = "Estymator jądrowy - Rozkład Jednostajny")
plot(density_N, main = "Estymator jądrowy - Rozkład Normalny")
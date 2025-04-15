# Wczytanie danych
data <- read.csv("waga1.csv", sep=";", header = TRUE)  

# Test Z
# Obliczenie średniej i odchylenia standardowego wzrostu
srednia <- mean(dane$Wzrost)
odchylenie_std <- sd(dane$Wzrost)

# Liczenie wartości Z
Z_wartosc <- (srednia - 168) / (odchylenie_std / sqrt(length(dane$Wzrost)))

# Obliczanie p-wartości dla dwustronnego testu
p_wartosc_Z <- 2 * (1 - pnorm(abs(Z_wartosc)))

# Test t-Studenta
# Używając funkcji t.test
test_t <- t.test(dane$Wzrost, mu = 168)

# Wypisanie wyników
cat("Test Z:\n")
cat("Wartość Z:", Z_wartosc, "\n")
cat("p-wartość:", p_wartosc_Z, "\n\n")

cat("Test t-Studenta:\n")
cat("Wartość testowa t:", test_t$statistic, "\n")
cat("p-wartość:", test_t$p.value, "\n")

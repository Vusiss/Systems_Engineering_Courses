# Wyniki rzutów kostką
wyniki <- c(171, 200, 168, 213, 226, 222)

# Oczekiwane frekwencje przy hipotezie, że kostka jest symetryczna
n <- sum(wyniki)
p <- rep(1/6, 6)
oczekiwane_frekwencje <- n * p

# Wyznaczenie statystyki testowej i wartości p
test <- chisq.test(wyniki, p = p)

# Wyniki
print(oczekiwane_frekwencje)
print(test$statistic)
print(test$p.value)



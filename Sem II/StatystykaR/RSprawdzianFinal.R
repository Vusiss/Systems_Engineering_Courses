# Dane

file_path <- "waga1.csv"
data <-- read.csv(file_path, header = TRUE, sep = ";")

data <- data*-1 # Nie wiem dlaczego, ale wartości wczytują się ujemne, więc przemnaam je przez -1

male_students <- subset(data, plec == 0)
wzrost <- male_students$Wzrost

mu <- 174
sigma <- sd(wzrost)  
n <- length(wzrost)


mean_sample <- mean(wzrost)


z_stat <- (mean_sample - mu) / (sigma / sqrt(n))
p_value_z <- 2 * (1 - pnorm(abs(z_stat))) 

t_test_result <- t.test(wzrost, mu = 174)

# cat(z_stat, "\n")
cat(p_value_z, "\n\n")

# cat(t_test_result$statistic, "\n")
cat(t_test_result$p.value, "\n")



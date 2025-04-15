

# Load the data
data <- read.csv("waga1.csv", header = TRUE, sep = ";")

# Calculate the weight gain
data <- data %>% mutate(Waga_gain = Waga_po - Waga_przed)

# Calculate the necessary statistics
mean_gain <- mean(data$Waga_gain)
sd_gain <- sd(data$Waga_gain)
n <- nrow(data)

# Given values
mu_0 <- 2
alpha <- 0.01

# Z-test
z_value <- (mean_gain - mu_0) / (sd_gain / sqrt(n))
p_value_z <- 2 * pnorm(-abs(z_value))

# Critical value for Z-test
critical_value_z <- qnorm(1 - alpha / 2)

cat("Z\n")
cat("Z-value: ", z_value, "\n")
cat("P-value: ", p_value_z, "\n")
cat("Critical value (Z): ", critical_value_z, "\n\n\n")

# Test studenta
t_value <- (mean_gain - mu_0) / (sd_gain / sqrt(n))
p_value_t <- 2 * pt(-abs(t_value), df = n - 1)
critical_value_t <- qt(1 - alpha / 2, df = n - 1)

cat("Test studenta\n")
cat("T-value: ", t_value, "\n")
cat("P=", p_value_t, "\n")
cat("Critical value (T): ", critical_value_t, "\n\n\n")

# T
t_test_result <- t.test(data$Waga_gain, mu = 2)

cat("T\n")
print(t_test_result)

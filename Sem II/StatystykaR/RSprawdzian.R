data <- read.csv("waga1.csv", header = TRUE, sep = ";")

male_data <- data %>% filter(plec == 0)
female_data <- data %>% filter(plec == 1)


mean_male <- mean(male_data$Waga_po)
mean_female <- mean(female_data$Waga_po)
sd_male <- sd(male_data$Waga_po)
sd_female <- sd(female_data$Waga_po)
n_male <- nrow(male_data)
n_female <- nrow(female_data)

# Z-test
z_value <- (mean_male - mean_female) / sqrt((sd_male^2 / n_male) + (sd_female^2 / n_female))
p_value_z <- 2 * pnorm(-abs(z_value))

cat("Z-test\n")
cat("Z-value: ", z_value, "\n")
cat("P-value: ", p_value_z, "\n")

# T-test
t_test_result <- t.test(male_data$Waga_po, female_data$Waga_po, var.equal = TRUE)

cat("T-test\n")
print(t_test_result)



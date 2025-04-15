
n <- 100
x <- 30
mu <- 109
war <- 225
a_95 <- 0.05
a_99 <- 0.01


p_hat <- x / n
sigma <- sqrt(war)
SE <- sqrt(p_hat * (1 - p_hat) / n)


Z_95 <- qnorm(1 - a_95/2)
CI_95 <- p_hat + c(-1, 1) * Z_95 * SE
cat(CI_95)


Z_99 <- qnorm(1 - a_99/2)
CI_99 <- p_hat + c(-1, 1) * Z_99 * SE
cat( CI_99)


Z_95 <- qnorm(1 - a_95/2)
SE <- sqrt(war) / sqrt(n)
CI_mean_95_normal <- c(mu - Z_95 * SE, mu + Z_95 * SE)
cat(CI_mean_95_normal)


Z_99 <- qnorm(1 - a_99/2)
CI_mean_99_normal <- c(mu - Z_99 * SE, mu + Z_99 * SE)
cat(CI_mean_99_normal)




t_95 <- qt(1 - a_95/2, df = n - 1)
CI_mean_95_student <- c(mu - t_95 * SE, mu + t_95 * SE)
cat(CI_mean_95_student)


t_99 <- qt(1 - a_99/2, df = n - 1)
CI_mean_99_student <- c(mu - t_99 * SE, mu + t_99 * SE)
cat(CI_mean_99_student)




# 2. 

data <- read.csv("waga1.csv", sep=";")
n <- nrow(data)
mean_height <- mean(data$Wzrost)
sd_height <- sd(data$Wzrost)
alpha <- 0.1
z_value <- qnorm(1 - alpha/2)
ci_normal <- c(mean_height - z_value * (sd_height/sqrt(n)), mean_height + z_value * (sd_height/sqrt(n)))

cat(ci_normal)


df <- n - 1
t_value <- qt(1 - alpha/2, df)
ci_student <- c(mean_height - t_value * (sd_height/sqrt(n)), mean_height + t_value * (sd_height/sqrt(n)))
cat(ci_student)
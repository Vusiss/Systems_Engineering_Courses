# Dane dla pierwszej grupy (uczacy się języków)
data <- read.csv("waga1.csv", header = TRUE, sep = ";")
wzrost <- data$Wzrost


n1 <- length(wzrost)
mean1 <- 170
sd1 <- (max(wzrost) - min(wzrost))/2



# Poziom ufności
alpha <- 1 - 0.94


df <- n1 - 1

t_critical <- qt(1 - alpha/2, df)


ci1 <- c(mean1 - t_critical * sd1 / sqrt(n1), mean1 + t_critical * sd1 / sqrt(n1))


print(paste("Przedział ufności dla uczących się języków: [", ci1[1], ",", ci1[2], "]"))


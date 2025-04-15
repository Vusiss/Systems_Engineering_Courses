x <- c(2, 3, 3.5, 4, 4.5, 5)
y <- c(2, 3, 3.5, 4, 4.5, 5)
pxy <- matrix(c(0.05, 0.03, 0.02, 0, 0, 0,
                0.05, 0.07, 0.05, 0.03, 0, 0,
                0.03, 0.05, 0.06, 0.04, 0.02, 0,
                0.01, 0.04, 0.06, 0.06, 0.02, 0.01,
                0, 0.02, 0.05, 0.08, 0.04, 0.01,
                0, 0.01, 0.01, 0.02, 0.03, 0.03), nrow = length(x), byrow = TRUE)

px <- rowSums(pxy)
py <- colSums(pxy)
ex <- sum(x * px)
ey <- sum(y * py)
varx <- sum((x - ex)^2 * px)
vary <- sum((y - ey)^2 * py)
exy <- sum(outer(x, y, function(x, y) x * y) * c(pxy))
covxy <- exy - ex * ey
rhoxy <- covxy / sqrt(varx * vary)


l <- length(x)
pyc <- array(0, dim = c(l, l))
for (i in 1 : l) {
  pyc[i,] <- pxy[i,] / px[i]
}

n <- 1000
samples <- numeric(n)
for (i in 1:n) {
  
  sampled_x <- sample(x, size = 1, prob = px)
  sampled_y <- sample(y, size = 1, prob = pyc[which(x == sampled_x),])
  
  samples[i] <- paste0(sampled_x, "_", sampled_y)
}

table(samples) / n

cor_matrix <- matrix(as.numeric(unlist(strsplit(samples, "_"))), ncol = 2)
cor_matrix <- cor_matrix[complete.cases(cor_matrix),]
cor_pearson <- cor(cor_matrix)[1,2]
cor_spearman <- cor(cor_matrix, method = "spearman")[1,2]
cor_kendall <- cor(cor_matrix, method = "kendall")[1,2]
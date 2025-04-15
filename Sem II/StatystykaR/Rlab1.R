
# i)
a <- seq(300, 0, by = -3)
b <- c("one", "two", "three", "four", "5")
c <- c("one", "two", "three", "four", "5")
d <- c(3, 1, 6, 3, 1, 6, 3, 1, 6, 3, 1, 6)
e <- c(3, 3, 3, 3, 1, 1, 1, 1, 6, 6, 6, 6)
f <- c(5, 1, 4, 7)

# ii)
info_vector <- function(vector) {

    length <- length(vector)
    typeof <- typeof(vector)
    min <- min(vector)
    max <- max(vector)
    if (is.numeric(vector)) {
        sum <- sum(vector)
    } else {
        sum <- 0
    }
  return(c(length, typeof, min, max, sum))
}

print(info_vector(a))
print(info_vector(b))
print(info_vector(c))
print(info_vector(d))
print(info_vector(e))
print(info_vector(f))

# iii)
print(sort(b))
print(sort(e))

# iv)
print(d + f)
print(sum(d * f))
print(a[35])
print(a[67:85])

# v)

print(length(a[a < 100]))

# 4 i)

A = matrix(c(-3, 1, -2, 4, -5, 3),2,3,byrow = TRUE)
B = matrix(c(1,2,3,4,5,6),3,2,byrow = TRUE)
C = matrix(c(7,-3,-2,1),2,2,byrow = TRUE)
D = matrix(c(1,2,4,3,5,7,2,3,2),3,3,byrow = TRUE)

# ii)



#print(A + B) # Nie mozna dodawać maiciezy o róznych kształtach
print(t(A) + B)
print(B %*% A) 
print(B * B)

print(solve(C))
print(solve(C) %*% C)


# iii)

# Dla XC = B

X1 <- B %*% solve(C)

print(X1)

# Dla DX = B

X2 <- solve(D) %*% B

print(X2)

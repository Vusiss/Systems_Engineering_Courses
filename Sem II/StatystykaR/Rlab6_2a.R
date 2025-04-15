# generowanie pary (X,Y) za pomocą rozkładu łącznego
# p'stwa dla rozkładu łącznego, pv
# liczba elementów w rozkładzie łącznym
mn <- m * n

# p'stwa skumulowane
s <- array(dim = mn) 
s[1] <- pv[1] # Przypisanie pierwszego elementu wektora pv do pierwszego elementu wektora s.
for (i in 2:mn) {
  s[i] <- s[i - 1] + pv[i] # Obliczenie i-tego elementu wektora s na podstawie poprzedniego elementu oraz i-tego elementu wektora pv.
}

# realizacja
x_rea <- array(dim = 1000)
y_rea <- array(dim = 1000)

# 1000 realizacji z U[0,1]
r <- runif(1000) # Wygenerowanie 1000 liczb losowych z rozkładu jednostajnego na przedziale [0,1].
for (j in 1:1000) {
  i <- 1
  while (r[j] > s[i]) {
    i <- i + 1 # Znalezienie indeksu i takiego, że r[j] <= s[i].
  }
  x_rea[j] <- xv[i] # Przypisanie odpowiedniej wartości x na podstawie wylosowanego indeksu i do wektora x_rea.
  y_rea[j] <- yv[i]
}

mat_rea <- cbind(x_rea, y_rea) # Utworzenie macierzy mat_rea poprzez złączenie wektorów x_rea i y_rea.

tab <- table(x_rea, y_rea) 
(tab_r <- tab / length(x_rea)) 

(r_p <- cor(x_rea, y_rea)) # Obliczenie współczynnika korelacji Pearsona między x_rea i y_rea

(r_s <- cor(x_rea, y_rea, method = "spearman")) # Obliczenie współczynnika korelacji Spearmana 

(r_k <- cor(x_rea, y_rea, method = "kendall")) # Obliczenie współczynnika korelacji Kendall'a

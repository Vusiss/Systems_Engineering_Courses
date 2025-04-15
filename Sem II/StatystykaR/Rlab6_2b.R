# generowanie pary (X,Y) za pomocą rozkładów brzegowych
# p'stwa skumulowane dla zmiennej X
sx <- array(0, dim = m) 
sx[1] <- px[1]
for (i in 2:m) {
  sx[i] <- sx[i - 1] + px[i] # Obliczenie i-tego elementu wektora sx na podstawie poprzedniego elementu oraz i-tego elementu wektora px.
}

# p'stwaskumulowane dla zmiennej Y przy danej X
sy <- array(0, dim = c(m, n)) # Utworzenie macierzy sy o wymiarach m x n i wypełnienie jej zerami.
sy[, 1] <- pyc[, 1] # Przypisanie pierwszej kolumny macierzy pyc do pierwszej kolumny macierzy sy.
for (j in 2:n) {
  sy[, j] <- sy[, j - 1] + pyc[, j] # Obliczenie j-tej kolumny macierzy sy na podstawie poprzedniej kolumny oraz j-tej kolumny macierzy pyc.
}

sx 
sy

N <- 1000

x_rea <- array(0, dim = N)
y_rea <- array(0, dim = N)
for (k in 1:N) {
  # generowanie x
  u <- runif(1)
  ii <- 1
  while (u > sx[ii]) {
    ii <- ii + 1 # Znalezienie indeksu ii takiego, że u <= sx[ii].
  }
  x_rea[k] <- x[ii] # Przypisanie odpowiedniej wartości x na podstawie wylosowanego indeksu ii do wektora x_rea.

  # generowanie y z rozkładu warunkowego
  u <- runif(1) 
  jj <- 1
  while (u > sy[ii, jj]) {
    jj <- jj + 1 # Znalezienie indeksu jj takiego, że u <= sy[ii, jj].
  }
  y_rea[k] <- y[jj] # Przypisanie odpowiedniej wartości y na podstawie wylosowanego indeksu jj do wektora y_rea.
}

mat_rea <- cbind(x_rea, y_rea) # Utworzenie macierzy mat_rea poprzez złączenie wektorów x_rea i y_rea.

tab <- table(x_rea, y_rea)
(tab_r <- tab / length(x_rea)) # Obliczenie stosunku częstości występowania do liczby realizacji i wyświetlenie tablicy przestawnej.

(r_p <- cor(x_rea, y_rea)) # Obliczenie współczynnika korelacji Pearsona między x_rea i y_rea

(r_s <- cor(x_rea, y_rea, method = "spearman")) # Obliczenie współczynnika korelacji Spearmana między x_rea i y_rea

(r_k <- cor(x_rea, y_rea, method = "kendall")) # Obliczenie współczynnika korelacji Kendall'a między x_rea i y_rea

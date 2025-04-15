# nośniki zmiennych
x<-c(0,1)
y<-c(0,1,2)
# rozmiary macierzy
m<-length(x)
n<-length(y)
# macierz p'pstwa łącznego rozkładu pxy
pxy<-matrix(c(1/8,1/6,1/4,1/6,1/8,1/6),nrow=m)

# rozkłady brzegowe
px <- rowSums(pxy)
py <- colSums(pxy)
px
py
# wartości oczekiwane
ex<-sum(x*px)
ey<-sum(y*py)
ex2<-sum(x*x*px)
ey2<-sum(y*y*py)
# wariancje
varx<-ex2-ex^2
vary<-ey2-ey^2
# rozkład oraz wartości x,y w postaci wektorowej
(xv<-rep(x,times=n))
(yv<-rep(y,each=m))
(pv<-c(pxy))
# współczynnik korelacji
exy<-sum(pv*xv*yv)
covxy<-exy-ex*ey
(rhoxy<-covxy/(varx*vary)^0.5)
# rozkłady warunkowe y -pierwszy wiersz P(Y=y|X=0)
# drugi P(Y=y|X=1)
pyc<-array(0,dim=c(m,n))
# obliczanie rozkładów warunkowych zmiennej Y
for (i in 1:m){
  pyc[i,]<-pxy[i,]/px[i]
}
pyc
# sprawdzenie niezależności zmiennych X i Y, z definicji P(X=x∩Y=y)=P(X=x)⋅P(Y=y)
is_independent <- TRUE

for (i in 1:m) {
  for (j in 1:n) {
    if (pxy[i,j] != px[i] * py[j]) {
      is_independent <- FALSE
      break
    }
  }
}

is_independent
# wynik FALSE, więc zmienne nie są niezależne


# a

# generowanie pary (X,Y) za pomocą rozkładu łącznego
# p'stwa dla rozkładu łącznego, pv 
# liczba elementów w rozkładzie łącznym 
mn<-m*n
# p'stwa skumulowane
s<-array(dim=mn)
s[1]<-pv[1]
for (i in 2:mn){
  s[i]=s[i-1]+pv[i]
}
# realizacja
x_rea<-array(dim=1000)
y_rea<-array(dim=1000)
# 1000 realizacji z U[0,1]
r<-runif(1000)
# generowanie 1000 par realizacji
for (j in 1:1000){
  i<-1
  while (r[j]>s[i]){
    i<-i+1
  }
  x_rea[j]<-xv[i]
  y_rea[j]<-yv[i]
}
# macierz realizacji
mat_rea<-cbind(x_rea,y_rea)
# obliczanie tablicy rozdzielczej
tab<-table(x_rea,y_rea)
# normalizacja tablicy rozdzielczej
(tab_r<-tab/length(x_rea))
# współczynnik korelacji Pearsona
(r_p<-cor(x_rea,y_rea))
# współczynnik korelacji Spearmana
(r_s<-cor(x_rea,y_rea,method="spearman"))
# współczynnik korelacji Kendalla
(r_k<-cor(x_rea,y_rea,method="kendall"))

#b

# generowanie pary (X,Y) za pomocą rozkładów brzegowych
# p'stwa skumulowane dla zmiennej X
sx<-array(0,dim=m)
sx[1]<-px[1]
for (i in 2:m){
  sx[i]<-sx[i-1]+px[i]
}
# p'stwa skumulowane dla zmiennej Y przy danej X
sy<-array(0,dim=c(m,n))
sy[,1]<-pyc[,1]
for (j in 2:n){
  sy[,j]<-sy[,j-1]+pyc[,j]
}
sx
sy

N<-1000
# generowanie par realizacji
x_rea<-array(0,dim=N)
y_rea<-array(0,dim=N)
for (k in 1:N){
  # generowanie x
  u<-runif(1)
  ii<-1
  while (u>sx[ii]){
    ii<-ii+1    
  }
  x_rea[k]<-x[ii]
  # generowanie y z rozkładu warunkowego
  u<-runif(1)
  jj<-1
  while (u>sy[ii,jj]){
    jj<-jj+1
  }
  y_rea[k]<-y[jj]
}
mat_rea<-cbind(x_rea,y_rea)
# obliczanie tablicy rozdzielczej
tab<-table(x_rea,y_rea)
(tab_r<-tab/length(x_rea))
# obliczanie współczynników korelacji
(r_p<-cor(x_rea,y_rea))
(r_s<-cor(x_rea,y_rea,method="spearman"))
(r_k<-cor(x_rea,y_rea,method="kendall"))

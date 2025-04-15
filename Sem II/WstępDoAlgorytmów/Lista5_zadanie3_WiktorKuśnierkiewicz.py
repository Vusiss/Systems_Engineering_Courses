# a)

text1 = "konwalia"
text2 = "zawalina"

def get_the_longest_string(first_text,second_text):
    
    first_text = first_text.lower()
    second_text = second_text.lower()
    i = 0
    j = 0
    the_longest = ""
    
    # W pętlach funkcja sprawdza kolejno dla kazdej litery z pierwszego słowa czy nie rozpoczyna ciągu znaków znajdującego się w drugim ciągu. Zapamiętywany jest ten najdłuzszy
    
    while i < len(first_text):
        while j < len(second_text):
            actual = ""
            while j < len(second_text) and i < len(first_text) and first_text[i] == second_text[j]:
                actual+=first_text[i]
                if len(actual) > len(the_longest):
                    the_longest = actual
                i+=1
                j+=1
            i-=len(actual)
            j-=len(actual) - 1
             
        i+=1
        j=0
    return the_longest, len(the_longest)

the_longest_string, lenght = get_the_longest_string(text1,text2)

print(the_longest_string,lenght)

# b)

def get_the_longest_string_with_breaks(first_text,second_text):
    
    first_text = first_text.lower()
    second_text = second_text.lower()
    i = 0
    j = 0
    the_longest = ""

    while j < len(second_text):
        for k in range(i,len(first_text)):
            if second_text[j] == first_text[k]:
                the_longest += second_text[j]    
                i = k+1
                break
        j+=1  
    return the_longest, len(the_longest)

h = "ApabqBCrDseEF"
l = "tABuCvDEwxFyz"


the_string_with_breaks, lenght = get_the_longest_string_with_breaks(h,l)

print(the_string_with_breaks,lenght)

# d*)

import numpy as np

def LevenshteinDistance(base_string, another_string):
    m = len(base_string)
    n = len(another_string)
    d = np.zeros((m,n))
    
    for i in range(0, m):
       d[i, 0] = i
    for j in range(1 ,n):
       d[0, j] = j
    print(d)
    print("")
      
    for i in range(1, m):
        for j in range(1, n):
            if base_string[i] == another_string[j]: cost = 0
            else: cost = 1
            d[i, j] = min(d[i-1, j] + 1,        # usuwanie
                          d[i, j-1] + 1,        # wstawianie
                          d[i-1, j-1] + cost)   # zamiana
    
    print(d)
    
    return d[m-1, n-1]

print(LevenshteinDistance("marka","ariada"))
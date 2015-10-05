# -*- coding: utf-8 -*-

# Este tiene un error... arreglar en clase :v
lim = 10
primos = [1,2,3]
n = 4
while len(primos)<=lim:
    cnt = 0
    for p in primos:
        if n%p==0: 
            cnt += 1
    if cnt == 2: primos.append(n) 
    n += 1
print("Los primeros %d numeros primos son: "%(lim))
print(primos)

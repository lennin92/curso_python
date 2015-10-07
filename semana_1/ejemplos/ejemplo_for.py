# -*- coding: utf-8 -*-
"""
@author: lennin

Ejemplo ciclo for

plantilla
for elemento in iterable:
    # hacer algo con elemento
    pass
    
"""

CANTIDAD = 0

for VALOR in range(CANTIDAD):
    if VALOR%2==0: print("el valor %d es multiplo de 2"%(VALOR))
    elif VALOR%3==0: print("el valor %d es multiplo de 3"%(VALOR))
    elif VALOR%5==0: print("el valor %d es multiplo de 5"%(VALOR))
    else: print("el valor %d no es multiplo de 2, 3 ni 5"%(VALOR))

def listaPar():
    i = 0
    while True:
        if i%2==0:
            yield i
        i+=1

p = 0

for e in listaPar():
    print(e)
    p+=1
    if p==51: break

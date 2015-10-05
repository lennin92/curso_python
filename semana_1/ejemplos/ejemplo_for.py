# -*- coding: utf-8 -*-
"""
@author: lennin

Ejemplo ciclo for

plantilla
for elemento in iterable:
    # hacer algo con elemento
    pass
    
"""

CANTIDAD = 10

for VALOR in range(CANTIDAD):
    if VALOR%2==0: print("el valor %d es multiplo de 2"%(VALOR))
    elif VALOR%3==0: print("el valor %d es multiplo de 3"%(VALOR))
    elif VALOR%5==0: print("el valor %d es multiplo de 5"%(VALOR))
    else: print("el valor %d no es multiplo de 2, 3 ni 5"%(VALOR))
    
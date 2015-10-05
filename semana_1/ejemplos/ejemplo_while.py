# -*- coding: utf-8 -*-
"""
@author: lennin

Ejemplo ciclo while

while condicion:
    # accion a repetir
    pass
    
"""

from random import randint

while True: # este ciclo correra para siempre
    VALOR = randint(0,100)
    
    if VALOR%2==0:
        print("el valor %d es multiplo de 2"%(VALOR))
    elif VALOR%3==0:
        print("el valor %d es multiplo de 3"%(VALOR))
    elif VALOR%5==0:
        print("el valor %d es multiplo de 5"%(VALOR))
    else: 
        print("el valor %d no es multiplo de 2, 3 ni 5"%(VALOR))
        break # permite forzar cierre del ciclo

# -*- coding: utf-8 -*-

"""
@author: lennin

Ejemplo if-elif-else
plantilla

if condicion:
    # parte True
    pass
elif otra_condicion:
    # parte False para condiciones anteriores
    # pero True para la condicion actual
    pass
else:
    # parte False de todas las condiciones
    pass
"""

from random import randint

VALOR = randint(0,100)

if VALOR%2==0:
    print("el valor %d es multiplo de 2"%(VALOR))
elif VALOR%3==0:
    print("el valor %d es multiplo de 3"%(VALOR))
elif VALOR%5==0:
    print("el valor %d es multiplo de 5"%(VALOR))
else: 
    print("el valor %d no es multiplo de 2, 3 ni 5"%(VALOR))
    
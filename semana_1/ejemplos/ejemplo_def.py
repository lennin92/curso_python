# -*- coding: utf-8 -*-
"""
@author: lennin

Ejemplo def

def nombre_funcion(parametros):
    # hacer algo con los parametros y retornar algo (si es deseable)
    pass
    
"""

def es_multiplo(valor, multiplicidad):
    return valor%multiplicidad==0

def es_mult_2(valor):
    return es_multiplo(valor, 2)

def es_mult_3(valor):
    return es_multiplo(valor, 3)

def es_mult_5(valor):
    return es_multiplo(valor, 5)

from random import randint

VALOR = randint(0,100)

if es_mult_2(VALOR):
    print("el valor %d es multiplo de 2"%(VALOR))
elif es_mult_3(VALOR):
    print("el valor %d es multiplo de 3"%(VALOR))
elif es_mult_5(VALOR):
    print("el valor %d es multiplo de 5"%(VALOR))
else: 
    print("el valor %d no es multiplo de 2, 3 ni 5"%(VALOR))
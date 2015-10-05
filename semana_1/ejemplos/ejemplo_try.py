# -*- coding: utf-8 -*-
"""
@author: lennin

Ejemplo try

try:
    # hacer algo que pueda generar una excepcion
    pass
except TipoExcepcion as e:
    # hacer algo con la excepcion e
    pass
    
"""

try:
    a = 2562/0
    print(a)
except Exception as e:
    print("ERROR!")
    print(e)


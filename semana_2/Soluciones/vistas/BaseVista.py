# -*- coding: utf-8 -*-
"""
@author: lennin

Vista Base para heredar.

El objetivo es minimizar la programacion de la impresion de menus en cli
la vista que herede debe agregar una variable llamada menu
que debe ser un diccionario con el siguiente formato:

menu = {
    <id de la opcion del menu> : ("<Nombre de la opcion>", <otro diccionario 
                                del mismo formato o una funcion que resuelva>)
}

ejemplo:

menu = {
    1: ("OPCION 1": {
        1: ("SUBMENU 1.1" , {
            1: ("ACCION 1.1.1", funcion1),
            2: ("ACCION 1.1.2", funcion2)
        }) }),
    2 : ("OPCION 2": {
        1: ("SUBMENU 2.1" , {
            1: ("ACCION 2.1.1", funcion3),
            2: ("ACCION 2.1.2", funcion4)
        }),
        2: ("SUBMENU 2.2" , {
            1: ("ACCION 2.2.1", funcion5),
            2: ("ACCION 2.2.2", funcion6)
        }) ,
        3: ("SALIR" , sys.exit) 
    })
}

NOTAS: 
    * Se debe evitar sobreescribir el metodo __init__ puesto que a partir de este
    se genera las acciones para mostrar menus. En cualquier caso, si se necesita
    sobreescribir el metodo __init__ debera llamarse al finalizar la funcion sobreescrita
    con super.__init__().
    
    * Por ningun motivo sobreescribir el metodo __print

"""

import sys

if sys.version[0]=='2':
    input = raw_input
    
entrada = input
salir = sys.exit

from types import FunctionType as funct

class VistaBase:
    
    menu = {}
    
    def __init__(self):
        self.__print()
    
    
    def __print(self, __menu=None, __key=None):
        
        if __menu is None:
            self.__print(self.menu, __key)
               
        elif __key is None:
            for k in __menu:
                print("[%d] %s"%(k,__menu[k][0]))
            opt = int(input('Seleccione opcion: '))
            if opt not in __menu:
                print("Error en opcion digitada")
                self.__print(__menu, __key)
            else:
                self.__print(__menu, opt)
        else:
            value = __menu[__key][1]
            if type(value) is dict:
                self.__print(value)
            elif type(value) is funct:
                value()
                self.__print()

if __name__=="__main__":
    
        
    def f1():
        print("REALIZANDO OPERACIONES....")

    def s():
        sys.exit()
    
    class EjemploVista(VistaBase):
            
        menu = {
            1: ("EJEMPLO 1", {
                    1: ("EJEMPLO SUB MENU 1", f1),
                    2: ("SALIR", s)
                }),
            2: ("SALIR", s)
        }
    
    
    EjemploVista()

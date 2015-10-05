# -*- coding: utf-8 -*-
"""
@author: lennin

Ejemplo class

class NombreClase:
    atributo1 = 1
    atributo2 = 1

    def __init__(self, parametros):
        # constructor
        pass
    
    def metodo1(self, parametros):
        #hacer algo
        pass

"""

class Libro:
    titulo = None
    autor = None
    anio = None
    genero = None
    edicion = None
    editorial = None
    sinopsis = None
    
    def __init__(self, titulo, autor, editorial):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
    
    def __str__(self):
        s = "<Libro  titulo: %s, autor:%s, editorial %s>"
        return s % (self.titulo, self.autor, self.editorial)
        

l = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Alfaguara')
print(l)

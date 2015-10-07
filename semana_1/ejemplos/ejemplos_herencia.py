# -*- coding: utf-8 -*-

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print('(Persona: {})'.format(self.nombre))

    def tell(self):
        print('nombre:"{}" edad:"{}"'.format(self.nombre, self.edad))

class Docente(Persona):
    def __init__(self, nombre, edad, salario):
        Persona.__init__(self, nombre, edad)
        self.salario = salario
        print('(Docente: {})'.format(self.nombre))

    def tell(self):
        Persona.tell(self)
        print('salario: "{:d}"'.format(self.salario))

class Estudiante(Persona):
    '''Represents a Estudiante.'''
    def __init__(self, nombre, edad, promedio):
        Persona.__init__(self, nombre, edad)
        self.promedio = promedio
        print('(Estudiante: {})'.format(self.nombre))

    def tell(self):
        Persona.tell(self)
        print('promedio: "{:d}"'.format(self.promedio))

t = Docente('Mrs. Shrividya', 40, 30000)
s = Estudiante('Swaroop', 25, 75)


members = [t, s]
for member in members:
    # Works for both Docentes and Estudiantes
    member.tell()

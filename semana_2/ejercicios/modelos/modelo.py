# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:48:54 2015

@author: lennin
"""
import sqlite3

"""
    1-
    Completar la siguiente funcion se debe conectar a la base de datos 
    sqlite3 cuyo nombre es el parametro "base" y ejecutar la consulta 
    en "sql" debe retornar una lista con todos los valores si el parametro
    "cantidad" es None o la cantidad especificada en dicho parámetro.
    Ademas la consulta debera evitar la inyeccion de sql, permitiendo el 
    uso de consultas parametrizadas con los valores enviados en el parametro
    "valores"; si este es None la consulta se realizará unicamente usando "sql"
"""
def ejecutarSelect(sql, base, valores=None, cantidad=None):
    pass
    
"""
    2-
    Completar la siguiente funcion se debe conectar a la base de datos 
    sqlite3 cuyo nombre es el parametro "base" y ejecutar la consulta 
    en "sql".
    Ademas la consulta debera evitar la inyeccion de sql, permitiendo el 
    uso de consultas parametrizadas con los valores enviados en el parametro
    "valores"; si este es None la consulta se realizará unicamente usando "sql"
"""
def ejecutar(sql, base, valores=None):
    pass
    
    

class Modelo:
    __DB__='models.sqlite3'
    
    __metadata__={
        'tabla':'modelo',
        'atributos': [
            ('id', 'INTEGER'),
        ],
        'pk': ('id'),
    }
    
    """
        3-
        Completar la siguiente funcion, para que realize la consulta CREATE TABLE.
    """
    
    @classmethod
    def __create__(cls):
        if not('tabla' in cls.__metadata__ and
            'atributos' in cls.__metadata__ and
            'pk' in cls.__metadata__):
                raise Exception('diccionario __metadata__ malformado')
        create_string = """
            CREATE TABLE IF NOT EXISTS %(tabla)s (
                %(atributos)s,
                PRIMARY KEY (%(pk)s)
            );
        """%{
            'tabla' : cls.__metadata__['tabla'],
            'pk' : cls.__metadata__['pk'],
            'atributos': ", ".join([e[0]+" "+e[1] for e in cls.__metadata__['atributos']])
        }
        # COMPLETAR
    
    @classmethod
    def __tupla2object(cls, tupla):
        a = cls()
        for i in range(len(tupla)):
            setattr(a, cls.__metadata__['atributos'][i][0], tupla[i])
        return a
    
    
    @classmethod
    def getAll(cls):
        select_string = """
        SELECT %(atributos)s 
        FROM %(tabla)s
        """%{
            'tabla':cls.__metadata__['tabla'],
            'atributos': ', '.join([e[0] for e in cls.__metadata__['atributos']])
        }
        modelos = []
        for modelo_t in ejecutarSelect(select_string, cls.__DB__):
            modelos.append(cls.__tupla2object(modelo_t))
        return modelos
        
    @classmethod
    def getId(cls, oid):
        # COMPLETAR 
        pass
    
    def save(self):
        # COMPLETAR
        pass
        
    def del(self):
        # COMPLETAR
        pass
                

if __name__=="__main__":
    class ModeloPrueba(Modelo):
        __metadata__={
            'tabla':'modelo_prueba',
            'atributos': [
                ('id', 'INTEGER'),
                ('atributo1', 'VARCHAR(20)'),
                ('atributo2', 'FLOAT'),
                ('atributo3', 'TEXT'),
            ],
            'pk': ('id'),
        }
        
        def __repr__(self):
            return "<ModeloPrueba id:%d attr1: %s>"%(self.id, self.atributo1)
        
    print("VERSION DE SQLITE:")
    print(ejecutarSelect('SELECT SQLITE_VERSION()', 'db', cantidad=1))
    ModeloPrueba.__create__()
    print("SELECT ALL MODELOS:")
    print(ModeloPrueba.getAll())

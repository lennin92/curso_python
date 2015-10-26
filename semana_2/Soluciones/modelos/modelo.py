# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:48:54 2015

@author: lennin
"""
import sqlite3

def ejecutarSelect(sql, base, valores=None, cantidad=None):
    with sqlite3.connect(base) as cnn:
        cur = cnn.cursor()
        if valores is None:
            filas = cur.execute(sql)
        else:
            filas = cur.execute(sql, valores)
    if cantidad is None:
        return [r for r in filas]
    elif cantidad==1:
        return [r for r in filas][0]
    else:
        return [r for r in filas][:cantidad]

def ejecutar(sql, base, valores=None):
    with sqlite3.connect(base) as cnn:
        cur = cnn.cursor()
        if valores is None:
            cur.execute(sql)
        else:
            cur.execute(sql, valores)
        cnn.commit()
    
    

class Modelo:
    __DB__='models.sqlite3'
    
    __metadata__={
        'tabla':'modelo',
        'atributos': [
            ('id', 'INTEGER'),
        ],
        'pk': ('id'),
    }
    
    @classmethod
    def __create__(cls):
        if not('tabla' in cls.__metadata__ and
            'atributos' in cls.__metadata__ and
            'pk' in cls.__metadata__):
                raise Exception('diccionario __metadada__ malformado')
        create_string = """
            CREATE TABLE IF NOT EXISTS %(tabla)s (
                %(atributos)s,
                PRIMARY KEY (%(pk)s)
            );
        """%{
            'tabla' : cls.__metadata__['tabla'],
            'pk' : ', '.join([e for e in cls.__metadata__['pk']]),
            'atributos': ", ".join([e[0]+" "+e[1] for e in cls.__metadata__['atributos']])
        }
        ejecutar(create_string, cls.__DB__)
    
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
                
    def save(self):
        ins_str = """
            INSERT INTO %(tabla)s ( %(atributos)s )
                VALUES ( %(valores)s );
        """%{
            'tabla':self.__metadata__['tabla'],
            'atributos': ', '.join([e[0] for e in self.__metadata__['atributos']]),
            'valores':', '.join([str(getattr(self,e[0], "null")) for e in self.__metadata__['atributos']])
        }
        ejecutar(ins_str, self.__DB__)

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

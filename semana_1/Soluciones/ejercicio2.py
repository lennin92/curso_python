# -*- coding: utf-8 -*-

"""
    1 -
    Crear una funcion llamada obtener_cuentas, con un solo parametro 
    llamado "texto", esta funcion deberá retornar un diccionario, cuyas
    llaves seran cada palabra dentro de la variable "texto" y su valor 
    será el numero de veces que se repite esa palabra en "texto".
    Ejemplos:
        obtener_cuentas("diccionarios de python")={ "diccionarios":1, "de":1, "python":1 }
        obtener_cuentas("hola hola Hola")={ "hola":2, "Hola":1 }
    
    PD. Para simplificar las palabras se separarán solamente por espacios
    no se tomarán en cuenta signos de puntuacion
"""

def obtener_cuentas(texto):
    cuenta = {}
    palabras = texto.split(' ')
    for p in palabras:
        if p in cuenta: cuenta[p]  = cuenta[p] + 1
        else: cuenta[p] = 1
    return cuenta

assert obtener_cuentas("diccionarios de python")['de']==1
assert obtener_cuentas("hola hola Hola")['Hola']==1
assert obtener_cuentas("hola hola Hola")['hola']==2
print("PARTE 1 CORRECTA")

"""
    2-
    Crear una funcion llamada obtener_cuentas_archivo, cuyo unico parametro
    sea la direccion de un archivo de texto plano; esta funcion deberá obtener
    el mismo resultado que "obtener_cuentas" para el contenido del archivo
"""
def obtener_cuentas_archivo(direccion):
    with open(direccion, 'r') as archivo:
        contenido = archivo.read()
        return obtener_cuentas(contenido)


fc = obtener_cuentas_archivo('github_licencia.txt')
assert fc['permission']==2
assert fc['GitHub']==42
print("PARTE 2 CORRECTA")

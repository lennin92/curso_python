# -*- coding: utf-8 -*-

def contar_letra(cadena, letra, sensitivo=False):
    cnt = 0
    for char in cadena:
        if sensitivo:
            if char==letra: 
                cnt+=1
        else:
            if char.lower()==letra.lower(): 
                cnt+=1
    return cnt

def obtener_cuentas(texto):
    cuenta = {}
    palabras = texto.split(' ')
    for p in palabras:
        if p in cuenta: cuenta[p]  = cuenta[p] + 1
        else: cuenta[p] = 1
    return cuenta

def obtener_cuentas_archivo(direccion):
    with open(direccion, 'r') as archivo:
        contenido = archivo.read()
        return obtener_cuentas(contenido)

print(obtener_cuentas_archivo('github_licencia.txt'))

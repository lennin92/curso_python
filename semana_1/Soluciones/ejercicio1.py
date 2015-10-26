# -*- coding: utf-8 -*-

"""
    1 - 
    Modificar esta funcion para que cuente la cantidad de veces 
    que "letra" se repite en "cadena"; agregarle un parámetro 
    opcional llamado "sensitivo" con valor por defecto False; 
    cuando sensitivo=True deberá considerar las letras mayusculas
    diferentes a las minusculas; si sensitivo=False, las letras
    mayusculas se consideran iguales a las minusculas.
    Ejemplos:
        contar_letra("Im hunting high and low", 'i') = 3
        contar_letra("Im hunting high and low", 'i', True) = 2
        contar_letra("Im hunting high and low", 'i', False) = 3
"""
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
    
prb = "urllib.request module uses HTTP/1.1 and includes Connection:close header in its HTTP requests."
assert  contar_letra(prb, 'h')==3
assert  contar_letra(prb, 'h', True)==1
assert  contar_letra(prb, 'c', False)==4
assert  contar_letra(prb, 'c')==4
assert  contar_letra(prb, 'C', True)==1
print("PARTE 1 CORRECTA")


# Funcion auxiliar
cache={}
def descargar_texto(url):
    if url in cache: return cache[url]
    else:
        from urllib.request import urlopen as uget
        cache[url]=uget(url).read().decode('utf-8')
        return descargar_texto(url)

"""
    2 - 
    Modificar la siguiente funcion para que cuente la cantidad de veces
    que "letra" se repite en los cuerpos de las paginas web cuyas urls
    estan en la lista "urls", en este caso la cuenta no debe ser sensitiva     
"""

def cuenta_avanzada(urls, letra):
    cnt = 0
    for url in urls:
        cadena = descargar_texto(url)
        cnt+= contar_letra(cadena, letra)
    return cnt

prb_urls = [
    'http://www.python.org/',
    'http://www.example.com/',
    'http://www.asdf.com/'
]

assert cuenta_avanzada(prb_urls, 'a')==2099
assert cuenta_avanzada(prb_urls, 'b')==313
assert cuenta_avanzada(prb_urls, 'c')==1123
print("PARTE 2 CORRECTA")




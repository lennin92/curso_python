# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 04:29:48 2015

@author: lennin
"""

from urllib.request import urlopen as uget
from urllib import parse
import re, time

IMG_URL_REGEXS = "<img[A-Za-z0-9 /\-_\=@\"\']*src=\"(?P<url>[A-Za-z0-9\_\-./:;?=&%]*)\"[A-Za-z0-9 0/\-_\=\'\"]*[\/ ]*>"
AHR_URL_REGEXS = "<a[A-Za-z0-9 /\-_\=@\"\':,]*href=\"(?P<url>[A-Za-z0-9\_\-./:;,?=&%]*)\"[A-Za-z0-9 0/\-_\=\'\",:]*[\/ ]*>"

IMG_REGEX = re.compile(IMG_URL_REGEXS)
AHR_REGEX = re.compile(AHR_URL_REGEXS)

clnhtmr =re.compile('<.*?>')
clntxtr =re.compile('[,.;:\'\"\?¿!]+')
def html_sin_etiquetas(texto):
    cleantext = re.sub(clnhtmr, '', texto)
    cleantext = re.sub(clntxtr, ' ', cleantext)
    return cleantext
    
cache={}
def descargar_html(url):
    if url in cache: return cache[url]
    else:
        try:
            cache[url]=uget(url).read().decode('utf-8')
            return descargar_html(url)
        except Exception as e:
            print("ERROR AL DESCARGAR")            
            print(e)
            return ""

def corregir_url(padre, hijo):
    return parse.urljoin(padre,hijo)

def lista_patrones(cadena, c_regexp):
    return c_regexp.findall(cadena)

def lista_urls_pagina(html):
    return lista_patrones(html, AHR_REGEX)

def lista_urls_imagen(html):
    return lista_patrones(html, IMG_REGEX)

def lista_palabras(html):
    return html_sin_etiquetas(html).split()

def crawl(pagina_inicial, profundidad=3):
    visitados = []
    inicio = time.time()
    indice = {}
    cola = []
    cola.append((pagina_inicial, 0, ))
    print("Crawl iniciado ")
    while(len(cola)>0):
        t_actual = cola.pop(0)
        url_actual = t_actual[0]
        prof_actual = t_actual[1]
        if url_actual in visitados:
            continue
        visitados.append(url_actual)
        html_txt = descargar_html(url_actual)
        img_urls = [corregir_url(url_actual,l) for l in lista_urls_imagen(html_txt)]
        pgs_urls = [corregir_url(url_actual,l) for l in lista_urls_pagina(html_txt)]
        palabras = lista_palabras(html_txt)
        for p in palabras:
            if p not in indice:
                indice[p] = []
            indice[p] = indice[p]+[url for url in img_urls]
        if prof_actual<profundidad and len(cola+visitados)<10:
            for u in pgs_urls:
                if not( u in visitados):
                    cola.append((u,prof_actual+1,))
        print("CANTIDAD URL EN COLA %d"%(len(cola),))
    fin = time.time()
    print("Crawl finalizado %.2f"%(fin-inicio))
    return indice


if __name__=="__main__":
    p = "https://github.com/"
    indice = crawl(p)
    buscar = "carro"
    print('Imagenes relacionadas a %s'%('carro'))
    print(indice[buscar])

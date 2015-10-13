# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 04:29:48 2015

@author: lennin
"""

from urllib.request import urlopen as uget
from urllib import parse
import re

IMG_URL_REGEXS = "<img[A-Za-z0-9 0/\-_\=@\"\']*src=\"(?P<url>[A-Za-z0-9\_\-./:;?=&\"\']*)\"[A-Za-z0-9 0/\-_\=\'\"]*[\/ ]*>"
AHR_URL_REGEXS = "<a[A-Za-z0-9 0/\-_\=@\"\':,]*href=\"(?P<url>[A-Za-z0-9\_\-./:;,?=&\"\']*)\"[A-Za-z0-9 0/\-_\=\'\",:]*[\/ ]*>"

IMG_REGEX = re.compile(IMG_URL_REGEXS)
AHR_REGEX = re.compile(AHR_URL_REGEXS)

cache={}
def descargar_html(url):
    if url in cache: return cache[url]
    else:
        cache[url]=uget(url).read().decode('utf-8')
        return descargar_html(url)

def corregir_url(padre, hijo):
    return parse.urljoin(padre,hijo)

def lista_patrones(cadena, c_regexp):
    return c_regexp.findall(cadena)

def lista_urls_pagina(html):
    pass

def lista_urls_imagen(html):
    pass

def crawl(pagina_inicial, profundidad=3):
    pass


if __name__=="__main__":
    p = "https://github.com/"
    crawl(p)
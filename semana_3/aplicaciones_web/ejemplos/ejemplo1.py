#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import string,cgi,time
from os import curdir, sep
from http.server import BaseHTTPRequestHandler
import socketserver
from cgi import parse_header, parse_multipart

import sys

if sys.version[0]=='2':
    from urlparse import parse_qs
else:
    from urllib.parse import parse_qs

PORT = 8000
html = """
<html>
    <head><title>Mi App</title></head>
    <body>
        <h1>Mi primer aplicacion web</h1>
        <h2>Hola %(nombre)s!</h2>
        <form method="POST">
            <input name="nombre" />
            <input type="submit" />
        </form>
    </body>
</html>
"""
class Request:
    def __init__(self, Handler):
        headers = Handler.headers['content-type']
        if headers is None: headers=''
        ctype, pdict = parse_header(headers)
        if ctype == 'application/x-www-form-urlencoded':
            length = int(Handler.headers['content-length'])
            postvars = parse_qs(
                Handler.rfile.read(length),
                keep_blank_values=1)
        else:
            postvars = {}
        self.contentType = ctype
        self.params = pdict
        self.values = postvars

    def getParamValue(self, key, default=None):
        values = self.getParamValueList(key, default)
        if values is None:
            return ''
        else:
            return values[0]

    def getParamValueList(self, key, default=None):
        return self.values.get(key, None)

class BaseHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.request = Request(self)
        self.get()
    def do_POST(self):
        self.request = Request(self)
        self.post()

    def get(self):
        raise NotImplementedError
    def post(self):
        raise NotImplementedError


class PruebaHandler(BaseHandler):

    def get(self):
        self.send_response(200)
        self.send_header('Content-type',	'text/html')
        self.end_headers()
        data = html%{'nombre':''}
        self.wfile.write(bytes(data, "utf-8"))


    def post(self):
        self.send_response(200)
        self.send_header('Content-type',	'text/html')
        self.end_headers()
        data = html%{'nombre':self.request.getParamValue(b'nombre').decode(encoding='UTF-8')}
        self.wfile.write(bytes(data, "utf-8"))

if __name__=="__main__":
    httpd = socketserver.TCPServer(("", PORT), PruebaHandler)
    try:
        print("serving at port", PORT)
        httpd.serve_forever()
    except Exception as e:
        print(r'^C received, shutting down server')
        httpd.socket.close()

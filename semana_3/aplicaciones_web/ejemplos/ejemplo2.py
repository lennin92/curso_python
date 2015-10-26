#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from modelo import Modelo
from ejemplo1 import BaseHandler

HTML = """
<html>
    <head><title>Estudiantes</title></head>
    <body>
        <h1>Estudiantes</h1>
        <h2>Agregar Estudiante</h2>
        <form method="POST">
            <input name="carnet" />
            <input name="nombres" />
            <input name="apellidos" />
            <input name="carrera" />
            <input type="submit" />
        </form>
        <hr />
        <style>th,td{ border:1px solid black;}</style>
        <h2> Estudiantes </h2>
        <table>
            <tr><th>CARNET</th><th>NOMBRE</th><th>CARRERA</th></tr>
            %(estudiantes)s
        </table>
    </body>
</html>
"""

class Estudiante(Modelo):
        __metadata__={
            'tabla':'estudiante',
            'atributos': [
                ('carnet', 'VARCHAR(7)'),
                ('nombres', 'VARCHAR(25)'),
                ('apellidos', 'VARCHAR(25)'),
                ('carrera', 'VARCHAR(40)'),
            ],
            'pk': ['carnet'],
        }

def estudiante2htmlrow(e):
    return r"<tr><td>%s</td><td>%s</td><td>%s</td><tr>"%(
        e.carnet, e.nombres+" "+e.apellidos, e.carrera
    )

class EstudiantesHTTP(BaseHandler):
    def get(self):
        self.send_response(200)
        self.send_header('Content-type',	'text/html')
        self.end_headers()
        data = HTML%{'estudiantes':''.join([estudiante2htmlrow(e) for e in Estudiante.getAll()])}
        self.wfile.write(bytes(data, "utf-8"))

    def post(self):
        e = Estudiante()
        e.carnet = self.request.getParamValue(b'carnet').decode(encoding='UTF-8')
        e.nombres = self.request.getParamValue(b'nombres').decode(encoding='UTF-8')
        e.apellidos = self.request.getParamValue(b'apellidos').decode(encoding='UTF-8')
        e.carrera = self.request.getParamValue(b'carrera').decode(encoding='UTF-8')
        e.save()
        data = HTML%{'estudiantes':''.join([estudiante2htmlrow(e) for e in Estudiante.getAll()])}
        self.wfile.write(bytes(data, "utf-8"))

if __name__=="__main__":
    Estudiante.__create__()
    import socketserver
    _PORT = 8181
    httpd = socketserver.TCPServer(("", _PORT), EstudiantesHTTP)
    try:
        print("serving at port", _PORT)
        httpd.serve_forever()
    except Exception as e:
        print(r'^C received, shutting down server')
    httpd.socket.close()

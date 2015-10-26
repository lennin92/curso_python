# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 23:57:07 2015

@author: lennin-pc
"""
from modelo import Modelo

class Factura(Modelo):
        __metadata__={
            'tabla':'factura',
            'atributos': [
                ('id', 'INTEGER'),
                ('fecha', 'DATE')
            ],
            'pk': ('id',),
        }

class Producto(Modelo):
        __metadata__={
            'tabla':'producto',
            'atributos': [
                ('id', 'INTEGER'),
                ('nombre', 'VARCHAR(20)'),
                ('costo', 'FLOAT'),
                ('precioVenta', 'FLOAT'),
            ],
            'pk': ('id',),
        }

class DetalleFactura(Modelo):
        __metadata__={
            'tabla':'detalle_factura',
            'atributos': [
                ('id_factura', 'INTEGER'),
                ('id_producto', 'INTEGER'),
                ('cantidad', 'FLOAT'),
                ('precio_venta', 'FLOAT'),
            ],
            'pk': ('id_factura', 'id_producto'),
        }
    
Factura.__create__()
Producto.__create__()
DetalleFactura.__create__()
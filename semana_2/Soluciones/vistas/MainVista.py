# -*- coding: utf-8 -*-

from BaseVista import VistaBase, entrada, salir

def accion1():
    print("REALIZANDO ACCION 1")
    print("%d+%d=%d"%(2,3,2+3))

def accion2():
    print("REALIZANDO ACCION 2")
    print("%d/%d=%f"%(2,3,2/3))

class VistaMain(VistaBase):
    menu = {
        1: ("ACCION 1", accion1),
        2: ("ACCION 2", accion2),
        5: ("salir", salir)
    }
    
if __name__=="__main__":
    VistaMain()

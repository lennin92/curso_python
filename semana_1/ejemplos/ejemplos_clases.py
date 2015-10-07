# -*- coding: utf-8 -*-

class Robot:
    
    # Variable de clase (static)
    total = 0
    
    # (post constructor)
    def __init__(self, nombre):
        """Inicializa los datos del Robot."""
        self.nombre = nombre
        print("Inicializando %s"%(self.nombre))
        Robot.total += 1
    
    def saluda(self):
        print("Hola! mi nombre es %s"%(self.nombre))
    
    def muere(self):
        print("%s esta muriendo."%(self.nombre))
        Robot.total -= 1
        if Robot.total == 0:
            print("%s era el ultimo"%(self.nombre))
        else:
            print("Quedan %d robots"%(Robot.total))
            
    @classmethod
    def cuantos(cls):
        print("Quedan %d robots"%(cls.total))
    
    
droid1 = Robot("R2-D2")
droid1.saluda()
Robot.cuantos()

droid2 = Robot("C-3PO")
droid2.saluda()
Robot.cuantos()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.muere()
droid2.muere()

Robot.cuantos()

   

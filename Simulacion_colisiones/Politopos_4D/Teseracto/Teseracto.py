from vectores import Vector_dimension
from particulas import Particula_dimension
from random import randrange

class Simulacion:
    def __init__(self, size):
        self.size = size 
        self.bodies = []
    def add_body(self, body):
        self.bodies.append(body)
    
    def update_all(self):
        for body in self.bodies:
            body.move()
            body.collision_handler()

teseracto = Simulacion(100)
body = Particula_dimension(teseracto, 10,(0,0,0,0) ,velocity = (3.5,20,1.5,3.5))
with open('Convertidor_Texto_Partitura\teseracto.txt','w') as file:
    for _ in range(500):
        teseracto.update_all()
        for i in range(4):
            if body.position[i] == 100 or body.position[i] == 0 :
                file.write("%s\n" %(str(body.position)))
    
file.close()

        
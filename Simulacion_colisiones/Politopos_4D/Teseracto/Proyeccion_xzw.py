import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from matplotlib.patches import Polygon
from vectores import Vector
from particulas import Particula

class Simulacion:
    def __init__(self, size):
        self.size = size 
        self.bodies = []
        self.fig , self.ax = plt.subplots(
            1,
            1,
            subplot_kw={'projection': '3d'},
            figsize = (self.size / 15, self.size / 15),
        )
        self.fig.tight_layout()
        #self.ax.view_init(0 , 0)


    def add_body(self, body):
        self.bodies.append(body)
    
    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
            body.collision_handler()

        

    def draw_all(self):
        self.ax.set_xlim((0, self.size ))
        self.ax.set_ylim((0, self.size ))
        self.ax.set_zlim((0, self.size ))
        plt.pause(1/65)
        self.ax.clear()
    
    




cubo = Simulacion(100)


body = Particula(cubo, 10, (0,0,0,0) ,velocity = (3.5,1.5,3.5)) 
with open('Teseracto\cubo_proyeccion_xzw.txt','w') as file:
    for _ in range(500):
        cubo.update_all()
        cubo.draw_all()
        # Para cualquier parte del cubo
        #if body.position[0] == 100:
         #   file.write("%s\n" %(str('R ')+str(body.position))) #R de Right
        #if body.position[0] == 0 :
         #   file.write("%s\n" %(str('L ')+str(body.position))) #L de Left
        #if body.position[1] == 100:
         #   file.write("%s\n" %(str('B ')+str(body.position))) #B de Back
        #if body.position[1] == 0:
         #   file.write("%s\n" %(str('F ')+str(body.position))) #F de Front
        #if body.position[2] == 100:
         #   file.write("%s\n" %(str('U ')+str(body.position))) #U de Up
        #if body.position[2] == 0:
         #   file.write("%s\n" %(str('D ')+str(body.position))) #D de Down
        for i in range(3):
            if body.position[i] == 100 or body.position[i] == 0 :
                file.write("%s\n" %(str(body.position))) 
       
        # Pero notamos que los condicionales anteriores entran en conflicto
        # si toca una arista del cubo 
        # por lo que tenemos de dos
        # hacemos un condicional para que esos casos nos los detecte como un caso especial
        # o dejamos tal cual los condicionales y en el archivo al momento de convertirlo en sonido tomamos en cuenta esa observacion
file.close()            

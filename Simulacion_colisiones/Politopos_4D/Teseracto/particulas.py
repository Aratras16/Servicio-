import math
from vectores import Vector,Vector_dimension


class Particula:
    #Nos ayudararan con el tamaño de los marcadores en el grafico 3D
    min_display_size = 10
    display_log_base = 1.3 


    def __init__(
        self,
        sistema, # por sistema me refiero a algun tipo de simulacion 
        mass,
        position = (0,0,0),
        velocity = (0,0,0),
    ):
        self.sistema = sistema 
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size
            )
        self.colour = 'black'

        self.sistema.add_body(self)

    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],

        )
    
    def draw(self):
        self.sistema.ax.plot(
            *self.position,
            marker = 'o',
            markersize = self.display_size,
            color = self.colour     
        )
    def collision_handler(self):
         # EJE X
        if self.position[0] <= 0 or self.position[0] >= 100:
            self.velocity = (-self.velocity[0],self.velocity[1],self.velocity[2])
        # EJE Y 
        if self.position[1] <= 0 or self.position[1] >= 100:
            self.velocity = (self.velocity[0],-self.velocity[1],self.velocity[2])
            # EJE Z
        if self.position[2] <= 0 or self.position[2] >= 100:
            self.velocity = (self.velocity[0],self.velocity[1],-self.velocity[2])
        
           
        

class Particula_dimension:
    def __init__(
        self,
        sistema, # por sistema me refiero a algun tipo de simulacion 
        mass,
        position = (0,0,0,0),
        velocity = (0,0,0,0),
    ):
        self.sistema = sistema 
        self.mass = mass
        self.position = position
        self.velocity = Vector_dimension(*velocity)
        self.sistema.add_body(self)

    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],
            self.position[3] + self.velocity[3],

        )

    def collision_handler(self):
         # EJE X
        if self.position[0] <= 0 or self.position[0] >= 100:
            self.velocity = (-self.velocity[0],self.velocity[1],self.velocity[2],self.velocity[3])
        # EJE Y 
        if self.position[1] <= 0 or self.position[1] >= 100:
            self.velocity = (self.velocity[0],-self.velocity[1],self.velocity[2],self.velocity[3])
        # EJE Z
        if self.position[2] <= 0 or self.position[2] >= 100:
            self.velocity = (self.velocity[0],self.velocity[1],-self.velocity[2],self.velocity[3])
        # EJE W
        if self.position[3] <= 0 or self.position[3] >= 100:
            self.velocity = (self.velocity[0],self.velocity[1],self.velocity[2],-self.velocity[3])
        

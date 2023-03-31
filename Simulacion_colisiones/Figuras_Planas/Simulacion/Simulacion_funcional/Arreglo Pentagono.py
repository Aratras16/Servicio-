import pygame,math,pymunk
from random import randint
pygame.init()

display = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
space = pymunk.Space()
fps = 60
def coordenadas(coordenada):
    return float(coordenada[0]),700-float(coordenada[1])
class Particula():
    def __init__(self,x,y,collision_type):
        angle = randint(0, 359) #Elegimos un ángulo al azar
        coeff = 1500 #randint(200,1000)
        self.body = pymunk.Body()
        self.body.position = x,y
        self.body.velocity = (coeff*math.cos(angle*math.pi/180), coeff*math.sin(angle*math.pi/180))
        self.shape = pymunk.Circle(self.body,10)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.shape.collision_type = collision_type
        space.add(self.body,self.shape)
    def draw(self):
        pygame.draw.circle(display,(255,0,0),coordenadas(self.body.position),10)
colisiones = []
def collision_1(arbiter,space,data):
    colisiones.append(tuple('a') + tuple(arbiter.shapes[1].body.position/6))
def collision_2(arbiter,space,data):
    colisiones.append(tuple('b')+tuple(arbiter.shapes[1].body.position/6))
def collision_3(arbiter,space,data):
    colisiones.append(tuple('c')+tuple(arbiter.shapes[1].body.position/6))
def collision_4(arbiter,space,data):
    colisiones.append(tuple('d')+tuple(arbiter.shapes[1].body.position/6) )
def collision_5(arbiter,space,data):
    colisiones.append(tuple('e')+tuple(arbiter.shapes[1].body.position/6) )

def crear_segmento(pos1,pos2,collision_type):
	segment_body = pymunk.Body(body_type= pymunk.Body.STATIC)
	segment_shape = pymunk.Segment(segment_body,pos1,pos2,10)
	segment_shape.elasticity = 1
	segment_shape.collision_type = collision_type
	space.add(segment_body,segment_shape)
vertice1 = (300,0)
vertice2 = (14.68,600-392.70)
vertice3 = (123.66,600-57.29)
vertice4 = (585.31,600-392.7)
vertice5 = (476.33,600-57.7)
segmento1 = crear_segmento(vertice1,vertice2,6)
segmento2 = crear_segmento(vertice1,vertice4,6)
segmento3 = crear_segmento(vertice2,vertice3,6)
segmento4 = crear_segmento(vertice4,vertice5,6)
segmento5 = crear_segmento(vertice3,vertice5,6)

def Simulacion():
    particula = Particula(350,100,5)
    a = space.add_collision_handler(1,6)
    a.separate = collision_1

    b = space.add_collision_handler(3,6)
    b.separate = collision_3

    c = space.add_collision_handler(2,6)
    c.separate = collision_2

    d = space.add_collision_handler(4,6)
    d.separate = collision_4

    e = space.add_collision_handler(4,6)
    e.separate = collision_5
    while True:
        with open('Sonorizacion\particula_pentagono.txt', 'w') as f:
            for i in colisiones:
                f.write("%s\n" %str(i))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255,255,255))
        particula.draw()
        pygame.draw.line(display,(0,0,0),vertice1,vertice2,10)
        pygame.draw.line(display,(0,0,0),vertice1,vertice4,10)
        pygame.draw.line(display,(0,0,0),vertice2,vertice3,10)
        pygame.draw.line(display,(0,0,0),vertice4,vertice5,10)
        pygame.draw.line(display,(0,0,0),vertice3,vertice5,10)
        pygame.display.update()
        clock.tick(fps)
        space.step(1/fps)
        

Simulacion()
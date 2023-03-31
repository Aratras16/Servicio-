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
        coeff = 1200  #randint(200,1000)
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
def collision_3(arbiter,space,data):
    colisiones.append(tuple('u') + tuple(arbiter.shapes[1].body.position/6.5))
    #print('arriba '+ str(arbiter.shapes[1].body.position))
def collision_1(arbiter,space,data):
    colisiones.append(tuple('d') + tuple(arbiter.shapes[1].body.position/6.5))
    #print('abajo ' + str(arbiter.shapes[1].body.position))
def collision_2(arbiter,space,data):
    colisiones.append(tuple('r') + tuple(arbiter.shapes[1].body.position/6.5))
    #print('derecha ' + str(arbiter.shapes[1].body.position) )
def collision_4(arbiter,space,data):
    colisiones.append(tuple('l') + tuple(arbiter.shapes[1].body.position/6.5))
    #print('izquierda ' + str(arbiter.shapes[1].body.position))

def crear_segmento(pos1,pos2,collision_type):
	segment_body = pymunk.Body(body_type= pymunk.Body.STATIC)
	segment_shape = pymunk.Segment(segment_body,pos1,pos2,10)
	segment_shape.elasticity = 1
	segment_shape.collision_type = collision_type
	space.add(segment_body,segment_shape)
pos_tl = (50,50)
pos_tr = (650,50)
pos_bl = (50,650)
pos_br = (650,650)
segmento1 = crear_segmento(pos_tl,pos_tr,1)
segmento2 = crear_segmento(pos_tr,pos_br,2)
segmento3 = crear_segmento(pos_br,pos_bl,3)
segmento4 = crear_segmento(pos_bl,pos_tl,4)

def Simulacion():
    particula = Particula(350,350,5)
    pared_inferior = space.add_collision_handler(1,5)
    pared_inferior.separate = collision_1

    pared_superior = space.add_collision_handler(3,5)
    pared_superior.separate = collision_3

    pared_derecha = space.add_collision_handler(2,5)
    pared_derecha.separate = collision_2

    pared_izquierda = space.add_collision_handler(4,5)
    pared_izquierda.separate = collision_4
    while True:
        with open('Sonorizacion\particula_cuadrado.txt', 'w') as f:
           for i in colisiones:
            
            f.write("%s\n" %str(i))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255,255,255))
        particula.draw()
        pygame.draw.line(display,(0,0,0),pos_tl,pos_tr,5)
        pygame.draw.line(display,(0,0,0),pos_tr,pos_br,5)
        pygame.draw.line(display,(0,0,0),pos_br,pos_bl,5)
        pygame.draw.line(display,(0,0,0),pos_bl,pos_tl,5)
        pygame.display.update()
        clock.tick(fps)
        space.step(1/fps)
        

Simulacion()
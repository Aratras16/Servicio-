import pygame,pymunk,math
from random import randint

# Creamos nuestra clase particula
class Particula():
	# Inicializamos la particula
	def __init__(self, x, y, size):
		self.size=size
		mass=self.size**2 #Con estos valores trabaja bien 
		self.color=(randint(0, 255), randint(0, 255), randint(0, 255)) #colores al azar
		angle=randint(0, 359) #Elegimos un ángulo al azar
		coeff=40000/mass
		self.body=pymunk.Body(mass)
		self.body.position=(x, y)
		self.body.velocity=(coeff*math.cos(angle*math.pi/180), coeff*math.sin(angle*math.pi/180))
		self.shape=pymunk.Circle(self.body, self.size)
		self.shape.elasticity=1 # La elasticidad nos dice que tanto rebota una particula (el valor de 1 nos dice que es completamente elastica)
		self.shape.density = 1

	
		space.add(self.body, self.shape)
	#Ahora vamos a definir una funcion que nos dibuje la particula
	def draw(self):
		x=int(self.body.position.x)
		y=int(self.body.position.y)
		pygame.draw.circle(pantalla, self.color, (x,y), self.size)

#Definimos una funcion para crear los margenes para que las particulas no se salgan

def crear_segmento(pos1,pos2):
	segment_body = pymunk.Body(body_type= pymunk.Body.STATIC)
	segment_shape = pymunk.Segment(segment_body,pos1,pos2,10)
	segment_shape.elasticity = 1
	segment_shape.collision_type = 2
	space.add(segment_body,segment_shape)


pygame.init()

#Pantalla 
pantalla = pygame.display.set_mode((700,700))
#Reloj (para animar los frames a futuro)
reloj = pygame.time.Clock()
# Creamos un espacio para la simulacion con ayuda de la libreria Pymunk

space = pymunk.Space()


#Declararemos algunas constantes que nos seran utiles mas adelante
fps = 50
blanco = (255,255,255)
negro = (0,0,0)
Conteo = []
#Creamos unas particulas
particulas = [Particula(350,350,10) for i in range(2)]
		
#Creamos los margenes
pos_tl = (50,50)
pos_tr = (650,50)
pos_bl = (50,650)
pos_br = (650,650)
segmento1 = crear_segmento(pos_tl,pos_tr)
segmento2 = crear_segmento(pos_tr,pos_br)
segmento3 = crear_segmento(pos_br,pos_bl)
segmento4 = crear_segmento(pos_bl,pos_tl)

#Vamos a  iniciar la pantalla 
ejecucion =  True 
while ejecucion:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ejecucion = False

	pantalla.fill(blanco)
	[particula.draw() for particula in particulas]
	pygame.draw.line(pantalla,negro,pos_tl,pos_tr,5)
	pygame.draw.line(pantalla,negro,pos_tr,pos_br,5)
	pygame.draw.line(pantalla,negro,pos_br,pos_bl,5)
	pygame.draw.line(pantalla,negro,pos_bl,pos_tl,5)
	pygame.display.flip()
	reloj.tick(fps)
	space.step(1/fps) #Actualiza el espacio de simulacion.
	#Con lo siguiente registramos las coordenadas de todas las bolas
	with open('Sonorizacion\particula_cuadrado.txt', 'w') as f:
		for particula in particulas:
				f.write("%s\n" %str(tuple(particula.body.position/6)))
	

f.close()

pygame.quit()

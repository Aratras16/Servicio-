import pygame,pymunk,math
from random import randint

# Creamos nuestra clase particula
class Particula():
	# Inicializamos la particula
	def __init__(self,x,y,size):
		self.size = size
		masa = self.size**2 #Con estos valores trabaja bien 
		self.color = (randint(0,255),randint(0,255),randint(0,255)) #No se me ocurrieron colores 
		angulo = randint(0,359) #Elegimos un ángulo al azar
		coeficiente = 40000/masa 
		self.body = pymunk.Body(masa)
		self.body.position = (x, y)
		self.body.velocity = (coeficiente*math.cos(angulo*math.pi/180),coeficiente*math.sin(angulo*math.pi/180))
		self.shape = pymunk.Circle(self.body,self.size)
		self.shape.elasticity = 1 # La elasticidad nos dice que tanto rebota una particula (el valor de 1 nos dice que es completamente elastica)
		self.shape.density = 1
		espacio.add(self.body,self.shape)
	#Ahora vamos a definir una funcion que nos dibuje la particula
	def dibujo(self):
		x = int(self.body.position.x)
		y = int(self.body.position.y)
		pygame.draw.circle(pantalla,self.color,(x,y),self.size)

#Definimos una funcion para crear los margenes para que las particulas no se salgan

def crear_segmento(pos1,pos2):
	segment_body = pymunk.Body(body_type= pymunk.Body.STATIC)
	segment_shape = pymunk.Segment(segment_body,pos1,pos2,10)
	segment_shape.elasticity = 1
	espacio.add(segment_body,segment_shape)




pygame.init()

#Pantalla 
pantalla = pygame.display.set_mode((600,600))
#Reloj (para animar los frames a futuro)
reloj = pygame.time.Clock()
# Creamos un espacio para la simulacion con ayuda de la libreria Pymunk

espacio = pymunk.Space()

#Declararemos algunas constantes que nos seran utiles mas adelante
fps = 50
blanco = (255,255,255)
negro = (0,0,0)

#Creamos unas particulas
# particulas = [Particula(randint(0,600),randint(0,600),10) for i in range(300)]
particulas = [Particula(300,300,10) for i in range(300)]


#Creamos los margenes
vertice1 = (300,0)
vertice2 = (14.68,600-392.70)
vertice3 = (123.66,600-57.29)
vertice4 = (585.31,600-392.7)
vertice5 = (476.33,600-57.7)
segmento1 = crear_segmento(vertice1,vertice2)
segmento2 = crear_segmento(vertice1,vertice4)
segmento3 = crear_segmento(vertice2,vertice3)
segmento4 = crear_segmento(vertice4,vertice5)
segmento5 = crear_segmento(vertice3,vertice5)

#Vamos a  iniciar la pantalla 
ejecucion =  True 
while ejecucion:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ejecucion = False

	pantalla.fill(blanco)
	[particula.dibujo() for particula in particulas]
	pygame.draw.line(pantalla,negro,vertice1,vertice2,10)
	pygame.draw.line(pantalla,negro,vertice1,vertice4,10)
	pygame.draw.line(pantalla,negro,vertice2,vertice3,10)
	pygame.draw.line(pantalla,negro,vertice4,vertice5,10)
	pygame.draw.line(pantalla,negro,vertice3,vertice5,10)
	pygame.display.flip()
	reloj.tick(fps)
	espacio.step(1/fps) #Actualiza el espacio de simulacion.
	with open('Sonorizacion\particula_pentagono.txt', 'w') as f:
		for particula in particulas:
			f.write("%s\n" %str(tuple(particula.body.position/6)))
	

f.close()

pygame.quit()

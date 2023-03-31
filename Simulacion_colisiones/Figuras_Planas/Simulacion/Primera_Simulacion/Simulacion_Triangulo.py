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
		self.shape.collision_type = 4
		space.add(self.body,self.shape)
	#Ahora vamos a definir una funcion que nos dibuje la particula
	def draw(self):
		x = int(self.body.position.x)
		y = int(self.body.position.y)
		pygame.draw.circle(pantalla,self.color,(x,y),self.size)

#Definimos una funcion para crear los margenes para que las particulas no se salgan

def crear_segmento(pos1,pos2):
	segment_body = pymunk.Body(body_type= pymunk.Body.STATIC)
	segment_shape = pymunk.Segment(segment_body,pos1,pos2,10)
	segment_shape.elasticity = 1
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

#Creamos unas particulas
# particulas = [Particula(randint(0,600),randint(0,600),10) for i in range(300)]
particula = Particula(300,300,10)


#Creamos los margenes
pos_ar = (350,80)
pos_abi = (50,600)
pos_abd= (650,600)
segmento1 = crear_segmento(pos_abi,pos_abd)
segmento2 = crear_segmento(pos_ar,pos_abd)
segmento3 = crear_segmento(pos_ar,pos_abi)

colisiones = []
def collision_3(arbiter,space,data):
    print(arbiter.shapes[1].body.position)
def collision_1(arbiter,space,data):
    print(arbiter.shapes[1].body.position)
def collision_2(arbiter,space,data):
    print(arbiter.shapes[1].body.position)

#Vamos a  iniciar la pantalla 
ejecucion =  True 
abajo = space.add_collision_handler(1,4)
abajo.separate = collision_1

derecha = space.add_collision_handler(3,4)
derecha.separate = collision_3

izquierda = space.add_collision_handler(2,4)
izquierda.separate = collision_2
while ejecucion:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ejecucion = False
	
	pantalla.fill(blanco)
	particula.draw()
	pygame.draw.line(pantalla,negro,pos_abi,pos_abd,10)
	pygame.draw.line(pantalla,negro,pos_ar,pos_abi,10)
	pygame.draw.line(pantalla,negro,pos_ar,pos_abd,10)
	pygame.display.flip()
	reloj.tick(fps)
	space.step(1/fps) #Actualiza el espacio de simulacion.
	#with open('Sonorizacion\particula_triangulo.txt', 'w') as f:
	#	for particula in particulas:
	#		f.write("%s\n" %str(tuple(particula.body.position/6)))
	

#f.close()


pygame.quit()

#   Vamos a hacer que suene de la siguiente forma
#   Primero vamos a asignarle a cada eje coordenado un aspecto del sonido
#   Al eje X le vamos a asignar el panning
#   Al eje Y le asignaremos el pitch
#   Al eje Z le asignaremos el amplitude
#   Por como se definen cada uno de los aspectos y para que suene bonito vamos a mapear nuestros ejes como sigue
#   El panning va de -1 a 1 Por lo que cada punto del eje x lo transformamos a un punto de la recta [-1,1] con la ecuacion f(x) = -1 + x/50
#   El pitch puede ir desde 0 a cualquier numero que querramos, por ello nuestro eje Y ira de 0 a 20 (si no duelen los oidos )
#   El amplitude puede ir desde 0 hasta cualquier numero, pero en 0 no se escucha asi que pondremos de 1 a 101 asi cada punto en el eje Z debemos sumarle una unidad  

with open('Cubo\Simulacion\cubo.txt') as file:
    with open('Cubo\Sonorizacion\sonido_cubo.rb','w') as f:
        for line in file:
            vector = tuple(eval(line))
            f.write('play ' + str(50) + ' , ' + 'pan: {}, pitch: {} , amp: {} \n'.format((-1+vector[0]/50) , vector[1]/5,vector[2]+1))
            #   Aqui tengo dos opciones puedo dejar una sola nota por ejemplo 50 y esta va a sonar distinto dependiendo en donde impacte 
            #   pues definimos a los ejes como aspectos del sonido por lo que asi escuchariamos una misma nota pero variada
            #   La otra opcion es dar una nota por cada coordenada del punto en el que colisiona y 
            #f.write('play ' + str(vector[0]) + ' , ' + 'pan: {}, pitch: {} , amp: {} \n'.format((-1+vector[0]/50) , vector[1],vector[2]+1))
            #f.write('play ' + str(vector[1]) + ' , ' + 'pan: {}, pitch: {} , amp: {} \n'.format((-1+vector[0]/50) , vector[1],vector[2]+1))
            #f.write('play ' + str(vector[2]) + ' , ' + 'pan: {}, pitch: {} , amp: {} \n'.format((-1+vector[0]/50) , vector[1],vector[2]+1))
            f.write('sleep {} \n'.format(1))
    f.close()  
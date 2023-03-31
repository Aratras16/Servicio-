def separa(archivo,nombre):
    with open(archivo) as file:
        with open(nombre, 'w') as f:
            for line in file:
                coma =line.replace(', ',' ')
                parentesis = coma.replace('(','')
                semi = parentesis.replace(')','')
                arriba = semi.replace("'u'",'use_synth:bass_foundation')
                abajo = arriba.replace("'d'",'use_synth:supersaw')
                derecha = abajo.replace("'r'",'use_synth:square')
                izquierda = derecha.replace("'l'",'use_synth:mod_pulse')
                f.write(semi)
        f.close()


def Partitura(archivo,nombre,final,espera,sintetizador = ''):
    separa(archivo,nombre)
    contador = 0
    if sintetizador == '':
        with open(nombre) as file:
            with open(final,'w') as f:
                for line in file:
                    if contador%3 == 0:
                        f.write(line)
                    else:     
                        f.write('play ' + line)
                    
                    if contador%3 == 2:
                        f.write('sleep {} \n'.format(espera))
                    contador += 1
            f.close()
    else:
        with open(nombre) as file:
            with open(final,'w') as f:
                f.write('use_synth {} \n'.format(sintetizador))

                for line in file:
                    if contador%3 == 0:
                        f.write(line)
                    else:     
                        f.write('play ' + line)
                    if contador%3 == 2:
                        f.write('sleep {} \n'.format(espera)) 
                    contador += 1
            f.close()
#Partitura('particula_cuadrado.txt',"cuadrado.txt",'prueba.txt',0.5)
#Partitura('particula_triangulo.txt',"triangulo.txt",'particulatriangulo.txt',0.5)
#Partitura('particula_pentagono.txt',"pentagono.txt",'particula_pentagono.rb',0.5)
Partitura('particula_cuadrado.txt','cuadrado.txt','llll.txt',0.5)

        
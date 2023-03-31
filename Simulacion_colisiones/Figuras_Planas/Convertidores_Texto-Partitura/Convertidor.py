def Sonido(figura,archivo,final,tiempo):
    with open(archivo) as file:
        lista = []
        with open(final,'w') as f:
            if figura == 'cuadrado':
                for line in file:
                    linea = line.replace('\n','')
                    lista.append(eval(linea))
                for i in lista:
                    if i[0] == 'l':
                        f.write('play ' + str(i[1]) + ' , ' + 'pan: -1' + ', pitch: {} \n'.format(i[2]/5))
                        f.write('play ' + str(i[2]) + ' , ' + 'pan: -1' + ', pitch: {} \n'.format(i[2]/5))
                        f.write('sleep {} \n'.format(tiempo))
                    if i[0] == 'r':
                        f.write('play ' + str(i[1]) + ' , ' + 'pan: 1' + ', pitch: {} \n'.format(i[2]/5))
                        f.write('play ' + str(i[2]) + ' , ' + 'pan: 1' + ', pitch: {} \n'.format(i[2]/5))
                        f.write('sleep {} \n'.format(tiempo))

                    if i[0] == 'u':
                        f.write('play ' + str(i[1]) + ' , ' + 'pitch: 20 ' + ', pan: {} \n'.format(-1+(i[2]/50)))
                        f.write('play ' + str(i[2]) + ' , ' + 'pitch: 20' + ', pan: {} \n'.format(-1+(i[2]/50)))
                        f.write('sleep {} \n'.format(tiempo))

                    if i[0] == 'd':
                        f.write('play ' + str(i[1]) + ' , ' + 'pitch: 0 ' + ', pan: {} \n'.format(-1+(i[2]/50)))
                        f.write('play ' + str(i[2]) + ' , ' + 'pitch: 0' + ', pan: {} \n'.format(-1+(i[2]/50)))
                        f.write('sleep {} \n'.format(tiempo))              
            if figura == 'triangulo':
                for line in file:
                    linea = line.replace('\n','')
                    lista.append(eval(linea))
                for i in lista:
                    if i[0] == 'l':
                        f.write('play ' + str(i[1]) + ' , ' + 'pan: -1' + ', pitch: {} \n'.format(i[2]/5))
                        f.write('play ' + str(i[2]) + ' , ' + 'pan: -1' + ', pitch: {} \n'.format(i[2]/5))
                        f.write('sleep {} \n'.format(tiempo))
                    if i[0] == 'r':
                        f.write('play ' + str(i[1]) + ' , ' + 'pan: 1' + ', pitch: {} \n'.format(i[2]/5))
                        f.write('play ' + str(i[2]) + ' , ' + 'pan: 1' + ', pitch: {} \n'.format(i[2]/5))
                        f.write('sleep {} \n'.format(tiempo))
                    if i[0] == 'd':
                        f.write('play ' + str(i[1]) + ' , ' + 'pitch: 0 ' + ', pan: {} \n'.format(-1+(i[2]/50)))
                        f.write('play ' + str(i[2]) + ' , ' + 'pitch: 0' + ', pan: {} \n'.format(-1+(i[2]/50)))
                        f.write('sleep {} \n'.format(tiempo))      


        f.close()       
    file.close()

Sonido('cuadrado','Sonorizacion\particula_cuadrado.txt','Sonorizacion\sonido_cuadrado.rb',1)
Sonido('triangulo','Sonorizacion\particula_triangulo.txt','Sonorizacion\sonido_triangulo.rb',1)



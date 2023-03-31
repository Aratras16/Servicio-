def proyeccion (archivo,resultado,ejes = (1,1,1,0),):
    with open(archivo) as file:
        with open(resultado,'w') as f:
            for line in file:
                vector = tuple(eval(line))
                if ejes == (1,1,1,0):
                    f.write(str(vector[0:3])+'\n')
                if ejes == (0,1,1,1):
                    f.write(str(vector[1:4])+'\n') 
                if ejes == (1,0,1,1):
                    f.write(str((vector[0],vector[2],vector[3]))+'\n') 
                if ejes == (1,1,0,1):
                    f.write(str((vector[0],vector[1],vector[3]))+'\n')                 

proyeccion('Convertidor_Texto_Partitura\teseracto.txt','Teseracto\proyeccion_ejes_xyz.txt')
proyeccion('Convertidor_Texto_Partitura\teseracto.txt','Teseracto\proyeccion_ejes_yzw.txt',(0,1,1,1))
proyeccion('Convertidor_Texto_Partitura\teseracto.txt','Teseracto\proyeccion_ejes_xzw.txt',(1,0,1,1))
proyeccion('Convertidor_Texto_Partitura\teseracto.txt','Teseracto\proyeccion_ejes_xyw.txt',(1,1,0,1))

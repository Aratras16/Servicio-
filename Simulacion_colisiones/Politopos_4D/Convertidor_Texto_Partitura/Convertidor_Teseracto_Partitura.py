with open('Convertidor_Texto_Partitura\teseracto.txt') as file:
    with open('Sonorizacion\sonido_3d.rb','w') as f:
        with open('Sonorizacion\sonido_4d.rb','w') as g:
            for line in file:
                vector = tuple(eval(line))
                f.write('play ' + str(50) + ' , ' + 'pan: {}, pitch: {} , amp: {} \n'.format((-1+vector[0]/50) , vector[1]/5,vector[2]+1))
                f.write('sleep {} \n'.format(1))
                g.write('play {}, release: 0.1, cutoff: rrand(65,70) \n'.format(vector[3]))
                g.write('sleep {} \n'.format(1))
    
        g.close() 
    f.close()
    

            
      
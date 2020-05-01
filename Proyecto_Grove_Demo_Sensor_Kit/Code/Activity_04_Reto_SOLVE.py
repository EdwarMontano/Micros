#Actividad Reto Medir EStatura
from grovepi import *
import grovepi
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import numpy as np

potenciometro= 2
ultrasonic_ranger = 7

Medida=[]
offset=[]

setRGB(10,10,10)

while True:
    try:
        
        for i in range(10):
            #print(i)
            distancia= ultrasonicRead(ultrasonic_ranger)
            Medida.append(distancia)
            Lectura_Pot=grovepi.analogRead(potenciometro)
            offset.append(Lectura_Pot)
            #sleep(0.005)
            
        vector_med=np.array(Medida)
        pro_estatura=np.around(np.mean(vector_med),2)
        vector_offset=np.array(offset)
        pro_offset=np.around(np.mean(vector_offset)/100,2)
        ajuste=np.around(pro_estatura+pro_offset,1)
        
        
        #print(pro_estatura,'cm', " ,offset: ", pro_offset)
        print(ajuste,'cm', " ,offset: ", pro_offset,"*****") 
        d = str(pro_estatura)
               
        
        setText("dis:" + d + "cm\n"+ "offset:"+str(pro_offset)+ "cm\n")

    except (IOError, TypeError) as e:
        print(str(e))        
        setText("")

    except KeyboardInterrupt as e:
        print(str(e))
        setText("")
        break

    
    
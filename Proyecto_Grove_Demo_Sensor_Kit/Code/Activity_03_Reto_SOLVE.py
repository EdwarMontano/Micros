import time
import grovepi
import math
from grovepi import *
import numpy as np 
import matplotlib.pyplot as plt

# Connections
sound_sensor = 1        # port A1
led_Rojo= 2                 # port D2
led_Verde= 3                # port D3

grovepi.pinMode(led_Rojo,"OUTPUT")
grovepi.pinMode(led_Verde,"OUTPUT")

print("Actividad 3 RETO")
Fs=44100
son=[]
print(son)

def nivelaudio(promedio):
    if promedio<341:
        print("ambiente silencioso")
    elif promedio<682:
        print("ambiente ruido moderado")
    else:
        print("ambiente ruido alto")

while True:
    
    try:
        while True:
            try:
                muestras=int(input("Digite el número de muestras: ").replace(" ",""))
                break
            except ValueError:
                print("Por favor ingrese un valor entero")
        #print(type(muestras))
        digitalWrite(led_Rojo,1) 
        for i in range(muestras):
            #print(i)
            sonido= grovepi.analogRead(sound_sensor)
            print(type(sonido))
            son.append(sonido)  
        digitalWrite(led_Rojo,0)
        
        print(son)
        
        vector=np.array(son)
        promedio=np.mean(vector)
        print(promedio)
        nivelaudio(promedio)
        
        plt.stem(son)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(linewidth=8, color='#d62728')
        plt.axhline(y=341)
        plt.axhline(linewidth=10, color='#ff0000')
        plt.axhline(y=682)
        
        plt.title('Actividad 3')
        plt.show()
        
    
        break
    except IOError:
        print("Error")
    except KeyboardInterrupt:
        exit()
    

    
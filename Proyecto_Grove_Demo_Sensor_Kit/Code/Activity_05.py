import time
import grovepi
import math
from grove_rgb_lcd import *

# Connections
sound_sensor = 1        # port A1
light_sensor = 0        # port A0
potenciometro = 2       # port A2
temperature_sensor = 8  # port D8
led_R= 2                 # port D2
led_G = 3                 # port D3

grovepi.pinMode(led_R,"OUTPUT")
grovepi.pinMode(led_G,"OUTPUT")


print("Actividad 5") 

def nivelaudio(promedio):
    if promedio<341:
        print("ambiente silencioso")
        setRGB(50,150,255)
    elif promedio<682:
        print("ambiente ruido moderado")
        setRGB(0,255,0)
    else:
        print("ambiente ruido alto")
        setRGB(255,10,10)
        
while True:
    
    try:
        # Obtener el Valor del sensor de Luz
        light_intensity = grovepi.analogRead(light_sensor)
        Lectura_Pot=grovepi.analogRead(potenciometro)
        # Give PWM output to LED
        grovepi.analogWrite(led_R,light_intensity)
        grovepi.analogWrite(led_G,Lectura_Pot)
        # GObtener Valor del sensor de sonido 
        sound_level = grovepi.analogRead(sound_sensor)
        
        nivelaudio(sound_level)

        #time.sleep(0.5)

        # Get value from temperature sensor
        [t,h]=[0,0]
        [t,h] = grovepi.dht(temperature_sensor,0)
        

        # Post a tweet
        out_str ="T: %d C, H: %d, L: %d, S: %d" %(t,h,light_intensity/10,sound_level)
        print(out_str)
        d = str(out_str)
               
        
        setText(d)
        
    except IOError:
        print("Error")
    except KeyboardInterrupt:
        exit()
    

    time.sleep(1) 
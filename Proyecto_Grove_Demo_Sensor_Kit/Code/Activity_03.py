
import time
import grovepi
import math

# Connections
sound_sensor = 1        # port A1
light_sensor = 0        # port A2
temperature_sensor = 8  # port D8
led = 2                 # port D2


grovepi.pinMode(led,"OUTPUT")
grovepi.analogWrite(led,10)  #turn led to max to show readiness
print("Actividad 3") 

while True:
    
    try:
        

        # Obtener el Valor del sensor de Luz
        light_intensity = grovepi.analogRead(light_sensor)
        
        # Give PWM output to LED
        grovepi.analogWrite(led,light_intensity)

        # GObtener Valor del sensor de sonido 
        sound_level = grovepi.analogRead(sound_sensor)

        time.sleep(0.5)

        # Get value from temperature sensor
        [t,h]=[0,0]
        [t,h] = grovepi.dht(temperature_sensor,0)
        

        # Post a tweet
        out_str ="Temp: %d C, Humedad: %d, Luz: %d, Sonido: %d" %(t,h,light_intensity/10,sound_level)
        print(out_str)
        
    except IOError:
        print("Error")
    except KeyboardInterrupt:
        exit()
    

    time.sleep(5)
import time
from grovepi import *

# Connect the Grove LED to digital port D4

print ("Conectar los módulos Led  a los puertos 2, 3 y 4 ")

led_red = 4
pinMode(led_green,"OUTPUT")

# Acá inicia tu código
led_green = None
led_blue = None
pinMode()
pinMode()
#Acá finaliza tu código

digitalWrite(led_green,0)
digitalWrite(led_blue,0)
digitalWrite(led_red,0) 

time.sleep(1)

print ("Actividad Reto Semaforo")
print (" ")
print ("Connect the LED to the port labele D4!" )

while True:
    try:
        digitalWrite(led_red,1)     # Send HIGH to switch on LED
        print ("Stop !")
        time.sleep(5)
        digitalWrite(led_red,0)     # Send LOW to switch off LED
        print ("LED Rojo OFF!")
        time.sleep(1)
        
        # Acá inicia tu código
        
        digitalWrite()     # Activar led Azul
        print ("Atento !")
        time.sleep(1)
        digitalWrite()     # Apagar led Azul
        print ("Led Azul OFF!")
        time.sleep(1)
        
        digitalWrite()     # Activar led verde
        print ("Adelante Verde !")
        time.sleep(5)
        digitalWrite()     # Apagar led verde
        print ("Led Verde Off!")
        time.sleep(1)        
       
        #Acá finaliza tu códigoo
        
        

    except KeyboardInterrupt:   # Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError:             # Print "Error" if communication error encountered
        print ("Error")
import time
from grovepi import *

# Connect the Grove LED to digital port D4

led_green = 2
led_blue = 3
led_red = 4

pinMode(led_green,"OUTPUT")
pinMode(led_blue,"OUTPUT")
pinMode(led_red,"OUTPUT")

digitalWrite(led_green,0)
digitalWrite(led_blue,0)
digitalWrite(led_red,0) 

time.sleep(1)

print ("Actividad Reto Semaforo")
print (" ")
print ("Connect the LED to the port labele D4!" )

while True:
    try:
        #Blink the LED
        digitalWrite(led_green,1)     # Send HIGH to switch on LED
        print ("Adelante Verde !")
        time.sleep(5)

        digitalWrite(led_green,0)     # Send LOW to switch off LED
        print ("Led Verde Off!")
        time.sleep(1)
        
        digitalWrite(led_blue,1)     # Send HIGH to switch on LED
        print ("Atento !")
        time.sleep(1)

        digitalWrite(led_blue,0)     # Send LOW to switch off LED
        print ("Led Azul OFF!")
        time.sleep(1)        
        
        digitalWrite(led_red,1)     # Send HIGH to switch on LED
        print ("Stop !")
        time.sleep(5)

        digitalWrite(led_red,0)     # Send LOW to switch off LED
        print ("LED Rojo OFF!")
        time.sleep(1)

    except KeyboardInterrupt:   # Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError:             # Print "Error" if communication error encountered
        print ("Error")
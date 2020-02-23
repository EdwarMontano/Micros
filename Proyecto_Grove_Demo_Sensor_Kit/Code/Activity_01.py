import time
from grovepi import *

# Connect the Grove LED to digital port D4


led_red = 4


pinMode(led_red,"OUTPUT")
digitalWrite(led_red,0) 

time.sleep(1)

print ("Actividad  !")
print (" ")
print ("Conectar el  LED al puerto D4!" )

while True:
    try:
        #Blink the LED      
        
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
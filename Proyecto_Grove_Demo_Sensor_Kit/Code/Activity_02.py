# Actividad   02 
import time
from grovepi import *
import math

buzzer= 5
relay = 8
button = 6



pinMode(buzzer,"OUTPUT")
pinMode(relay,"OUTPUT")
pinMode(button,"INPUT")


print ("Actividad 2 !")
print (" ")
print ("Conectar el buzzer al puerto D5!" )
print ("Conectar el botón al puerto D6!" )
print ("Conectar el Relay al puerto D8!" )

time.sleep(5)


status = 0
while True:
    try:
        status= digitalRead(button)  #Read the Button status
        print(status)    
        
        if status == 1:
            digitalWrite(buzzer,1)
            digitalWrite(relay,1)
                                      
        else:       
            digitalWrite(buzzer,0)
            digitalWrite(relay,0)
            
                             
    except KeyboardInterrupt:   # Stop the buzzer before stopping
            digitalWrite(buzzer,0)
            digitalWrite(relay,0)
            break
    except (IOError,TypeError) as e:
            print("Error")

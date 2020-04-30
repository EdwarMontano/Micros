import time
from grovepi import *
import math

buzzer_pin = 5
relay = 8
button = 6



pinMode(buzzer_pin,"OUTPUT")
pinMode(relay,"OUTPUT")
pinMode(button,"INPUT")


print ("Actividad 2 !")
print (" ")
print ("Conectar el buzzer al puerto D5!" )
print ("Conectar el botón al puerto D6!" )
print ("Conectar el Relay al puerto D8!" )

time.sleep(5)

button_Flag= 0
status = 0
while True:
    try:
        button_status= digitalRead(button) 
        print(button_status)
        
        if button_status == 1 and button_Flag == 0:   
            status=1-status
            time.sleep(1)
            
        button_Flag= button_status
        
        if status == 1:
            digitalWrite(buzzer_pin,1)
            digitalWrite(relay,1)
                                      
        else:       
            digitalWrite(buzzer_pin,0)
            digitalWrite(relay,0)
            
                             
    except KeyboardInterrupt:   
            digitalWrite(buzzer_pin,0)
            digitalWrite(relay,0)
            break
    except (IOError,TypeError) as e:
            print("Error")
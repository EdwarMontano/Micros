import time
from grovepi import *
import math

buzzer= 5
relay = 8
button = 6


# Acá inicia tu código
pinMode(buzzer,)
pinMode(relay,)
pinMode(,"INPUT")
#Acá finaliza tu código

print ("Actividad 2 RETO !")
print (" ")
print ("Conectar el buzzer al puerto D5!" )
print ("Conectar el botón al puerto D6!" )
print ("Conectar el Relay al puerto D8!" )

time.sleep(5)

# Acá inicia tu código
button_Flag= None
status = None
#Acá finaliza tu código
while True:
    try:
        button_status= digitalRead(button)  #Leer el estado del Botón
        #print(button_status)
        
        # Acá inicia tu código
        if :#Condicional para mantener el Estado del Botón
            status=1-status
            time.sleep(1)
            
        button_Flag= button_status
        #Acá finaliza tu código
        
        if status == 1:# Condicional para verificar estado 
            digitalWrite(buzzer_pin,1)
            digitalWrite(relay,1)
                                      
        else:       
            digitalWrite(buzzer_pin,0)
            digitalWrite(relay,0)
            
                             
    except KeyboardInterrupt:   # Stop the buzzer before stopping
            digitalWrite(buzzer_pin,0)
            digitalWrite(relay,0)
            break
    except (IOError,TypeError) as e:
            print("Error")

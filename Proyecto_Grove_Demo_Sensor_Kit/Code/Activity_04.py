from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan

ultrasonic_ranger = 7
setRGB(0,0,255)

while True:
    try:
        
        distancia= ultrasonicRead(ultrasonic_ranger)
        print(distancia,'cm')
        
        d = str(distancia)

       
        
        setRGB(0,0,255)
        setText("dis:" + d + "cm\n" )

    except (IOError, TypeError) as e:
        print(str(e))        
        setText("")

    except KeyboardInterrupt as e:
        print(str(e))
        setText("")
        break

    
    sleep(0.05)

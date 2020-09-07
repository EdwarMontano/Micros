#Son las unicas librerias que se usan
#os ya viene por defecto, y pormite ejecutar comandos de consola, desde python.
#En este caso, esos comandos, son otroas scripts de python.
import os
import tkinter as tk
from tkinter import *
import time
from grovepi import *
import numpy as np 
import matplotlib.pyplot as plt
import math
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import numpy as np



window = tk.Tk()
window.geometry("1080x650")
window.title("Raspberry Demo GUI")

#Asi se crean los sensores, o mejor dicho, las variables booleanas que definen si un determinado sensor esta en funcionamiento.
#cuando se logren modificar estas, solo es necesario poner diferentes condiciones en el metodo paginaActividad() para indicar que
#los sensores de alguna actividad estan finalmente activos y correr el script determinado.

global flag

flag=0
print(flag)
#

def setElement(element,x,y):
    element.grid(row=x, column=y)

#Se crean distintas variables que almacenan la ruta a las imagenes usadas en la interdfaz grafica.
boton1 = PhotoImage(file="button1.gif")
boton2 = PhotoImage(file="button2.gif")
boton3 = PhotoImage(file="button3.gif")
boton4 = PhotoImage(file="button4.gif")
boton5 = PhotoImage(file="button5.gif")
ejecutarButton = PhotoImage(file="Ejecutar2.gif")
backButton = PhotoImage(file="back.gif")
photoPi =  PhotoImage(file="raspberry-pi-logo.gif")
photoUv =  PhotoImage(file="Logo-uv.gif")
photoBlank = PhotoImage(file="blank.gif")

#Para separar los botones, se crean unos "blanks" o espacios en blanco, que se ubican en los espacios de la rejilla que van entre los botones
#y son invisible.
blankSpace = 100
blank1 = Label(window,image=photoBlank, height=blankSpace, width=blankSpace)
blank3 = Label(window,image=photoBlank, height=blankSpace, width=blankSpace)
blank5 = Label(window,image=photoBlank, height=blankSpace, width=blankSpace)
blank7 = Label(window,image=photoBlank, height=blankSpace, width=blankSpace)
blank9 = Label(window,image=photoBlank, height=blankSpace, width=blankSpace)


#Se añaden tanto el logo de la universidad de valle como el logo de Raspberry PI
piLogo = Label(window,image=photoPi, height=200, width=240)
uvLogo = Label(window,image=photoUv, height=200, width=240)

#Se añaden los labels que contienen el etxto utilizado en la interfaz. Los labels son el titulo del protecto y el identificador de numero de la actividad.
titulo = Label(window,text="\nRaspberry PI Demo\nSensor Kit\n",fg="black",bg="white",font=("Arial",50))
numeroId = Label(window, text="test", fg="black", bg="white", font=("Arial", 60))



#Se crean todos los botones, llamando al metodo paginaActividad con un valor distinto, inicializando su tamaño y sus respectivas imagenes.
buttonSize = 142
btn1 = Button(window, image=boton1, height=buttonSize, width=buttonSize, borderwidth=0, command =lambda: paginaActividad(1))
btn2 = Button(window, image=boton2, height=buttonSize, width=buttonSize, borderwidth=0, command =lambda: paginaActividad(2))
btn3 = Button(window, image=boton3, height=buttonSize, width=buttonSize, borderwidth=0, command =lambda: paginaActividad(3))
btn4 = Button(window, image=boton4, height=buttonSize, width=buttonSize, borderwidth=0, command =lambda: paginaActividad(4))
btn5 = Button(window, image=boton5, height=buttonSize, width=buttonSize, borderwidth=0, command =lambda: paginaActividad(5))
back = Button(window, image=backButton, height=buttonSize, width=buttonSize, borderwidth=0, command =lambda: regresarPaginaPrincipal())

btnActividad1 = Button(window, image=ejecutarButton, height=buttonSize, width=buttonSize-1, borderwidth=0, command =lambda: actividad_1())
btnActividad2 = Button(window, image=ejecutarButton, height=buttonSize, width=buttonSize-1, borderwidth=0, command =lambda: actividad_2())
btnActividad3 = Button(window, image=ejecutarButton, height=buttonSize, width=buttonSize-1, borderwidth=0, command =lambda: actividad_3())
btnActividad4 = Button(window, image=ejecutarButton, height=buttonSize, width=buttonSize-1, borderwidth=0, command =lambda: actividad_4())
btnActividad5 = Button(window, image=ejecutarButton, height=buttonSize, width=buttonSize-1, borderwidth=0, command =lambda: actividad_5())


#
# textoActividad1 = Label(window,text="\nRaspberry PI Demo\nSensor Kit\n",fg="black",bg="white",font=("Arial",50))
# textoActividad2 = Label(window,text="\nRaspberry PI Demo\nSensor Kit\n",fg="black",bg="white",font=("Arial",50))
# textoActividad3 = Label(window,text="\nRaspberry PI Demo\nSensor Kit\n",fg="black",bg="white",font=("Arial",50))
# textoActividad4 = Label(window,text="\nRaspberry PI Demo\nSensor Kit\n",fg="black",bg="white",font=("Arial",50))
# textoActividad5 = Label(window,text="\nRaspberry PI Demo\nSensor Kit\n",fg="black",bg="white",font=("Arial",50))


#En este metodo se escribi lo que debe ir en cada seccion de cada actividad. Esta dibuja sus contenido  de acuerto al boton
#que se haya presionado
def paginaActividad(numeroActividad):
    for btn in buttons:
        btn.grid_forget()
    back.grid(row=2, column = 0)
    numeroId.configure(text = "Actividad #"+str(numeroActividad))
    numeroId.grid(row =1, column = 1)
    if numeroActividad == 1:
        flag=0
        print(flag)
        btnActividad1.grid(row=2, column=1)
    elif numeroActividad ==2:
        btnActividad2.grid(row=2, column=1)
    elif numeroActividad ==3:
        btnActividad3.grid(row=2, column=1)
    elif numeroActividad ==4:
        btnActividad4.grid(row=2, column=1)
    elif numeroActividad ==5:
        btnActividad5.grid(row=2, column=1)



#Se crea una rreglo llamado buttons con todos los compenentes en la pantalla que seran escondidos luego de
#seleccionar una pestaña en espeficico
buttons = [btn1,btn2,btn3,btn4,btn5,blank1,blank3,blank5,blank7,blank9]

#Se crea el metodo regresar a la pantalla principal que se ejecuta luego de presionar su boton correspondiente u cuya funcion es
#dibujar nuevamente los componentes borrados.
def regresarPaginaPrincipal():
    
    #back['state']=tk.DISABLED
    
    numeroId.grid_forget()
    back.grid_forget()
    btnActividad1.grid_forget()    
    btnActividad2.grid_forget()
    btnActividad3.grid_forget()
    btnActividad4.grid_forget()
    btnActividad5.grid_forget()
    titulo.grid(row=0, column=1, columnspan=3)
    piLogo.grid(row=0, column=0)
    uvLogo.grid(row=0, column=4)
    blank1.grid(row=1, column=0)
    blank1.grid(row=1, column=0)
    blank3.grid(row=1, column=2)
    blank5.grid(row=1, column=4)
    blank7.grid(row=2, column=1)
    blank9.grid(row=2, column=3)
    btn1.grid(row=1, column=1)
    btn2.grid(row=1, column=3)
    btn3.grid(row=2, column=0)
    btn4.grid(row=2, column=2)
    btn5.grid(row=2, column=4)
    
    
def actividad_1():
    
    led_red = 3
    pinMode(led_red,"OUTPUT")
    digitalWrite(led_red,0) 

    time.sleep(1)

    print ("Actividad  !")
    print (" ")
    print ("Conectar el  LED al puerto D4!" )
    #back['state']=tk.DISABLED
    #print(btnActividad1['state'])

    while True:
        try:
            #Blink the LED      
            
            digitalWrite(led_red,1)     # Send HIGH to switch on LED
            print ("Stop !")
            time.sleep(5)

            digitalWrite(led_red,0)     # Send LOW to switch off LED
            print ("LED Rojo OFF!")
            time.sleep(1)
            
            
            #if back['state']=='disabled':
                #break

        except KeyboardInterrupt:   # Turn LED off before stopping
            digitalWrite(led,0)
            break
        except IOError:             # Print "Error" if communication error encountered
            print ("Error")
    print("Sali Test1");
    regresarPaginaPrincipal()
    
def actividad_2():
    x=1
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
def actividad_3():
    # Connections
    x=1
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
            exit
def actividad_4():
    x=1
    potenciometro= 2
    ultrasonic_ranger = 7

    Medida=[]
    offset=[]

    setRGB(10,10,10)

    while True:
        try:
            
            for i in range(10):
                #print(i)
                distancia= ultrasonicRead(ultrasonic_ranger)
                Medida.append(distancia)
                Lectura_Pot=grovepi.analogRead(potenciometro)
                offset.append(Lectura_Pot)
                #sleep(0.005)
                
            vector_med=np.array(Medida)
            pro_estatura=np.around(np.mean(vector_med),2)
            vector_offset=np.array(offset)
            pro_offset=np.around(np.mean(vector_offset)/100,2)
            ajuste=np.around(pro_estatura+pro_offset,1)
            
            
            #print(pro_estatura,'cm', " ,offset: ", pro_offset)
            print(ajuste,'cm', " ,offset: ", pro_offset,"*****") 
            d = str(pro_estatura)
                   
            
            setText("dis:" + d + "cm\n"+ "offset:"+str(pro_offset)+ "cm\n")

        except (IOError, TypeError) as e:
            print(str(e))        
            setText("")

        except KeyboardInterrupt as e:
            print(str(e))
            setText("")
            break
def actividad_5():
    x=1
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







#Se añaden a la ventana los compenentes iniciales
titulo.grid(row = 0, column = 1,columnspan=3)

setElement(piLogo, 0, 0)
setElement(uvLogo, 0, 4)

setElement(blank1, 1, 0)
setElement(blank3, 1, 2)
setElement(blank5, 1, 4)
setElement(blank7, 2, 1)
setElement(blank9, 2, 3)
setElement(btn1, 1, 1)
setElement(btn2, 1, 3)
setElement(btn3, 2, 0)
setElement(btn4, 2, 2)
setElement(btn5, 2, 4)







#Finalmente se crea le ventana de la GUI
window.configure(background='white')
window.resizable(width=False, height=False)

window.mainloop()

# Proyecto Microcontroladores y Ensamblador RaspberryPI Demo Sensor Kit 

**Autores:** Lasso Juan Pablo, Montaño Edwar Stiven

El uso de tarjetas de desarrollo completas con las que contamos el día de hoy ahorran tiempo, esfuerzo y acortan distancia entre el programador y el montaje de hardware embebido. Con el uso de un lenguaje de programación de fácil aprendizaje y sumamente estandarizado estás plataformas alcanzan el objetivo de acercar la tecnología a todos. Los módulos utilizados en este proyecto cumplen con estas características y tenemos como aprovecharnos al máximo de las herramientas que brinda el GrovePi+, implementando una serie de actividades como Demo

**Palabras Clave**  — RaspberryPi, GrovePi+, Sensor, Actuador.

## Fase I Documentacion

### I.	INTRODUCCIÓN
El RaspberryPi esta destinado principalmente al desarrollo de pequeños prototipos y a estimular la enseñanza de las ciencias de la computación en los centros educativos, desarrollado en hardware libre cuenta con sistemas operativos GNU/Linux de muy fácil uso y aprendizaje acelerado. 

El GrovePi + por otra parte solo permite conectar, programar y controlar sensores para construir dispositivos inteligentes. Sin embargo, esta funcionalidad abre por completo un nuevo campo de desarrollo, en el que obtener información proveniente de sensores externos, trabajar con esos datos y enviarlos a través de distintos módulos nunca había sido tan fácil, rápido y construido usando un lenguaje de programación como Python.

### II.	OBJETIVOS DEL PROYECTO

Desarrollar 5 actividades donde se implemente el uso y manejo de todos los sensores del GrovePi + kit  

*	Desarrollar una rutina de prueba para los sensores y las rutinas para cada actividad usando el lenguaje de programación Python. 
*	Acceder a cada componente de la actividad (sensores y actuadores) usando Scripts en Python que son convertidos en configuraciones para el microcontrolador presente en el GrovePi +
* Diseñar una interfaz gráfica para que el usuario pueda interactuar con cada actividad de forma visual e intuitiva
*	Implementar una buena metodología de desarrollo como lo es RUP para llevar a cabo el proyecto de manera eficiente

### II.	SOFTWARE Y HARDWARE A UTILIZAR

<table>
    <tr>
      <th colspan="2"><b>HARDWARE</b></th>      
    </tr>
    <tr>
      <th><b>Raspberry Pi 3modelo B+</b></th>
      <th><b>GrovePi +  Kit</b></th>
    </tr>  
    <tr>
      <th><img width="250px" src="https://suconel.com/wp-content/uploads/91zSu4434L._SL1500_-1.jpg"></th>
      <th><img width="250px" src="https://www.mcielectronics.cl/website/image/product.template/19751_7720929/image"></th>
    </tr>  
    <tr>
      <td>
        <ul>
          <li>SoC Broadcom BCM2837B0 con </li>
          <li>procesador ARM Cortex A53  64 bits, 1.4 GHz</li>
          <li>1 GB RAM, GPU VideoCore IV</li>
          <li>salida de video HDMI</li>
          <li>salida de audio y video compuesto 3.5 mm</li>
          <li>lector microSD, 4 x USB 2.0</li>
          <li>Ethernet 10/100/300</li>
          <li>WiFi 2.4 GHz y 5 GHz</li>
          <li>Bluetooth</li>
          <li>28 pines I/O con UART, SPI y I²C<a href="https://www.xataka.com/ordenadores/raspberry-pi-3-model-b-analisis-mas-potencia-y-mejor-wifi-para-un-minipc-que-sigue-asombrando">[1]</a></li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Soporta Raspberry Pi 3 modelo A+ y B+</li>
          <li>7 Puertos Digitales</li>
          <li>3 Puertos Analogos</li>
          <li>3 Puertos I2C</li>
          <li>1 Puerto Serial para conectar a GrovePi +</li>
          <li>1 Puerto Serial para conectar a RaspberryPi</li>
          <li>12 Módulos Principales</li>
          <li>Posee un Microcontrolador Atmega 328p <a href="https://shop.dexterindustries.com/grovepi-starter-kit-2/">[2]</a></li>          
        </ul>
      </td>
    </tr>  
    <tr>
      <th colspan="2"><b>SOFTWARE</b></th>      
    </tr>
    <tr>
      <th><img width="250px" src="https://www.sketchappsources.com/resources/source-image/python-logo.png"></th>
      <td>
        <li>Lenguaje de propósito general</li>
        <li>Es multiparadigma</li>
        <li>Python es un lenguaje interpretado.</li>
        <li>Es multiplataforma</li>
        <li>Es de tipado dinámico</li>
        <li>Es orientado a objetos <a href="https://www.python.org/psf/about/">[3]</a></li>
      </td>
    </tr> 
</table>

### III.	DESCRIPCIÓN DE LAS ACTIVIDADES

## **Actividad 1**

Se realizará el proceso de la configuración inicial, la instalación de programas y librerías para  implementará un programa sencillo para configurar los modos de operación del RaspberryPI que muestre un resultado sencillo de interpretar: Dos LEDs parpadeando como actividad guiada y como actividad reto la realización de un semáforo temporizado. A continuación, se observarán los módulos que se utilizarán para esta primera actividad



<a href="https://ibb.co/9nzRnkt"><img align="center" width="500px" src="https://i.ibb.co/v1g216Y/Diapositiva1.png" alt="Actividad 1" border="0" ></a>

**Figura 4**. *Módulos a usar  en la Actividad 1*

			
## **Actividad 2**

Se añadirá una entrada a nuestro sistema y las salidas correspondientes (un bombillo controlado por un Relé y un Buzzer) que se alterarán al presionar el botón de entrada de esta manera se realizará una alarma como actividad guiada y como actividad reto que el buzzer se active número de veces que el botón sea presionado dependiendo . A continuación, se observarán los módulos que se utilizarán para la actividad 2.

<center>
<a href="https://ibb.co/8x8ZN1m"><img width="500px" src="https://i.ibb.co/pKXFbY1/Diapositiva2.png" alt="Actividad 2" border="0"></a>
</center>

**Figura 5.** *Módulos a usar  en la Actividad 2 alarma*


## **Actividad 3**

Usando los ADCs presentes en el microcontrolador se implementará un filtro en la señal de entrada captada por un micrófono, de manera que puedan mostrar salidas distintas (3 LEDs a la salida) dependiendo del tono del sonido captado como actividad guiada y como actividad reto que se pueda grabar el audio y sea guardado en algún formato de audio para poder reproducirlo. A continuación, se observarán los módulos que se utilizarán para esta tercera actividad.

<a href="https://ibb.co/dMcGyw2"><img width="500px" src="https://i.ibb.co/QQcrG3N/Diapositiva3.png" alt="Actividad 3" border="0"></a>

**Figura 6.** *Módulos a usar  en la Actividad 3 medidor de ruido ambiente*

## **Actividad 4**

Se trabajará con la configuración del microcontrolador con el fin de usar un PWM para medir distancia con un sensor ultrasónico, y se implementará un protocolo de comunicación I2C para transmitir esta información a un Display LCD. A continuación, se observarán los módulos que se utilizarán para esta actividad.

<a href="https://ibb.co/LDFZs4J"><img width="500px" src="https://i.ibb.co/wZkz2Dw/Diapositiva4.png" alt="Actividad 4" border="0"></a>
 
**Figura 7.** *Módulos a usar  en la Actividad 4 medidor de estatura*

## **Actividad 5**

Se implementará un programa en el que se usen múltiples sensores como entradas y sean mostrados en un Display LCD usando un protocolo de comunicación I2C. A continuación, se observarán los módulos que se utilizarán para la actividad 5.


 <a href="https://ibb.co/r6H8m1q"><img width="500px" src="https://i.ibb.co/PhgXNfJ/Diapositiva5.png" alt="Actividad 5" border="0"></a>

**Figura 8.** *Módulos a usar  en la Actividad 5 estación de clima*


## Fase II Code en Python 
## Fase III GUI en Python
**Interfaz Gráfica**

Con el uso de librería como QT para la creación de interfaces gráficas en Python, se desarrollará una interfaz gráfica que proporcione al usuario una forma intuitiva de ver el estado de los sensores, y las actividades que puede realizar dependiendo de si los sensores están listos, y la selección rápida de actividades. A continuación, se podrá ver el diseño previsto para esta interfaz, mostrando dos botones para acceder a la ventana de las actividades y otro para acceder a la ventana de prueba de sensores.


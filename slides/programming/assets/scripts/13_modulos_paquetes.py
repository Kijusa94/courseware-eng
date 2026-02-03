#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:49:26 2023

@author: kijusa94
"""

"""
Las funciones pueden ser agrupadas en archivos conoocidos como 'modulos'.
Estos agrupan funciones que se asocian debido a las tareas que cumplen. De
esa forma no tendremos que 'reinventar la rueda'

Un ejemplo de ello es el modulo 'math'. El cual agrupa funciones
matematicas para ser usadas en nuestros códigos. Veamos un ejempo sencillo.
"""

import math
help (math)
math.cos(math.pi)

"""
Si el módulo no se encuentra instalado en nuestra versión de python, podemos
usar el entorno de Anaconda para instalarlo.

Tambien, podemos instalarlo usando el terminal del Anaconda con el siguiente
comando:
    conda install nombre_del_modulo
    
Otra forma de hacerlo, es a traves de terminal usando Python:
    pip install nombre_del_modulo

Podemos listar los paquetes istalados mediante:
    pip list
"""

"""
Por otra parte, tenemos el concepto de 'paquete'. Estos son archivos que 
agrupan un conjunto de modulos.

Para evitar confusiones con las definiciones. Puede usar la siguiente analogía:
    Receta = funcion
    Libro de recetas = modulos
    Estanteria de recetas = paquete
    
Los paquetes tienen una etiqueta que caracteriza el paquete para que sus modulos
no se confunda con otros, a esta se le denimona 'namespace'. 

Siguiendo la analogía anterior, el namespace es como el nombre del autor. A
partir de ello, se puede diferenciar las recetas de diferentes autores.
"""

"""
Organice sus proyectos como se sugiere a continuacion:
    
src
    principal.py                        #Su codigo principal
    paquete_de_datos                    #Subcarpeta
        transacciones.py                #paquete o modulo
    paquete_de_visualizacion            #Subcarpeta
        graficas.py                     #paquete o modulo
        plantillas.py                   #paquete o modulo
    paqueteconfuncionesauxiliares       #Subcarpeta
        auxiliares_matematicas.py       #paquete o modulo
        auxiliares_fechas.py            #paquete o modulo
        
assets                                  #Almacena archivos necesarios
    images                              #Subcarpeta
        fondo.png                       #Recurso
        logo.png                        #Recurso
    language                            #Subcarpeta
        spanish.json                    #Recurso
        english.json                    #Recurso  
    
"""

"""
EJERCICIO: Cree una libreria personalizada con las funciones básicas de
una calculadora. Aplique una de las funciones a un codigo independiente.
Tome como base, la siguiente guía
"""

import my_package.my_package_1

my_package.my_package_1.Factorial(3)


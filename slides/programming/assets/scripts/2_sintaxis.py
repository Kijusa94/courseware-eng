#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 08:52:08 2023

@author: kijusa94
"""


"""
Así como el lenguaje natural entre seres humanos sigue unas reglas, los
códigos de los programas siguen una estructura definida para ejecutar acciones.
A las acciones se les denominará "sentencias" o "frases".

Veamos algunos ejemplos:
"""

"""
La siguiente instrucción utiliza la palabra reservada "import" para traer a 
este script la libreria "math",la cual contiene otros códigos que realizan
operaciones matematicas
"""          
import math

"""
En la siguiente instrucción se define una variable. Las variables son espacios
de memoria en disco que almacenan datos. Son contenedores en donde guardamos un dato.
En el caso de Python no se define el tipo de dato a guardar. 
"""
a = 5       #Se define la variable con nombre "a" y se le asigna el valor 5.
c = 10/a    #Se define la variable con nombre "c" y se le asigna el cociente.
nombre = 'hola mundo'   #Se define la variable "nombre" y se le asigna
                        # 'hola mundo'. Note que en este caso tiene comillas 
                        #por ser un tipo de dato texto

"""
Las variables pueden ser de los siguientes tipos:
    Numerica: Almacenan valores enteros o decimales
    Texto: Almacena cadenas de caracteres. Es decir, la suma de letras
    Booleano: Almacena Verdadero o False. True/False
"""

"""
A pesar de que no se define el tipo de variable, es necesario tener presente los
tipos de variables.

A continuación se presenta la forma en como se asignan valores:
"""
numero = 0                          #Los numeros almacenan valores enteros o decimales
                                    #Observe que no llevan comillas
                                    
cadena = "hola mundo"               #Las cadenas de texto llevan comillas dobles
                                    #porque son la suma de caracteres individuales
                                    
diccionario = {10:"valor1", 15:"valor 2", 11:"cadena de texto", 21:45}
diccionario[10]
                                    #Los diccionarios almacenan datos en pares con 
                                    # la particularidad que son una clave y un valor 
                                    
lista = ["dato1", "dato2", "dato3"] #Las listas pueden almacenar muchos datos de un mismo tipo
                                    #en este caso está almacenando 3 datos de tipo cadena. la
                                    #lista lo organiza de forma secuencial. lista[0] = "dato1"
                                    
tupla = ("manzana", 15)             #Las tuplas son casos especiales de listas. estos almacenan
                                    #datos organizados por indice, es decir, el indice
                                    #cero de la tupla tiene por valor "manzana".
                                    
"""
Podemos acceder a los valores de las variables de la siguiente forma.
numero
cadena
diccionario[15]
lista[0]
tupla[1]
Copie y pegue cada una de estas lineas en la consola de comandos. Observará que
se deslpliega el valor de cada variable indicada
"""

"""
Los valores constantes no existen en Python, por lo que se utiliza una nomenclatura
para asignar valores que esperamos que no cambien en nuestro programa. Es habitual
nombrar en mayusculas las variables que consideramos constantes. Observe los ejemplos:
"""
GRAVEDAD = 9.8
PI = 3.1416
MU = 2.21
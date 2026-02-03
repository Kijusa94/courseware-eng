#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:07:56 2023

@author: kijusa94
"""

"""
Python es una herramienta de procesamiento numerico bastante potente, por ende
trabajar con archivos es una tarea comun. En este código se explicará como
se puede realizar la lectura y escritura en archivos.

Los archivos almacenan lineas compuestas por cadenas de texto.
"""

#Para abrir un archivo usamos open(). Es necesario indicar el modo de apertura
#pues podemos solo leer, solo escribir, leer y escribir
archivo = open('ejercicio.csv', 'r')
archivo.read()

#Cuando terminamos de leer la informacion del archivo, es importante cerrarlo
archivo.close()
archivo.read()

"""
Modos de apertura: Binario (b) es para audio o video.
Indicador           Modo                                    Ubicacion puntero
r                   solo lectura                            Al inicio del archivo
rb                  solo lectura en modo binario            Al inicio del archivo
r+                  lectura y escritura                     Al inicio del archivo
rb+                 lectura y escritura (b)                 Al inicio del archivo
w                   solo escritura. sobreecribe o crea      Al inicio del archivo
wb                  solo escritura (b). sobreecribe o crea  Al inicio del archivo
w+                  lect. y escrit. sobreecribe o crea      Al inicio del archivo
a                   añadido. Crea.                          Añadir (al final). Crea (al inicio)
a                   añadido (b). Crea                       Añadir (al final). Crea (al inicio)
a+                  añadido y lectura. Crea.                Añadir (al final). Crea (al inicio)
ab+                 añadido y lect (b). Crea.               Añadir (al final). Crea (al inicio)
"""

"""
Veamos algunos metodos para manejar el contenido de un archivo
"""

archivo = open('ejercicio.csv', 'r')
contenido = archivo.read()
print(contenido)            #El print ha incluido \n como salto de linea
archivo.close()

#Para leer linea a linea. readline(). Tenga presente que las lineas se leeran
#de acuerdo co la posicion del puntero dentro del archivo.
archivo = open('ejercicio.csv', 'r')
linea0 = archivo.readline()
linea1 = archivo.readline()
print(linea0)               #Incluye un salto de linea por al lectura
print(linea1.strip())       #Eliminamos el salto de linea
archivo.close()


#Podemos ser eficientes con la lectura, aplicando un clico
archivo = open('ejercicio.csv', 'r')
for linea in archivo.readlines():
    print(linea.strip())
archivo.close()

#Utilizamos tell() para conocer la ubicacion del puntero en el archivo.
archivo = open('ejercicio.csv', 'r')
print(archivo.tell())
linea0 = archivo.readline()
print(archivo.tell())
archivo.close()

#Para posicionar el puntero, usamos seek()
archivo = open('ejercicio.csv', 'r')
archivo.read()
print(archivo.tell())
archivo.seek(0)
print(archivo.tell())
archivo.close()

#Podemos crear un archivo nuevo (si este no existe en la carpeta) y escribir
#en él.
archivo = open('prueba_texto.csv', 'w+')
archivo.write('nueva cadena de caracter')
archivo.close()

#Hay veces que el procesador está ocupado. Por lo que podemos hacer flush()
#para forzar la escritura en el archivo (de lo que esta en la memoria temporal)
archivo = open('prueba_texto.csv', 'a+')
archivo.write('cadena para flushear')
archivo.flush()
archivo.close()

#Abrir el archivo de la siguiente forma, puede ser mas conveniente. Esto dado
#de que la apertura o cierre puede fallar. La instruccion 'with open' se 
#encarga de gestionar ello y de guardar si falla.
#OJO: 'archivo' solo existe en el contexto del with open.
with open('prueba_texto.csv', 'r') as archivo:
    print(archivo.read())
print(archivo.read())







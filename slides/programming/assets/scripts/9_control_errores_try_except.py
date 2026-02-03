#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:10:07 2023

@author: kijusa94
"""

"""
en este script vamos a ver cómo tratar errores en Python con el bloque try/except. 
Recordemos que en uno de los códigos anteriores hablamos sobre cómo,
de los errores se aprende. Pero no siempre querremos aprender de ellos sobre
todo cuando son errores de tipo de ejecución. A menudo, es mejor tratarlos
y, o bien, arreglarlos o bien ponerles algún remedio para que no sean un
error tan problemático. 
"""

"""
Veamos el siguiente código. En él queremos que el usuario ingrese un numero
para calcular el factorial del numero.
"""

factorial = 1
valor = int(input("Ingrese un numero entero para calcular su factorial"))

for i in range(1, valor + 1):
    factorial *= i
print("El factorial del numero", valor, "es", factorial)

"""
Un usuario puede poner una palabra (tres) y es to da un error. Cuando
esto pase el programa fallará, el programa dará error y si
el usuario final no somos nosotros sino que es alguien que
está utilizando el programa no entenderá que está pasando.

Para indicar al usuario un error, podemos utilizar las instrucciones 'try'
y 'except'.
"""
try:
    factorial = 1
    valor = int(input("Ingrese un numero entero para calcular su factorial"))

    for i in range(1, valor + 1):
        factorial *= i
    print("El factorial del numero", valor, "es", factorial)
except Exception as e:
    print("Ha ingresado un valor no válido. Ejecute nuevamente.")
    print(e)
    

"""
Si se requiere el valor ingresado para realizar otra serie de operaciones 
por fuera del 'try'/'except'. Es recomendable asignar un valor por defecto
para no detener la ejecución del programa.
"""

try:
    factorial = 1
    valor = int(input("Ingrese un numero entero para calcular su factorial"))

    for i in range(1, valor + 1):
        factorial *= i
    print("El factorial del numero", valor, "es", factorial)
except Exception as e:
    print("Ha ingresado un valor no válido. Ejecute nuevamente.")
    print(e)
    factorial = 0
    
print("El factorial del numero sumado mas tres es:", factorial + 3)

"""
Tenga presente que si el bloque de código en el try es extenso, se dificultará
detectar el origen del error. Podemos indicar el tipo de error mediante los 
tipos de errores disponibles en la documentación de Python.
"""

try:
    factorial = 1
    valor = int(input("Ingrese un numero entero para calcular su factorial"))

    for i in range(1, valor + 1):
        factorial *= i
    print("El factorial del numero", valor, "es", factorial)
    
except ArithmeticError:
    print("Error aritmetico")
except ValueError:
    factorial = 0
except Exception as e:
    print("Ha ingresado un valor no válido. Ejecute nuevamente.")
    print(e)

print("El factorial del numero sumado mas tres es:", factorial + 3)
    
    
"""
En algunos casos queremos que se ejecuten unas instrucciones independiente
mente de lo ocurrido con el 'try' o 'except'. Para ello, usamos el 'finally'
Este resulta de gran importancia al cerrar archivos/conexiones a bases de datos
o sockets, o cualquier recurso que pueda bloquear la ejecución del programa.
"""    
try:
    factorial = 1
    valor = int(input("Ingrese un numero entero para calcular su factorial"))

    for i in range(1, valor + 1):
        factorial *= i
    print("El factorial del numero", valor, "es", factorial)
    
except ValueError:
    factorial = 0
finally:
    print(factorial + 3)            #Puede ser el cierre de una conexion a BD


    
    
    
    
    
    
    
    
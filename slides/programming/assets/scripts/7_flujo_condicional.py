#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:57:12 2023

@author: kijusa94
"""

"""
Pyhton funciona bajo un flujo de trabajo secuencial, en donde las instrucciones
se ejecutan una detras de otra. Por ejemplo:
"""
numero1 = 10
numero2 = 20
resultado = numero1 + numero2

"""
Sin embargo, en programación existen flujos de trabajo diferentes que permiten
afectar la ejecución de tareas dependiendo de condiciones. 

Un flujo de trabajo se denomina 'condicional'. y se estructura de la
siguiente manera:
    
if (condicion):
    Sentencia1
    Sentencia2
    ...
elif (condicion):
    Sentencia
else:
    SentenciaSiNo1
    SentenciaSiNo2
    ...

NOTA: SEA ORDENADO!. La identación (espacios entre saltos de linea) son 
indispensables en Python.
"""

if (numero1 >= numero2):
    print("el primer numero es mayor o igual que el primer numero")
else:
    print("el primer numero es menor que el segundo numero")
    

"""
Puede anidar los condicionales para preguntar por multiples condiciones. 
Para ello, utilice el comando elif
"""
if (numero1 > numero2):
    print("el primer numero es mayor que el primer numero")
elif (numero1 < numero2):
    print("el primer numero es menor que el segundo numero")
else:
    print("el numero 1 es igual al numero 2")
    
"""
EJERCICIO: Realice un código que imprima en pantalla un mensaje a partir de
la calificacion de un estudiante, de acuerdo con los siguientes rangos:
    Entre 0 y 1: Cancele herman@
    Entre 1 y 2: Sufrir el resto del semestre
    Entre 2 y 3: Lo subo en el próximo corte
    Entre 3 y 4: Lo importante es pasar
    Entre 4 y 5: A pedir decimas pa' promedio
"""
nota = float(input("Ingrese la nota del estudiante: "))

if (nota > 0 and nota < 1):
    print("Cancele herman@")
elif (nota > 1 and nota < 2):
    print("Sufrir el resto del semestre. Que cucho tan canson")
elif (nota > 2 and nota < 3):
    print("Lo subo en el proximo corte")
elif (nota > 3 and nota < 4):
    print("Lo importante es pasar")
elif (nota > 4 and nota < 5):
    print("Hay que pedir decimas para la beca")
else:
    print("Ingreso un valor no válido")


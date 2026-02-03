# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:17:46 2024

@author: juand
"""
#%%
"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
palabra = input("Ingrese la palabra a mostrar 10 veces: ")

#SOLUCION CON WHILE
a = 0
while a < 10:
    print(palabra)
    a = a + 1       #a += 1#
    
#SOLUCION CON FOR
for i in range(0, 10):
    print(palabra)

#%%
"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). 
"""
edad = int(input("Ingrese su edad: "))

#SOLUCION CON WHILE
i = 1
while i <= edad:
    print(i)
    i = i + 1
    
#SOLUCION CON FOR
for i in range(1, edad + 1):
    print(i)
    
#%%
"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
num = int(input("Ingrese el numero."))

if (num > 0):
    #SOLUCION CON WHILE
    i = 1
    while i < num:
        if (i % 2 == 1):
            print(i, end=",")
        i = i + 1
    
    #SOLUCION CON FOR
    """
    for i in range(1, num):
        if (i % 2 == 1):
            print(i, end=",")
    """            
else:
    print("Error, no es un numero entero positivo.")

#%%
"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
invertir = float(input("Ingrese el valor a invertir: "))
interesAnual = float(input("Ingrese el interes anual: "))
numAnios = int(input("Ingrese el numero de anios: "))

for i in range(numAnios):
    ganancia = invertir * interesAnual / 100
    print(f"El capital en el {i} año es {invertir}.")
    invertir = invertir + ganancia

#%%
"""

"""











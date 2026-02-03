# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:51:16 2024

@author: juand
"""
"""
EJERCICIO: Realice un código que permita listar los numeros del uno al cien, pero que no incluya aquellos numeros que son divisibles entre 3.
"""
i = 0
while (i < 100):
    i = i + 1
    if (i % 3 == 0):
        continue
    print(i)
    
for i in range(1, 101):
    if (i % 3 == 0):
        continue
    print(i)

"""
Calcular el factorial de un número.
5! = 1*2*3*4*5 = 120
"""
factorial = 1

num = int(input("Ingrese el numero: "))

for i in range(1, num + 1):
    factorial = factorial * i

print(f"{num}! = {factorial} ")

"""
Calcular la permutación de nPr = n! / (n - r)!
"""
factorialN = 1
factorialNR = 1

N = int(input("Ingrese el valor de N: "))
r = int(input("Ingrese el valor de r: "))

for i in range(1, N + 1):
    factorialN = factorialN * i

for i in range(1, (N - r) + 1):
    factorialNR = factorialNR * i

resultado = factorialN / factorialNR

print (f"{N} P {r} = {resultado}")

"""
Crea un algoritmo que dibuje un árbol dado un número, asumiendo que n >1. Para n = 5:
*
**
***
****
*****
"""
num = int(input("Ingrese el numero n: "))

for i in range(num + 1):
    msj = "*" * i
    print(msj)

"""
Escribir el sumatorio de los números que se quiera hasta ingresar -1.
"""
suma = 0
while num != -1:
    num = float(input("Ingrese el numero: "))
    suma += num
    print("Acumulado: " + str(suma))

"""
Calcula la Hipotenusa. Para ello, pide al usuario que te de el valor de los catetos. Por cada  caso, comprueba que los catetos son mayores a 0. Hasta que estos datos sean validados no calcular.
"""
#%%
import math 

cat1 = -1
cat2 = -1

while cat1 < 0 or cat2 < 0:
    cat1 = float(input("Ingrese el valor del cateto 1: "))
    cat2 = float(input("Ingrese el valor del cateto 2: "))

h = math.sqrt(cat1 ** 2 + cat2 ** 2)

print(f"La hipotenusa es: {h}" )
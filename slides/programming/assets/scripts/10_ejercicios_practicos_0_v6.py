# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:53:04 2024

@author: juand
"""
import math
#%%
"""
Se desea un codigo que permita calcular el factorial de un numero.
Ej:
    5! = 5*4*3*2*1 = 120
    10! = 10*9*8*7*...*3*2*1 = 
"""
factorial = 1

num = int(input("Ingrese el valor para calcular su factorial: "))

for i in range(1, num + 1):
    factorial = factorial * i
    
print(f"El factorial de {num} es {factorial}")

#%%
"""
Se desea un codigo que permita calcular la permutacion de un par de numeros dados por el usuario. La permutación está dada por la fórmula:
    N P r = N! / (N - r)! 

"""
factorialN = 1
factorialNr = 1

N = int(input("Ingrese el valor de N:"))
r = int(input("Ingrese el valor de r:"))

for i in range(1, N + 1):
    factorialN = factorialN * i

for j in range(1, (N-r) + 1):
    factorialNr = factorialNr * j
    
resultado = factorialN / factorialNr

print(f"{N} P {r} = {resultado}")

#%%
"""
Se desea un codigo que permita calcular la combinatoria de un par de numeros dados por el usuario. La combinatoria está dada por la fórmula:
    N C r = N! / r!(N - r)!
"""
factorialN = 1
factorialr = 1
factorialNr = 1

N = int(input("Ingrese el valor de N:"))
r = int(input("Ingrese el valor de r:"))

for i in range(1, N + 1):
    factorialN = factorialN * i

for i in range(1, r + 1):
    factorialr = factorialr * i

for i in range(1, (N-r) + 1):
    factorialNr = factorialNr * i
    
resultado = factorialN / (factorialr * factorialNr)

print(f"{N} C {r} = {resultado}")





















#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:27:18 2023

@author: kijusa94
"""

"""
Realice un programa que permita calcular la permutacion de un par de numeros
"""


import math

menu_control = 0
print("\014")

while menu_control != 3:
    print("1. Calculo de permutaciones")
    print("2. Calculo de combinaciones")
    print("3. Salir")
    menu_control = int(input("Ingrese la opción que necesite: "))
    print("\014")
    
    if (menu_control == 1):
        print("Una permutación permite conocer la cantidad de variaciones"
              " en un proceso de cambiar el orden lineal de un conjunto"
              "ordenado")
        print("Para ello, se requiere conocer el numero total de elementos"
              "del conjunto (N), y el numero de elementos que tendrá cada"
              "subconjunto (r)")
        print("La operación a realizar es: NPr = N!/(N-r)!")
        
        N = int(input("Ingrese el valor de N:"))
        r = int(input("Ingrese el valor de P:"))
        
        factorial1 = 1
        factorial2 = 1
        for i in range(N):
            factorial1 *= i + 1 
        for i in range(N-r):
            factorial2 *= i + 1
        
        resultado = factorial1/factorial2
        
        print("El factorial {0} P {1} = {2}".format(N, r, resultado))
        
        input("Press Enter to continue...")
        print("\014")
        
"""
EJERCICIO: Realice un programa que permita calcular la combinacion
de un par de numeros
"""

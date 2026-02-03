#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:15:16 2023

@author: Juan Guzman
"""

print("BIENVENIDA")
print("Le ofrecemos:")
print("1. Desayuno")
print("2. Almuerzo")
print("3. Cena")
opcion = int(input("Escoja su opcion: "))

if (opcion == 1):
    print("De desayuno tenemos: ")
    print("1. Huevito ranchero")
    print("2. Pan y cafe")
    print("3. Frutica picada")
    seleccion = int(input("Escoja su plato: "))
    if (seleccion <= 3):
        print("Su opción fue desayuno y el plato ", seleccion)
    else:
        print("Error. Plato no valido.")
elif (opcion == 2):
    print("De almuerzo tenemos: ")
    print("1. carnita asada")
    print("2. Huevo y arroz")
    print("3. pollo sudado")
    seleccion = int(input("Escoja su plato: "))
    print("Su opción fue almuerzo y el plato ", seleccion)
elif (opcion == 3):
    print("De cena tenemos: ")
    print("1. pasta")
    print("2. Huevo")
    print("3. lasagna")
    seleccion = int(input("Escoja su plato: "))
    print("Su opción fue cena y el plato ", seleccion)
else:
    print("La opcion es 1, 2 o 3. Error en su solicitud.")

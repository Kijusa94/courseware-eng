#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:20:11 2023

@author: kijusa94
"""
tipo = {10:"Las once", 20:"Almuerzo", 30:"Cena"}
platos_desayuno = {1:"Tostadas francesas", 2:"Pan y café", 3:"Frutica picada"}
platos_almuerzo = {1:"Carnita asada", 2:"huevo y arroz", 3:"Pollo sudado"}
platos_cena = {1:"Pasta", 2:"Pizza", 3:"Lasagna"}

print("BIENVENIDA")
print("Le ofrecemos:")
print(list(tipo.keys())[0], ".", list(tipo.values())[0])
print(list(tipo.keys())[1], ".", list(tipo.values())[1])
print(list(tipo.keys())[2], ".", list(tipo.values())[2])
opcion = int(input("Ingrese su opción: "))

if (opcion == list(tipo.keys())[0]):
    print(list(platos_desayuno.keys())[0], ".", list(platos_desayuno.values())[0])
    print(list(platos_desayuno.keys())[1], ".", list(platos_desayuno.values())[1])
    print(list(platos_desayuno.keys())[2], ".", list(platos_desayuno.values())[2])
    plato = int(input("Ingrese el plato que desea: "))
    if (platos_desayuno.keys().__contains__(plato)):
        print("Usted ha seleccionado la opción de {} con el plato {}")
    else:
        print("Ha ingresado una opción no válida. Ejecute nuevamente el programa.")

elif (opcion == list(tipo.keys())[1]):
    print(list(platos_almuerzo.keys())[0], ".", list(platos_almuerzo.values())[0])
    print(list(platos_almuerzo.keys())[1], ".", list(platos_almuerzo.values())[1])
    print(list(platos_almuerzo.keys())[2], ".", list(platos_almuerzo.values())[2])
    plato = int(input("Ingrese el plato que desea: "))
    if (platos_almuerzo.keys().__contains__(plato)):
        print("Usted ha seleccionado la opción de {} con el plato {}")
    else:
        print("Ha ingresado una opción no válida. Ejecute nuevamente el programa.")

elif (opcion == list(tipo.keys())[2]):
    print(list(platos_cena.keys())[0], ".", list(platos_cena.values())[0])
    print(list(platos_cena.keys())[1], ".", list(platos_cena.values())[1])
    print(list(platos_cena.keys())[2], ".", list(platos_cena.values())[2])
    plato = int(input("Ingrese el plato que desea: "))
    if (platos_cena.keys().__contains__(plato)):
        print("Usted ha seleccionado la opción de {} con el plato {}")
    else:
        print("Ha ingresado una opción no válida. Ejecute nuevamente el programa.")

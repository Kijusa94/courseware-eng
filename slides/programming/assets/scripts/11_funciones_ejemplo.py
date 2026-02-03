#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:59:09 2023

@author: kijusa94
"""


"""
EJERCICIO MENU DESAYUNO
"""

platos = [{"Huevito y arroz": 3000},
        {"Calentado": 4000},
        {"Arepa": 3500},
        {"Cereal": 2500},
        {"Corrientazo": 5000},
        {"Churrazco": 10000},
        {"Tamal": 3000},
        {"Ensalada": 2000}]

carrito = []

opcion = 0

def CalcularTotal():
    
    return total

def AgregarACarrito(platoId):
    carrito.append(platos[platoId])

while opcion != len(platos) + 1:
    
    print("BIENVENIDO.")
    print("Hoy ofrecemos:")
    
    #Para imprimir los elementos de la lista de diccionarios.
    for i, item in enumerate(platos):
        print(f'{i+1}. {list(item.keys())[0]}...........{list(item.values())[0]}')
    
    print("Salir y calcular total.")
    opcion = int(input("Ingrese el plato que desea: "))
    
    if (opcion > 0 and opcion < len(platos)):
        AgregarACarrito(opcion)
        print("El plato seleccionado se ha añadido a la lista de compra.")
        input("Presione una tecla para continuar...")
        
    else:
        CalcularTotal()







platos = {"1. Huevo":3000}
(list(platos.keys())[0])[0]
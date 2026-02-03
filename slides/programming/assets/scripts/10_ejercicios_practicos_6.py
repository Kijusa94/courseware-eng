#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:43:01 2023

@author: kijusa94
"""

Desayuno = {1:"Huevito ranchero", 2:"Pan y café", 3:"Frutica picada", 4:"Tamal y pan"}
Almuerzo = {1:"Carnita asada", 2:"huevo y arroz", 3:"Pollo sudado", 4:"Tilapia", 5:"Frijoles"}
Cena = {1:"Pasta", 2:"Pizza", 3:"Lasagna", 4:"Hamburguesa", 5:"Perro", 6:"Sandwhich"}
tipo_txt = {1:"Desayuno", 2:"Almuerzo", 3:"Cena"}
tipo_log = {1:Desayuno, 2:Almuerzo, 3:Cena}

print("BIENVENIDA")
print("Le ofrecemos:")
for i in range(0, len(tipo_txt)):    
    print(list(tipo_txt.keys())[i], ".", list(tipo_txt.values())[i])
tipo_id = int(input("Ingrese su opción: "))

if (tipo_txt.__contains__(tipo_id)):
    print(f"El menu de {tipo_txt[tipo_id]} tiene los siguientes platos: ")
    for i in range(0, len(tipo_log[tipo_id])):    
        print(list(tipo_log[tipo_id].keys())[i], ".", list(tipo_log[tipo_id].values())[i])
    plato_id = int(input("Ingrese su opción: "))
    
    if (tipo_log[tipo_id].keys().__contains__(plato_id)):
        print(f"Su menu es {tipo_txt[tipo_id]} con el plato {list(tipo_log[tipo_id].values())[plato_id-1]}.")
    else:
        print("Error en la selcción del plato.")    
else:
    print("Ha ingresado un valor no válido.")


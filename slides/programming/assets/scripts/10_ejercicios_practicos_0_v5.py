# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:32:48 2024

@author: juand
"""

"""
Realice un programa que permita:
    Añadir elementos a una lista. Debe revisar que el objeto sea siempre diferente
    Eliminar los elementos de una lista
    Listar los elementos de una lista
    Promediar los valores de la lista
    Salir de la aplicacion
"""

lista = [1, 2, 3]
opcion = 0

while opcion != 5:
    print("MENU")
    print("1. Agregar un dato.")
    print("2. Editar un dato.")
    print("3. Eliminar un dato")
    print("4. Imprimir/Seleccionar un dato")
    print("5. Salir")
    opcion = int(input("Ingrese su opcion: "))
    
    if (opcion == 1):
        valor = int(input("Ingrese el valor a agregar a la lista: "))
        lista.append(valor)
        
    elif (opcion == 2):
        idx = int(input("Ingrese el indice al cual quiere acceder: "))
        lista[idx] = int(input("Ingrese el nuevo valor de la lista: "))
    
    elif (opcion == 3):
        valor = int(input("Indique el valor a eliminar: "))
        lista.remove(valor)
    
    elif (opcion == 4):
        idx = int(input("Ingrese el indice al cual quiere mostrar: "))
        print(f"El valor en la posicion {idx} es {lista[idx]}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
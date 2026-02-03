#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 08:06:25 2023

@author: kijusa94
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
menu_control = 0
print("\014")

while menu_control != 5:
    print("1. Añadir elemento a la lista")
    print("2. Quitar elemento de la lista")
    print("3. Listar los elementos de la lista")
    print("4. Promediar valores de la lista")
    print("5. Salir")
    menu_control = int(input("Ingrese la opción que necesite: "))
    print("\014")
    
    if (menu_control == 1):
        valor = int(input("Inserte el valor a agregar en la lista: "))
        i = 0
        for i in range(0, len(lista)):
            if (valor == lista[i]):
                isListed = True
                break
            else:
                isListed = False
                continue
        
        if (isListed):
            print(f'El numero {valor} ya se encuentra en la lista')
        else:
            lista.append(valor)
            print(f'Se agregó el valor {valor} a la lista')
            
        input("Press Enter to continue...")
        print("\014")
        
        #if(valor in lista):
        #   print(f'El numero {valor} ya se encuentra en la lista')
        #else:
        #   lista.append(valor)
        #   print(f'Se agregó el valor {valor} a la lista')
        
    if (menu_control == 2):
        valor = int(input("Inserte el valor a eliminar de la lista: "))
        try:    
            posicion = lista.index(valor, 0, len(lista))
            print(f'Se eliminó {valor} de la posicion {posicion} de la lista')
            lista.remove(valor)
            input("Press Enter to continue...")
            print("\014")
            
        except Exception as e:
            print(f'El valor {valor} no se encuentra en la lista')
            print(e)
            input("Press Enter to continue...")
            print("\014")
        
    if (menu_control == 3):
        for i in range(0, len(lista)):
            print(lista[i])
        
        input("Press Enter to continue...")
        print("\014")
        
    if (menu_control == 4):
        suma = 0
        for i in lista:
            suma += suma + i
        print('El promedio de los valores en la lista es:', suma/len(lista))
        input("Press Enter to continue...")
        print("\014")
        
"""
EJERCICIO: Añada al codigo anterior las siguientes opciones:
    opción que permita eliminar un valor de la lista mediante el indice/posicion, y otra opcion que permita
    opcion que limpiar/vaciar la lista
    opcion que imprima el maximo valor de la lista
    opcion que imprima el minimo valor de la lista
    opcion que permita contar cuantas veces se repite un numero. Eliminar
    fragmento de codigo que evita introducir numeros repetidos.
"""
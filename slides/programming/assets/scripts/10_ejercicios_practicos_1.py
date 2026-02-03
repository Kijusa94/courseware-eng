#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:27:00 2023

@author: kijusa94
"""

"""
Construya una aplicación de terminal que permita calcular las areas y los volumenes
de diferentes formas (min 3).
"""

import math

print("BIENVENIDO")
print("1. Calcular areas.")
print("2. Calcular volumenes.")
print("3. Salir.")
opcion = int(input("Ingrese la opción que desea: "))

if (opcion == 1):
    print("AREA")
    print("1. Calcular area triangulo.")
    print("2. Calcular area circulo.")
    print("3. Calcular area rectangulo.")
    print("4. Salir.")
    opcion = int(input("Que area desea calcular: "))

    if (opcion == 1):
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        area = base * altura * 0.5
        print(f'El area de la figura es {area}')  
        
    elif (opcion == 2):
        radio = float(input("Ingrese el radio del circulo: "))
        area = (radio ** 2) * math.pi
        print(f'El area de la figura es {area}')
        
    elif (opcion == 3):
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        area = base * altura
        print(f'El area de la figura es {area}')  
    else:
        print("Opcion no valida.")  
        
elif (opcion == 2):
    print("VOLUMEN")
    print("1. Calcular volumen cilindro.")
    print("2. Calcular volumen esfera.")
    print("3. Calcular volumen rombo.")
    print("4. Salir.")
    opcion = int(input("Que area desea calcular: "))

    if (opcion == 1):
        base = float(input("Ingrese la base del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))             
        volumen = base * altura
        print(f'El volumen de la figura es {volumen}')
    
    elif (opcion == 2):
        radio = float(input("Ingrese el radio del circulo: "))
        volumen = 3/4 * math.pi * radio ** 3
        print(f'El volumen de la figura es {volumen}')

    elif (opcion == 3):
        d_menor = float(input("Ingrese el valor de la diagonal menor: "))
        d_mayor = float(input("Ingrese el valor de la diagonal mayor: "))
        volumen = 0.5 * d_menor * d_mayor
        print(f'El volumen de la figura es {volumen}')    
    else:
        print("Opcion no valida.")          
else:
    print("Opcion no valida.")        


"""
EJERCICIO: Complemente el ejercicio anterior con un menú que permita 
calcular el perimetro de tres figuras diferentes.
"""
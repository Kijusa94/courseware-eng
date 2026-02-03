# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:58:30 2024

@author: juand
"""

"""
EJERCICIO 1: ¿MAYOR DE EDAD?
"""
edad = int(input("Ingrese su edad."))

if (edad < 18):
    print("Usted es menor de edad.")
else:
    print("Usted es mayor de edad.")

"""
EJERCICIO 2: VERIFICACION DE CONTRASEÑA
"""
contrasena = "programacion"

dato = input("Usuario, ingrese su contraseña: ")

if (dato == contrasena):
    print("Correcto")
else:
    print("Incorrecto")
    
"""
EJERCICIO 3: Escribir un programa que realice la división de dos numeros. Si el divisor es cero debe generar un error.
"""
#Pedimos el primer valor
num1 = float(input("Ingrese el primer valor: "))

#Pedimos el segundo valor
num2 = float(input("Ingrese el segundo valor: "))

#Revisamos si el segundo valor es diferente de cero. Si es cero, mostramos error.
if (num2 != 0):
    resultado = num1 / num2
    print("El resultado es", resultado)
else:
    print("Error")

"""
EJERCICIO 4: ¿NUMERO PAR O IMPAR?
"""
num = int(input("Ingrese el valor a determinar: "))

if (num % 2 == 0):
    print("El numero es par.")
else:
    print("El numero es impar")

"""
EJERCICIO 5: TRIBUTACION
"""
print("App de Tributación")
edad = float(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))

if (edad > 16 and ingresos >= 1000):
    print("Usted debe tributar.")
else:
    print("Usted NO debe tributar.")

"""
EJERCICIO 6: SALA DE JUEGOS
"""
print("App de sala de juegos.")
edad = int(input("Ingrese su edad: "))

if (edad < 4):
    print("Su entrada es gratis.")
elif (edad > 4 and edad < 18):
    print("Su entrada cuesta 5 euros.")
elif (edad > 18):
    print("Su entrada cuesta 10 euros.")
else:
    print("Ha ingresado un valor no válido.")
    
"""
EJERCICIO 7: PIZZERIA
"""
#%%
opcionesVeggie = {1:"Pimiento", 2:"Tofu"}
opcionesNoVeggie = {1:"Pepperoni", 2:"Jamón", 3:"Salmón"}

print("App pizzeria")
print("BIENVENIDO")
print("Las opciones que tenemos son:")
print("1. Pizza vegetariana")
print("2. Pizza no vegetariana")
opcion = int(input("Ingrese su opción: "))

if (opcion == 1):
    print("La pizza vegetariana tiene los siguientes ingredientes.")
    print("1. Pimiento")
    print("2. Tofu")
    seleccion = int(input("Ingrese su opción: "))
    print(f"Su solicitud es: Una pizza vegetariana con queso mozzarella, tomate y {opcionesVeggie[seleccion]}")
    
if (opcion == 2):
    print("La pizza vegetariana tiene los siguientes ingredientes.")
    print("1. Pepperoni")
    print("2. Jamón")
    print("3. Salmón")
    seleccion = int(input("Ingrese su opción: "))
    print(f"Su solicitud es: Una pizza No vegetariana con queso mozzarella, tomate y {opcionesNoVeggie[seleccion]}")
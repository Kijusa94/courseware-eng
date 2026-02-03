# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 06:54:21 2024

@author: juand
"""
#%%
"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
edad = input("Ingrese su edad: ")

if (int(edad) > 18):
    print("Usted es mayor de edad.")
else:
    print("USted es menor de edad.")
    
#%%
"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas
"""
contrasena = "programacion123"

valor = input("Ingrese su contraseña: ")

if (valor == contrasena):
    print("Acceso permitido.")
else:
    print("Acceso denegado.")

#%%
"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""
num1 = float(input("Ingrese el primer valor: "))
num2 = float(input("Ingrese el segundo valor: "))

if (num2 == 0):
    print("ERROR")
else:
    print(num1 / num2)

#%%
"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar
"""
num = int(input("Ingrese el valor a evaluar: "))

if (num % 2 == 0):
    print("Es par.")
else:
    print("Es impar.")

#%%
"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Inserte sus ingresos: "))

if (edad > 16 and ingresos >= 1000):
    print("Usted debe tributar.")
else:
    print("Usted no debe tributar.")
    
#%%
"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""
print("APP PARA SALA DE JUEGOS")

try:
    edad = int(input("Ingrese su edad:"))
    
    if (edad > 0 and edad < 4):
        print("Entrada gratis.")
    elif (edad > 4 and edad < 18):
        print("Costo de entrada es 5 euros.")
    elif (edad > 18):
        print("Costo de la entrada es 10 euros")
    else:
        print("Ha ingresado un valor no válido.")
    
except:
    print("ERROR")


#%%
"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""
tipoPizza = {1:"Veggie", 2:"No Veggie", 3:"Hawaii", 4:"Solo carnes"}
ingredientesPizzaVeggie = {1:"Pimiento", 2:"Tofu", 3:"Cebolla"}
ingredientesPizzaNoVeggie = {1:"Pepperoni", 2:"Jamon", 3:"Salmon"}

print("APP DE PIZZERIA")

print("Bienvenido.")

for i in tipoPizza:
    print(f"{i}. {tipoPizza[i]}")

opcion = int(input("Ingrese la opción deseada: "))

#%%
print("1. Opción vegetariana")
print("2. Opción no vegetariana")

opcion = int(input("Ingrese la opción deseada: "))
    
if (opcion == 1):
    print("Usted escogió la pizza vegetariana. Los ingredientes son:")
    print("1. Pimiento.")
    print("2. Tofu")
    opcion = int(input("Ingrese el ingrediente que desea: "))
    
    if (opcion == 1):
        print("Usted escogió pimiento.")
    elif(opcion == 2):
        print("Usted escogió tofu.")
    else:
        print("Ha ingresado una opción no válida.")
    
elif (opcion == 2):
    print("Usted escogió la pizza no vegetariana. Los ingredientes son:")
    print("1. Pepperoni.")
    print("2. Jamon")
    print("3. Salmon")
    opcion = int(input("Ingrese el ingrediente que desea: "))
    
    if (opcion == 1):
        print("Usted escogió pepperoni.")
    elif(opcion == 2):
        print("Usted escogió jamon.")
    elif(opcion == 3):
        print("Usted escogió salmon.")
    else:
        print("Ha ingresado una opción no válida.")

else:
    print("Ha ingresado una opción no válida.")
    
    
"""

"""
    
    


























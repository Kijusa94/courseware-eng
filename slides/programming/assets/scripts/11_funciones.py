#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:32:04 2023

@author: kijusa94
"""

"""
Como hemos visto, hay situaciones en nuestros programas en las que necesitamos
ejecutar las mismas tareas mas de una vez. En esas situaciones se recurre a 
utilizar las funciones o metodos. Estos son fragmentos o bloques de código
que realizan una tarea en especifico.

Su utilidad radica en que a pesar de realizar una tarea, tienen la capacidad
de recibir diferentes parametros/valores para dicha tarea. Lo que permite ser
recursivos cuando necesitamos ejecutar tareas repetitivas con pequeños cambios

Las funciones tienen dos partes:
    -La definición de la función: En donde establecemos las sentencias que 
    realizará la función
    -El llamado de la función: Donde queremos que ejecute la función
    
Veamos un ejemplo:
"""
def Factorial(num):
    resultado = 1
    for i in range(num):
        resultado *= i + 1 
    return resultado

numero = Factorial(3)/Factorial(3) + Factorial(2)
print(numero)


numero2 = int(input("Ingrese un numero para calcular su factorial: "))
print(f'El factorial de {numero2} es {Factorial(numero2)}')

"""
La función anterior calcula el factorial de un numero. Observe que el valor
ingresado puede ser cualquier valor entero positivo.
Para que la función se defina, utilizamos la palabra reservada 'def'. Esto indica
el inicio de sentencias a realizar por la función.

En la definición de la función, observamos que entre los parentesis se define
una variable llamada 'num'. Esta es conocida como 'parametro de entrada', y es
una variable que almacena el valor ingresado al llamar la función.

Así mismo, observamos que al ejecutar las sentencias de la función, cerramos
con la palabra clave 'return'. Esta indica el valor retornado por la función
al ciclo de ejecución principal. A este se le llama 'parametro de salida'.
En la medida de lo posible, se busca que se retorne solo un elemento por funcion,
ya sea un numero o un objeto, a pesar de que se pueden retornar varios
resultados mediante comas.

NOTA: Si en nuestras funciones existen bifurcaciones (condicionales), y se debe
retornar un valor, hay que considerar un 'return' por cada caso que se pueda
presentar.

Finalmente, se observa que en la función print realizamos el llamado de la
función para que nos arroje el resultado del bloque de 'Factorial' en pantalla
"""

"""
Veamos un ejemplo que permite ver el potencial de las funciones:
    Mediante un programa queremos calcular la permutacion de un conjunto de
    numeros. El código que se presenta a continuación, permite realizar dicho
    calculo.
"""

import math

menu_control = 0
print("\014")

while menu_control != 2:
    print("1. Calculo de permutaciones")
    print("2. Salir")
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
        r = int(input("Ingrese el valor de r:"))
        
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
Sin embargo, observemos que el calculo del factorial se repite
en dos situaciones. Por tanto, podemos utilizar funciones para
ser recursivos en este programa
"""
#%%
menu_control = 0
print("\014")

def Factorial(num):
    factorial = 1
    for i in range(num):
        factorial *= i + 1 
    return factorial

while menu_control != 2:
    print("1. Calculo de permutaciones")
    print("2. Salir")
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
        
        resultado = Factorial(N)/Factorial(N-r)
        
        print("El factorial {0} P {1} = {2}".format(N, r, resultado))
        
        input("Press Enter to continue...")
        print("\014")

#%%
"""
EJERCICIO: Elabore una función que permita calcular la combinatoria de un 
conjunto. La función tendrá por parametro el valor de 'N' y el valor de 'r'
"""
def Factorial(num):
    factorial = 1
    for i in range(num):
        factorial = factorial * (i + 1) 
    return factorial

def Combinatoria(N, r):
    #INGRESE SU CODIGO AQUI
    combinatoria = 0    
    combinatoria = Factorial(N)/(Factorial(r)*Factorial(N-r))
    
    return combinatoria

ValorN = int(input("Ingrese el valor N de la combinatoria: "))
ValorR = int(input("Ingrese el valor r de la combinatoria: "))
print(f'La combinatoria {ValorN} C {ValorR} = {Combinatoria(ValorN,ValorR)}')

#%%
pizza = {1:"Hawaiana", 2:"Peperonni", 3:"Jamon y queso", 4:"Pollo y champiñones", 5:"Mexicana", 6:"Napolitana", 7:"Picante", 8:"Maiz con tocineta", 9:"Criolla", 10:"Con carne"}

combo = {1:"gaseosa", 2:"papas", 3:"todo", 4:"Sin combo"}

precioPizza = 5000
precioDomicilio = 5000
precioCombo = {1:1000, 2: 2500, 3:3000, 4:0}

totalPedidos = []

def ImprimirMenu():
    print("===BIENVENIDO===")
    print("Aplicacion para gestión de pedidos de pizza")
    print("Seleccione su opción")
    
    for i in pizza.items():
        print(f"{i[0]}. {i[1]}")

def ImprimirMenuPizza():
    print("Escoja sus preferencias")
    print("1. Combo gaseosa")
    print("2. Combo papas")
    print("3. Combo pizza + gaseosa + salsa")
    print("4. Sin combo")
    
while True:
    ImprimirMenu()
    opcion = int(input("Ingrese su pizza favorita: "))
    
    if (opcion != 5):
        ImprimirMenuPizza()
        opcionCombo = int(input("Escoja su combo: "))
        
        print(f"Usted selecciona una pizza {pizza[opcion]} y la pidió con el combo {combo[opcionCombo]}")
        
        precio = precioPizza + precioCombo[opcionCombo]
        
        pedido = [opcion, opcionCombo, precio]
        
        totalPedidos.append(pedido)
        
    elif (opcion == 5):
        print("¿Desea su pedido a domicilio?:")
        print("1. Si")
        print("2. No")
        opcionDomicilio = int(input("Seleccione su opcion: "))
        
        if (opcionDomicilio == 1):
            precioDomicilio = 5000
        else:
            precioDomicilio = 0
        
        print("Su pedido fue: ")
        precioTotal = 0
        for i in totalPedidos:
            precioTotal = precioTotal + i[2]
            print(f"Pizza {pizza[i[0]]} con combo {combo[i[1]]}")
        print("Total a pagar: ", precioTotal + precioDomicilio)
        break














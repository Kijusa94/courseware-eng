#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:22:19 2023

@author: kijusa94
"""

"""
Pyhton funciona bajo un flujo de trabajo secuencial, en donde las instrucciones
se ejecutan una detras de otra. Por ejemplo:
"""
numero1 = 10
numero2 = 20
resultado = numero1 + numero2

"""
Sin embargo, en programación existen flujos de trabajo diferentes que permiten
afectar la ejecución de tareas dependiendo de condiciones.

En ciertas circunstancias, requerimos repetir las instrucciones una cierta
cantidad de veces o hasta cumplir una condición determinada. A los primeros,
se les llama ciclo 'for', a los segundos ciclos 'while'.

En ambos casos, empezamos con una inicializacion, despues realizamos el ciclo,
y finalmente, ejecutamos alguna tarea de finalización, si se requiere.
"""

"""
Veamos el ciclo 'while' con un ejemplo.
Crearemos una lista de mensajes en las que se muestre el valor de un numero
que se reducira de uno en uno hasta alcanzar un valor igual a cero.
"""
#%%
a = 10
while a > 0:                                
    print("El valor de 'a' es: " + str(a))
    a -= 1  #a = a - 1
print("Se terminan las iteraciones")
#%%
"""
Hay que tener presente la condicion del ciclo 'while'. Si no se es cuidadoso,
el programa nunca terminará su ejecución, pues quedará atrapado en el ciclo.

EJERCICIO: Cambié la operación de resta por una de suma, y concluya sobre lo 
ocurrido.
"""



"""
Veamos ahora el ciclo 'for' con un ejemplo.
Crearemos un ciclo para descomponer una palabra en las letras que la conforman.
"""
#%%
cadena = "palabras"
cadena[2:]
for i in cadena:
    print(i)
    print("terminamos ciclo 'for'")
#%%
"""Veamos otro ejemplo en el que imprimimos los elementos de una lista"""
#%%
lista = ["Pedro", "Pablo", "Carlos", "Jhon", "Yamil", "Balanta"]

for idx in range(1,len(lista), 2):
    print(lista[idx])
print("Terminamos ciclo 'for'")
#%%

"""
Los bucles tienen palabras especiales que permiten controlar la ejecución del
ciclo. Ellos son 'break' y 'continue'.

'break' es utilizado para cortar la ejecución del cilo. Retornando el interprete
a la linea de codigo siguiente a las instrucciones del ciclo.

'continue' es utilizado para saltar la ejecución del ciclo.

Veamos su uso a traves de los siguientes ejemplos. 

En el primer ejemplo, tenemos que se listarán las letras de una palabra hasta
que se encuentre una letra 'b'.
"""
#%%
cadena = "palabras"

for letra in cadena:
    if letra != 'b':
        print(letra)
    else:
        print("Encontré la letra b")
        break
print("terminamos ciclo 'for'")
#%%
"""
En el segundo ejemplo, saltaremos al segundo elemento en la lista.
"""
#%%
lista = ["Pedro", "Pablo", "Carlos", "Jhon"]

for i in range(0,len(lista)):
    if i == 1:
        continue
    print(lista[i])
print("Terminamos ciclo 'for'")
#%%

"""
EJERCICIO: Realice un código que permita listar los numeros del uno al cien, pero que no incluya aquellos numeros que son divisibles entre 3
"""
#%%
for i in range(0,100):
    if (i % 3 != 0):
        print(i)
#%%
"""
EJERCICIO: Suma de numeros pares de 2 a 100
"""
suma = 0
for numero in range(2, 100, 2):
    suma += numero
print(suma)


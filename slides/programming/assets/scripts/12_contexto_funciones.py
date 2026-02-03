#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:03:33 2023

@author: kijusa94
"""

"""
Cuando creamos funciones hay que tener cuidado con el contexto de las variables.
Cada bloque identado tiene su propio contexto y las variables que se crean dentro
de ese bloque solamente son accesibles dentro de ese bloque.

Programa principal
var_global = valor

    funcion nombre_funcion()
        var_local = valor

Las variables que pueden ser manipuladas en el todo el programa se denominan
'variables globales'; aquellas que se definen dentro de un bloque/contexto/funcion
se denominan 'variables locales'.

Veamos el siguiente ejemplo.
"""


var_global = 7

def funcionContexto(parametro):
    var_local = 100
    print(f'La variable global es: {var_global}')
    print(f'La variable local es: {var_local}')
    print(f'El parametro de entrada es: {parametro}')
    
funcionContexto('entrada')

#Si intentamos acceder a la variable global, no hay problema.
print(f'La variable global sigue valiendo: {var_global}')

#Si intentamos acceder a la variable local, se genera ERROR. Elimine '#'
#print(f'el valor de la variable local es: {var_local}')

#Si intentamos acceder a la variable parametro, se genera ERROR. Elimine '#'
#print(f'el valor de la variable parametro es: {parametro}')


"""
Sin embargo, si podemos editar los valores de variables globales en funciones
Para ello utiizamos la palabra clave 'global'
"""
def funcionCambioGlobal():
    global var_global
    var_global = 2
    
funcionCambioGlobal()

print(f'Observe que var_global cambia a un nuevo valor {var_global}')


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias",  child3 = "Linus")



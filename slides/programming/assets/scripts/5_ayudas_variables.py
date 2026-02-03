#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:28:22 2023

@author: kijusa94
"""
"""
A veces es necesario identificar el tipo de dato que estamos manejando. 
Es muy útil cuando queremos hacer una serie de operaciones y no sabemos que
es lo que nos está llegando
Algunas funciones que lo permiten son:
    type()
"""
type(1234)
type([1,2,3,4])
type((1,2,3,4))
type({"1":"uno", "2":"dos"})

cadena = "hola mundo"
type(cadena)

numero = 23
type(numero)


"""
Otra fución que ayuda a determinar el tipo de dato de una variable o una
función es: "help()"
"""
help(int)
import math
help(math)

"""
Simplemente, help y entre paréntesis aquello que tengamos dudas de cómo
funciona y muchas veces con la ayuda que vienen python no necesitaremos
buscar en internet cómo hacer las cosas porque el propio python ya nos dice
que es lo que podemos hacer con ello.
"""

"""
Una función que permite conocer las dependencias de una tipo de dato es dir.
Esta nos permite ver los atributos y funciones de un objeto. Podemos pasar 
el tipo de dato o la variable como tal.
Veamos algunos ejemplos:
"""
dir(int)            #Pasando un tipo de dato
dir([1,2,3,4])      #Pasando una lista
a = [1,2,3,4]       
dir(a)              #Pasando una variable definida


"""
Por otra parte, tenemos funciones de conversión, que como indican, permite
convertir o representar un tipo de dato en otro, siempre y cuando cumplan
ciertas condiciones. 
int()
float()
ord()
hex()
oct()
tuple()
set()
list()
dict()
str()
"""
numero = 3
cadena = "245"
suma = numero + int(cadena)


"""
Por último y no menos importante, tenemos la función 'input', la cual permite
ingresar al usuario una valor mediante el terminal. Esto resulta práctico
para determinar lo que quiere un usuario, y a partir de ello, realizar una
accion.
"""
numero = input("Ingrese un valor numerico: ")
type(numero)

"""
NOTA: Tenga presente que la función input recibe el valor ingresado en formato de
cadena de texto.
"""
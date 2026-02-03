# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:32:42 2024

@author: juand
"""

"""
Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""
def CalcularIVA(valor, iva):
    resultado = valor + (valor * iva)
    return resultado

precio = float(input("Ingrese el valor del producto: "))
porcentaje = float(input("Ingrese el porcentaje del IVA: "))
print("El producto mas iva cuesta: ", CalcularIVA(precio, porcentaje/100))

"""
Ejercicio 2
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
"""
def MostrarMensaje(nombre):
    print(f"Hola {nombre}!")
    
MostrarMensaje('Juan')

"""
Ejercicio 5
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
"""
import math

def CalcularAreaCirculo(radio):
    area = math.pi * radio ** 2
    return area

def CalcularVolumenCilindro(radio, altura):
    volumen = CalcularAreaCirculo(radio) * altura
    return volumen

CalcularVolumenCilindro(2, 2)

#%%
"""
Ejercicio 6
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""
def CalcularPromedio(lista):
    suma = 0;
    for i in lista:
        suma = suma + i
    promedio = suma / len(lista)
    return promedio

lista = [11,12,5,20,10,20, 60, 100]

CalcularPromedio(lista)

#%%
"""
Ejercicio 7
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""
lista = [3, 6, 9, 12, 15]

def CalcularCuadradosLista(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] ** 2
    return lista

CalcularCuadradosLista(lista)

#%%
"""
Cree una función que calcule el area de un rectangulo. Debe recibir como parametro el ancho y el alto, y debe retornar el valor del area.
"""
def CalcularAreaRectangulo(base , altura):
    area = base * altura
    return area

CalcularAreaRectangulo(5, 4)

#%%
"""
Escriba un programa que pida la anchura de un triángulo y lo dibuje con caracteres producto (*): Ejemplo: Si la anchura es 4, debe mostrar:
*
**
***
****
***
**
*
"""
def DibujarTriangulo(anchura):
    for i in range(anchura):
        print('*' * (i + 1))
    for j in range(anchura, 0, -1):
        print('*' * (j))
        
DibujarTriangulo(10)

#%%
"""
Escriba un programa que permita crear una lista de palabras (que puede ser vacía). Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
"""










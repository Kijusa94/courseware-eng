#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:57:20 2023

@author: kijusa94
"""

"""
A partir de lo aprendido, realice un código que cuente el numero de lineas 
del archivo ejercicio.csv
"""
archivo = open('ejercicio.csv','r')
i = 0
for line in archivo:
    i += 1
print(f'el documento {archivo.name}tiene {i} lineas')
archivo.close()
   

"""
Modifique el ejercicio anterior, para que muestre en pantalla aquellas
lineas en las que aparece la palabra 'run'
"""
archivo = open('ejercicio.csv','r')
for line in archivo:
    if ('run' in line):
        print(line.strip())
archivo.close()


"""
EJERCICIO: Modifique el código anterior para contar el numero total de palabras
del documento.
"""

"""
Modifique el primer código para que permita abrir un archivo indicado por el
usuario
"""
nom_archivo = input('Ingrese el nombre del archivo: ')
try:
    archivo = open(nom_archivo,'r')
    for line in archivo:
        print(line)
    archivo.close()
except:
    print('No se encuentra el archivo especificado')













#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:22:01 2023

@author: kijusa94
"""

"""
En este código profundizaremos en las cadenas de texto.
Podemos utilizar simbolos para organizar nuestras cadenas de texto
"""

#Concatenar cadenas de texto
cadena1 = "Hay que estar pendiente del examén sorpresa de programación."
cadena2 = "Ese cucho está loco!."
cadena = cadena1 + cadena2

print(cadena)

#Los \ ayudan a organizar cadenas muy extensas.
#OJO NO DEBEN HABER ESPACIOS DEPUES DEL SIMBOLO '\'
cadena = "Hay que estar pendiente del examén"\
    " sorpresa de programación."\
    " Ese profesor está loco!."
    
print(cadena)

#En los textos podemos agregar saltos de linea
cadena = "Hay que estar pendiente del examén \n"\
    " sorpresa de programación.\n"\
    " Ese profesor está loco!."
    
print(cadena)

#Tambien podemos usar comilla triple. Pero ojo, las tabulaciones se tendran en cuenta
cadena = ''' Hay que estar pendiente del examén sorpresa de programación.
    Ese cucho está loco!.'''
    
print(cadena)




"""
Podemos extraer los caracteres que componen las cadenas.
"""
cadena = "Hay que estar pendiente del examén sorpresa de programación. Ese cucho está loco!."

#Para obtener la longitud de la cadena. Usamos:
len(cadena)

#Para acceder a un caracter
cadena[30]

#Podemos obtener trozos de la cadena
cadena[0:10]
cadena[10:20]
cadena[:10]
cadena[10:]
cadena[:-5]
cadena[-5:]


"""
¿Qué podemos hacer con las cadeas?
"""
cadena = "Hay que estar pendiente del examén sorpresa de programación. Ese cucho está loco!."

#Pone el texto en minuscula
cadena.lower()

#Pone el texto en mayuscula
cadena.upper()

#Pone solo la primera letra en mayuscula
cadena.capitalize()

#Cambia una palabra de la cadena por otra
cadena.replace('cucho','profesor')

#Retorna el indice en el que se encuentra la primera letra de la palabra a buscar
#La busqueda es MAYUS SENSITIVE
cadena.find('loco')  #Si retorna -1 es porque no se encuentra

#Podemos encadenar funciones
cadena.lower().find('loco')

#Podemos eliminar los espacios como saltos de linea
cadena.strip()

#Podemos separar la cedena y convertirlo en una lista de palabras
cadena.split()

#Podemos separar usando un caracter de separacion
cadena.split('.')



"""

"""
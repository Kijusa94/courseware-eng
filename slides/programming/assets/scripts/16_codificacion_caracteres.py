#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:26:49 2023

@author: kijusa94
"""

"""
Representacion de texto mediante convencion ASCII.
ASCII viene de American Standard Code for Information Interchange. Es una
convención que permite escribir un caracter mediante un código especifico.
Este se representa en un código binario compuesto de 7 bits. Sin embargo,
es habitual encontrarlo descrito mediante un codigo decimal.

Por ejemplo, el simbolo '@' representado en código ASCII es 64. Por eso, al
presionar 'Alt + 64' escribimos en pantalla el simbolo '@'. Este valor '64'
se representa en forma de bits como 0110 (6) y 100 (4).

Sin embargo, el código ASCII se ve limitado debido a que solo permite
representar un total de 128 caracteres diferentes (2^7 = 128). Por lo que, 
se creo la convención Unicode
"""

"""
Representacion Universal Unicode y UTF-8
Este es una tabla ampliada que permite describir cada caracter mediante un
codigo. Es Universal (para todos los idiomas), uniforme (codificacion) y es
unico (representacion unica de cada caracter).

Unicode utiliza el esquema de codificacion UTF-8.

Tamaño      UTF-8                           Uso
1 byte      0xxxxxx                         ASCII
2 bytes     110yyyyy 10xxxxxx               romance, greek, arab...
3 bytes     1110zzzz 10yyyyyy 10xxxxxx      CJK
4 bytes     ....                            suplemental
"""

"""
La importancia de estas convenciones es que nos permiten traducir un conjunto
de letras a un código binario que puede ser interpretado por el ordenador.
Es importante conocer que codificacion utilizan las aplicaciones para que
las representaciones sean las correctas. 
"""

#Con la función ord() podemos conocer el codigo Unicode de un caracter
print(ord('a'))

#Con la funcion chr() podemos conocer el caracter correspondiente a un codigo
print(chr(89))

#Tambien, podemos conocer los codigos que componen una cadena
cadena = 'El perro de Roque'
for letra in cadena:
    print(ord(letra), end=" ")
    
#Esto puede ser util cuando queremos codificar mensajes. Cifraado Cesar
#Tambien llamado cifrado por desplazamiento.
cadena = 'Este es mi mensaje'
cifrado =''
desplazamiento = 5

#Codificacion
for letra in cadena:
    cifrado = cifrado + chr(ord(letra) + desplazamiento)
    
#Decodificacion
descifrado = ''
for letra in cifrado:
    descifrado = descifrado + chr(ord(letra) - desplazamiento)
    
print(f'Este es mi mensaje original: {cadena}')
print(f'Este es mi mensaje codificado: {cifrado}')
print(f'Este es mi mensaje decodificado: {descifrado}')













 
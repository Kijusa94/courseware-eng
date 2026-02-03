#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:06:42 2023

@author: kijusa94
"""

"""
En esta sección hablaremos de las operaciones que pueden realizar las variables
Iniciaremos con las operaciones aritmeticas:
"""
numero1 = 3
numero2 = 2

suma = numero1 + numero2            #Suma
resta = numero1 - numero2           #Resta
producto = numero1 * numero2        #Multiplicacion
cociente = numero1 / numero2        #Division

modulo = numero1 % numero2          #Residuo de la división
potenciacion = numero1**numero2     #Exponente

negacion = -numero1                 #Ponemos menos para negar el numero

"""
Tenga presente que al programar se tiene la misma precendencia (orden de
operaciones) que en matematicas. Negacion > potencia > modulo > cociente ...
Si tienen el mismo nivel de precedencia (como lo es la division y el producto)
las operaciones se realizan en orden de izqierda a derecha

Puede utilizar parentesis para indicar la precedencia que considere.
"""

"""
Otro tipo de operaciones con valores numericos, se denominan operaciones 
logicas. Estas arrojan resultados booleanos al comparar valores numericos.
"""
numero1 = 3
numero2 = 5

numero1 < numero2       #Operacion menor que. Resultado: True
numero1 <= numero2      #Operacion menor o igual que. Resultado: True
numero1 > numero2       #Operacion mayor que. Resultado: False
numero1 >= numero2      #Operacion mayor o igual que. Resultado: False
numero1 == numero2      #Operacion igual que. Resultado: False
                        #Es con doble igual porque es comparacion, no asignacion
                        
"aa" is "a"*2           #Comparacion de igualdad de memoria. Retorna True.
                        #porque las operaciones no estan alojadas en memoria

letraA = "a"
"aa" is letraA*2        #Comparacion de igualdad de memoria. Retorna False.
                        #porque la variable letraA está alojada en memoria.
                        
"""
Tambien se tiene conectores logicos para realzar algebra booleana. Entre ellos
esta: 'y', 'o' y 'not'
"""
boolean1 = True
boolean2 = False

boolean1 and boolean2
boolean1 or boolean2
not boolean1


"""
En Python tambien tenemos operaciones con cadenas de texto. Algunos ejemplos
"""
cadena1 = "hola "
numero = 5

cadena2 = cadena1 + "mundo"
cadena2 = cadena1 * 5

f'la cadena de texto completa es {cadena2}'
f'el valor del numero es {numero}'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:58:45 2023

@author: kijusa94
"""

"""
Una de las cosas que podemos hacer en Python es que las variables sean 
las que llaman a las funciones.

Otra de las cosas que podemos hacer, es encadenar llamadas de variables.
"""
print("\014")

mitexto = "Hay que estar pendiente del examén sorpresa de programación. Ese cucho está loco!."

#help(str)

str.title(mitexto)


"""
Al ser mitexto una cadena de texto, podemos llamar directamente a la funcion.
"""

mitexto.title()

"""
Tambien podemos encadenar llamadas
"""

mitexto.replace('cucho', 'profesor').title()
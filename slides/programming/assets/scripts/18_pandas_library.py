#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:00:50 2023

@author: kijusa94
"""

"""
Pandas es una potente librería que
se utiliza dentro del lenguaje Python y está especialmente
indicada para trabajar con datos almacenados en hojas de cálculo,

Además, proporciona un conjunto de estructuras optimizadas
para trabajar con series temporales. Pandas puede
trabajar con ficheros de tipo texto, como los CSV, o también,
los ficheros de Excel, que también están formados por filas y columnas.
Por último, es importante señalar que la librería Pandas,
a diferencia de la librería Numpy, puede trabajar con cualquier
tipo de datos, no trabaja sólo con números, como hace Numpy.
"""

import pandas as pd
import random

"""
Pandas utiliza una estructura de datos denominada 'Serie', esta contiene
dos vectores: El indice y los datos. La siguiente linea muestar como se crea
una serie a partir del constructor de la estructura de datos.
"""
s = pd.Series(['Enero','Febrero','Marzo','Abril'])
print(s)

"""
El indice puede ser alfanumerico. Utilizamos el parametro index para ajustar
esto
"""
s = pd.Series(['Enero','Febrero','Marzo','Abril'], index=['a','b','c','d'])

"""
El indice puede ser una fecha
"""
#Crea 5 fechas/dias empezando desde 2022-01-01
fechas = pd.date_range('20220101',periods=5)

#Crea 5 numeros aleatorios del 1 al 50 y los almacena en datos. Requiere
#modulo random
datos = [random.randrange(1, 50, 1) for i in range(5)]

#Crea la serie con los datos generados
s = pd.Series(datos)
print(s)

"""
Para acceder a los datos. Utilizamos los corchetes de forma similar a como
se utiliza en las listas
"""
#Acceso a las posicion 0 de la serie
print(s[0])

#Acceso a la posicion 2 de la serie
print(s[2])


"""
También podemos utilizar funciones matematicas sobre las series. Por
ejemplo:
"""
#Sumatoria de los valores de la serie
print(s.sum())

#Promedio de los valores de las serie
s.mean()
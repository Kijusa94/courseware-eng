#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:19:18 2023

@author: kijusa94
"""

"""
Un DataFrame es un conjunto de datos con estructura matricial,
es decir, que está formado por filas y columnas. Como ya
sabemos lo que es una Serie, podemos definir un DataFrame como
un conjunto de series que comparten un mismo índice. Pueden
almacenar cualquier tipo de dato, no solo números, y por lo
tanto, al trabajar con filas y columnas, con datos matriciales,
pues, son muy apropiados para trabajar con hojas de cálculo.

Se puede connstruir un dataframe de diferentes maneras.
"""
import pandas as pd

#Creacion de dataframe mediante listas
df = pd.DataFrame(data = [('Enero',177643,12475,996,2564),
                          ('Febrero',33727,3278,333,1364),
                          ('Marzo',4457,482,75,172)],
                  columns=['Mes','Casos','Hospitalizados','UCI','Fallecidos'])

print(df)

#Creacion de dataframe mediante diccionarios
df = pd.DataFrame({'Mes': ['Enero','Febrero','Marzo'], 
                   'Casos':[177643,33727,4457], 
                   'Hospitalizados':[12475,3278,482], 
                   'UCI':[996,333,75], 
                   'Fallecidos':[2564,1364,172] })

"""
Generalmente, cargamos los datos de un csv o archivo de Excel. Los dataframes
permiten todo tipo de operaciones:
    Agruparlos por valores de columnas
    Calcular sumas, medias, medianas, maximos, minimos, de valores agrupados
    Seleccionar filas o columnas con ciertos valores
    Concatenar, mezclar, combinar varios dataframes
"""

df.Casos.min()
print(df.Casos.mean())

"""
A Continuacion se lista algunos de los metodos típicos en el uso de 
dataframes.
"""

#Indica la dimension del dataframe
len(df)

#Indica las caracteristicas del indice
df.index

#Lista los valores del dataframe. Retorna una lista con los valores de la serie
df.values

#Indica los encabezados de las columnas y sus caracteristicas
df.columns

"""
Por otro lado, podemos utilizar la función describe, que lo
que nos hace es, nos calcula un montón de operaciones
de cada una de las columnas numéricas. Nos dice cuántos elementos son
no nulos, en este caso, tres, tres, tres, de cada columna; nos calcula la media,
la varianza, el mínimo y el máximo, y los tres cuartiles del
veinticinco, cincuenta y el setenta y cinco por cien.
El cincuenta por cien sería la mediana, en este caso.
"""
df.describe()


"""
También podemos pasarle el DataFrame info, que nos da información 
sobre las columnas, el tipo de cuál es cada columna y cuántos valores
no nulos tiene.
"""
df.info()

"""
También, podemos modificar el formato
de cómo se visualiza esta información. Por ejemplo, Pandas tiene
la orden set_ option y aquí, vamos a indicarle que el formato para visualizar
datos de tipo float es con dos decimales
"""
pd.set_option('display.float_format','{:.2f}'.format)
df.describe()

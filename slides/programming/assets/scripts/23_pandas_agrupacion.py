#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:13:24 2023

@author: kijusa94
"""

"""
Agrupar los datos de un DataFrame, es una herramienta
muy potente. Con los datos agrupados se pueden realizar
varios calculos matematicos con datos repetidos, por ejemplo, una categoría de
un artículo, una fecha, un nombre de un cliente.

Para realizar las agrupaciones se utiliza el metodo
groupby:
    
    df.groupby(by=None, axis=0, sort=True, as_index=True, dropna=True)
    
-by: indica las columnas que se utilizan para agrupar
-axis: lo hace por filas si es 0, o por columnas si es 1
-sort: ordena por las claves espcificadas en by
-as_index: si la clave será indice o no
dropna: elimina las filas que tengan valores nulos.
"""

import pandas as pd

df = pd.read_csv('ejercicio.csv', encoding='utf-8')

#%%
"""
Estos datos agrupados pueden ser operados de las siguientes formas:
    
Agrupamos por una columna que tenga datos repetidos, y seleccionamos una 
columna que no tenga elementos repetidos ni nulos.
"""
#Queremos saber cuantas personas realizaron cada tipo de dieta
df.groupby(by='diet', as_index=False)['n'].count()

#Queremos saber cuantas personas tuvieron cada tipo de pulso
df.groupby(by='pulse', as_index=False)['n'].count()

#Queremos saber el promedio de pulso de los participantes que hicieron cada dieta
df.groupby(by='diet', as_index=False)['pulse'].mean()

#Queremos saber cual fue el maximo pulso de cada tipo de tratamiento
df.groupby(by='kind', as_index=False)['pulse'].max()

"""
Se pueden reordenar los datos obtenidos
"""
##Queremos saber cuantas personas tuvieron un cierto ritmo cardiaco
#Organicemos el resultado con aquellos ritmos mas frecuentes
(df.groupby(by='pulse', as_index=False)['id'].count()).sort_values(by='id', ascending=False)

#Queremos saber cual fue el maximo pulso de cada tipo de tratamiento
#Organicemos el resultado por el tipo de tratamiento con el pulso mas alto
(df.groupby(by='kind', as_index=False)['pulse'].max()).sort_values(by='pulse', ascending=False)

"""
Otras operaciones a considerar:
    Mediana: median()
    Varianza: std()
    Maximo: max()
    Minimo: min()
    
Así mimo se pueden obtener varias estadisticas a la vez:
    Utilizamos agg ('agregate') recibe el nombre de las funciones para
    agregar al calculo.
"""
#Conocer el promedio, min y maximo de pulso en las diferentes dietas
df.groupby(by='diet').agg({'pulse':['mean','min','max']})

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:53:08 2023

@author: kijusa94
"""

"""
En esta sección veremos como acceder a los datos de un
dataframe. Para eso veremos como estan definidas las
filas y columnas.
Metodos: iloc, loc, iat, at, get_loc, get_indexer.
"""
import pandas as pd

#Creacion de dataframe mediante listas
df = pd.DataFrame(data = [('Enero',177643,12475,996,2564),
                          ('Febrero',33727,3278,333,1364),
                          ('Marzo',4457,482,75,172)],
                  columns=['Mes','Casos','Hospitalizados','UCI','Fallecidos'],
                  index=list('abc'))

#%%
"""
Para referenciar las filas, podemos usar el indice o la
etiqueta de la fila. Así mismo para las columnas.
"""
#Si etiqueta de la columna no tiene espacios, accedemos
#con el operador punto. #Si la etiqueta si tiene espacios
#accedemos como si fuera una lista. TENGA PRESENTE QUE ES
#CAPS_SENSITIVE.
df.Mes
df['Mes']

#Tambien podemos acceder a un rango de filas
df[0:2]         #Con el indice es rango abierto/no incluye
df['a':'b']     #Con la etiqueta es rango cerrado/incluye

#%%
"""
Podemos seleccionar los datos por posicion mediante los
metodos iloc. Tiene dos parametros que seleccionan los
rangos.
    df.iloc[<filas>,<columnas>]
-El valor inicial es 0
-Si se omite el primer valor se asume 0, si se omite el 
    segundo valor se asume el ultimo
-Se se omite <columnas> las devuelve todas.
-Se utilizan valores negativos para indexar desde la ultima
    posicion
"""
df.iloc[0]          # primera fila
df.iloc[-2]         # penúltima fila
df.iloc[:,1]        # segunda columna
df.iloc[:,-2]       # penúltima columna
df.iloc[0:2]        # primera y segunda fila
df.iloc[0:1,[0,1,3]]  # 

#%%
"""
Por su parte, el metodo loc permite seleccionar filas y
columnas mediante la etiqueta. Sigue los mismos criterios
que iloc.
"""
df.loc['a']                     # primera fila
df.loc['c']                     # última fila
df.loc[:,'Casos']               # segunda columna
df.loc['a':'b']                 # todas las filas
df.loc[:,'UCI']                # penúltima columna
df.loc[:,['Mes','Casos','UCI']] # primera, segunda y cuarta columna

#Tambien puede utilizar operaciones boolenas
df.loc[df.loc[:,'Mes'] == 'Enero']
df.loc[df.Mes=='Enero']         #De forma abreviada.

#%%
"""
Para acceder a los datos especificos de la fila y la 
columna utilizamos el metodo 'iat' (utiliza indices) y 
'at' (utiliza etiquetas).
"""
df.iat[1,2]             #Obtenemos dato de la fila 2 y columna 3
df.iat[0,-1]            #Obtenemos dato de la fila 0 y ultima columna
df.loc[:,'Mes'].iat[1]  #Obtenemos dato de una serie.
df.Mes.iat[1]           #Mismo resultado anterior

df.at['a', 'Mes']       #Obtenemos dato de la columna con etiqueta 'a' y columna 'Mes'
df.at['b','Mes']

#Ambos metodos permiten cambiar el valor de un dato.
df.at['b','Hospitalizados']=5
df.iat[1,2]=5

#%%
"""
Finalmente, los metodos get_loc y get_indexer permitiran
conocer la posicion de la etiqueta de una o varias filas
o columnas. Esto es util para cuando hemos agregado o quitado
filas o columnas y queramos conocer los indices nuevos de 
las etiquetas.

En su caso, get_indexer devuelve un array con la lista
de indices de las etiquetas que se pasan como parametros
"""
df.columns.get_loc('UCI')

df.columns.get_loc('Mes')

df.index.get_loc('b')

df.iloc[:,df.columns.get_loc('Mes')]

df.columns.get_indexer(['Mes','UCI'])

df.index.get_indexer(['a','c'])

df.iloc[:,df.columns.get_indexer(['Mes','UCI'])]

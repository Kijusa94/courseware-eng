#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:37:57 2023

@author: kijusa94
"""

"""
Es necesario conocer las operaciones que podemos realizar con los dataframes.
Dentro de las principales operaciones encontramos:
    Concatenate
    Merge
    Join
    Append
    Eliminar datos
   
Podemos utilizar, incluso, operaciones de conjunto como las uniones o intersecciones
y se pueden utilizar los índices o las columnas
como claves para realizar las operaciones, es decir, que podemos
añadir filas, añadir columnas a un DataFrame determinado.
También, vamos a ver cómo hacerlo con diferentes métodos
y cuál es el resultado de aplicar dicho método a uno o varios DataFrames.

Veamos algunos ejemplos. Primero creamos el set de DataFrames.
"""

#%%
import pandas as pd

def CreateDataFrame(rows, columns):
    data = []
    datarow = []

    for i in range(0, len(rows)):
        #print(f'i={i}')
        for j in range(0, len(columns)):    
            #print(f'j={j}')
            datarow.append(rows[i] + columns[j])
        data.append(datarow)
        datarow = []
            
    #print(data)
    df = pd.DataFrame(data, columns = columns, index = rows)
    
    return df

columns1 = ['C0','C1','C2','C3']
rows1 = ['R0','R1','R2','R3']

columns2 = ['C0','C1','C2','C3']
rows2 = ['R4','R5','R6','R7']

columns3 = ['C0','C1','C2','C3']
rows3 = ['R8','R9','R10','R11']

columns4 = ['C2','C3','C6']
rows4 = ['R2','R3','R7','R8']

columns5 = ['C5','C6','C7']
rows5 = ['R2','R3','R7','R8']

df1 = CreateDataFrame(rows1, columns1)
df2 = CreateDataFrame(rows2, columns2)
df3 = CreateDataFrame(rows3, columns3)
df4 = CreateDataFrame(rows4, columns4)
df5 = CreateDataFrame(rows5, columns5)

#%%
"""
Como los df 1, 2 y 3 tienen las mismas columnas, podemos
concatenar los datos que los componen.

pd.concat(objs,axis=0,join="outer",ignore_index=False,…)
objs: lista de df a unir.
axis: 0 para concatenar filas. 1 para concatenar columnas
join: tipo de concatenacion. Union, interseccion, etc
ignore_index = True para dejar los indices. False para 
reiniciarlos.

"""
r = pd.concat([df1,df2,df3])

#Concatenar columnas. Se agrega Nan porque no tienen valor
r = pd.concat([df1,df4],axis=1)
r = pd.concat([df1,df4])

#Ejemplo de intersección.
r = pd.concat([df1, df4], axis=1, join="inner")
              
#Podemos quedarnos con los valores que se tengan
#solamente en un dataframe. Ejemplo: Df1.
r = pd.concat([df1, df4], axis=1).reindex(df1.index)

"""
Por otra parte, tambien podemos combinar dataframes
con la instruccion merge (solo funciona con 2 DF).
La estructura es la siguiente:
pd.merge(lf, rg, how="inner", on=None, left_on=None, right_on=None, sort=True, indicator=False)
lf y rg son los dataframes
how: left, right, outer, inner indica que indices se usarán
on: left_on, right_on indica la columna que se usara como clave
sort: ordena el DF resultante por la columna clave
indicator: añade una columna con la procedencia de cada fila
"""
#%%
import pandas as pd

lf = pd.DataFrame(data = [('C0', 'C0', 'A0', 'B0'),
                          ('C0', 'C1', 'A1', 'B1'),
                          ('C1', 'C0', 'A2', 'B2'),
                          ('C2', 'C1', 'A3', 'B3')], 
                  columns=['C1','C2','A','B'])
                  
rg = pd.DataFrame(data = [('C0', 'C0', 'C0', 'D0'),
                          ('C1', 'C0', 'C1', 'D1'),
                          ('C1', 'C0', 'C2', 'D2'),
                          ('C2', 'C0', 'C3', 'D3')], 
                  columns=['C1','C2','C','D'])

#Fusiona las coincidencias de las columnas C1 y C2
r = pd.merge(lf,rg,on=["C1","C2"])

#Si se usa how left/right, se fusionan todas las coincidencias
#del dataframe de la izquierda/derecha, y se llena los valores
#de las columnas que o existen con Nan
r = pd.merge(lf,rg,how="left",on=["C1","C2"])

r = pd.merge(lf,rg,how="right",on=["C1","C2"])

#"outer" indica union, por lo que asume todos.
r = pd.merge(lf,rg,how="outer",on=["C1","C2"])

#"inner" indica interseccion. Se queda con lo que no
#aaroja valores nulos.
r = pd.merge(lf,rg,how="inner",on=["C1","C2"])


"""
En el caso en el que hay columnas con nombre repetido,
la libreria separa las columnas de cada dataframe
"""
#%%
lf = pd.DataFrame(data = [('C0', 'C0', 'A0', 'B0'),
                          ('C0', 'C1', 'A1', 'B1'),
                          ('C1', 'C0', 'A2', 'B2'),
                          ('C2', 'C1', 'A3', 'B3')], 
                  columns=['C1','C2','A','B'])
                  
rg = pd.DataFrame(data = [('C0', 'C0', 'C0', 'D0'),
                          ('C1', 'C0', 'C1', 'D1'),
                          ('C1', 'C0', 'C2', 'D2'),
                          ('C2', 'C0', 'C3', 'D3')], 
                  columns=['C1','C2','B','D'])

#Note que se el dataframe resultante tiene una columna
#para cada dataframe de entrada en el que coincide la
#columna de mismo nombre
r = pd.merge(lf,rg,on=["C1","C2"])

r = pd.merge(lf,rg,how="left",on=["C1","C2"])

"""
Podemos unir columnas de dos DF usando el metodo Join.
Este utiliza como clave los indices de los DF o una
columna.
    -No puede haber columnas con los mismos nombres en
    los dos DF.
    -Join se aplica sobre un DF
    df1.join(df2, on=None, how='left', sort=False)

ESTA FUNCION SE DIFERENCIA DE MERGE EN EL SENTIDO QUE
PERMITE UNIR DF A PARTIR DE LOS INDICES, MERGE ES MAS
VERSATIA AL PERMITIR COMBINAR FILAS Y COLUMNAS.

"""
r = df1.join(df5,how='outer')

r = df1.join(df5,how='inner')

r = df1.join(df5,how='left') 

r = df1.join(df5,how='right')

#%%
"""
La operacion APPEND permite añadir filas a un DF al 
final del DF que la llama. Si el DF añadido tiene
una columna que no está en el DF que llama al metodo,
Esta se agrega y llena con NaN.
"""
df1.append(df2, ignore_index=False, sort=False)

r = df1.append(df2)

r = df1.append(df4, ignore_index=True)

r = df1.append([df2,df4])

#%%
"""
finalmente, podemos eliminar datos, filas o columnas
con los siguientes metodos.
"""
r = df1.join(df5,how='outer')

#Podemos eliminar una fila mediante su etiqueta.
#Tambien podemos eliminar mediante su indice
r = r.drop('R3')
r = r.drop(r.index[3])

#Podemos eliminar una columna mediante su etiqueta.
#Tambien podemos eliminar mediante su indice. Hay que
#agregar axis=1 para que asuma las columnas.
r = r.drop('C5',axis=1)
r = r.drop(r.columns[4],axis=1)

#Podemos cambiar los valores NaN (nulos) por otro valor
r = r.fillna(0)
r = r.fillna('NULO')

#Con la instruccion dropna podemos eliminar filas o 
#columnas que tengan valores nulos.
#Eliminar filas con Nan
r = r.dropna(axis=0)

#Eliminar columnas con Nan
r = r.dropna(axis=1)

#Eliminar filas en donde las columnas C1 y C3 tengan
#valores nulos
r = r.dropna(subset=['C1','C3'])

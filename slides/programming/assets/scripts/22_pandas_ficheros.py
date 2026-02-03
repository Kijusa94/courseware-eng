#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:33:51 2023

@author: kijusa94
"""

"""
vamos a ver cómo funciona la lectura y escritura de
ficheros en Panda, para poder crear DataFrames a partir
de los datos que tenemos en un fichero o poder escribir
los datos de un DataFrame en un fichero.
Y vamos a ver tanto la utilización de ficheros CSV, 
como ficheros Excel.

Para leer un fichero csv utilizamos:
    df = pd.read_csv(nombre, sep=separador, header=n, index_col=m, decimal=separador-decimal)
"""
import pandas as pd

#Leemos un archivo csv y lo cargamos a df
df = pd.read_csv('ejercicio.csv')

#Cuando tenemos caracteres especiales
df = pd.read_csv('ejercicio.csv',encoding='utf-8') 

#Cuando el fichero no tiene nombres de columnas se pueden
#indicar al momento de la lectura.
df = pd.read_csv('ejercicio.csv', names = ['n','id','diet','time','kind'])

"""
Para escribir un dataframe en un csv, utilizamos
    
    df.to_csv(nombre, sep=separador, columns=none, index=bool)
    
nombre: nombre del fichero
sep: separador a usar para los datos
columns: las columnas que se van a almacenar
index: True para guardar los indices. False para no hacerlo
"""
#df.to_csv('ejercicio.csv')

#%%
"""
Para leer datos de una hoja de calculo de excel, utilizamos
    df = pd.read_excel(nombre,sheet_name=hoja, header=n, index_col=m, decimal=separador-decimal)

Nombre: nombre del archivo o url
hoja: si tiene varias hojas
n: numero de linea en la que está la cabecera, por defecto 0
m: la columna que se utilizará como indice
separador_decimal: se utiliza el '.' por defecto. En Europa es ','
"""

df = pd.read_excel('data/ejercicio.xlsx', sheet_name='ejercicio')

#%%
"""
Para escribir en un fichero de Excel, utilizamos ExcelWriter.
"""
import xlsxwriter

#Creacion de dataframe mediante listas
df1 = pd.DataFrame(data = [('Enero',177643,12475,996,2564),
                          ('Febrero',33727,3278,333,1364),
                          ('Marzo',4457,482,75,172)],
                  columns=['Mes','Casos','Hospitalizados','UCI','Fallecidos'],
                  index=list('abc'))

df2 = pd.DataFrame(data = [('Septiembre',234765,12475,332,4321),
                          ('Octubre',21342,2341,222,9876),
                          ('Noviembre',5532,398,80,203)],
                  columns=['Mes','Casos','Hospitalizados','UCI','Fallecidos'],
                  index=list('abc'))

writer = pd.ExcelWriter('datos_covid', engine='openpyxl')

df1.to_excel(writer, sheet_name='Hoja1', index=False)

df2.to_excel(writer, sheet_name='Hoja2', index=False)

writer.save()


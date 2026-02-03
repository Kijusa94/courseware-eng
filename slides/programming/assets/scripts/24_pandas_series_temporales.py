#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:35:11 2023

@author: kijusa94
"""

"""
Una serie temporal es aquella en la que los datos toman valores a lo largo del
tiempo. Una de las características más interesantes de los DataFrames es que
pueden analizar patrones a lo largo del tiempo y para ello, utilizarán las 
series temporales. Podemos hacer agrupaciones de datos, como hemos visto antes,
utilizando agrupaciones diarias, semanales, mensuales o anuales.

Para utilizar las series de tiempo con los dataframes, se utilizarán conversiones
entre cadenas de texto y datetimes. Primero, creemos el dataframe
"""

import pandas as pd

#Creamos el dataframe con la fecha en formato cadena de texto
data = [('2021-1-1', 'A' , 794,  66,  6, 12),
        ('2021-1-1', 'CS', 178,  15,  2, 3),
        ('2021-1-1', 'V' , 1036, 113, 9, 28),
        ('2021-1-2', 'A' , 970,  83,  7, 11),
        ('2021-1-2', 'CS', 272,  17,  1, 4)]
columns = ['Fecha', 'Provincia', 'Casos', 'Hospitalizados', 'UCI', 'Defunciones']
df = pd.DataFrame(data= data, columns= columns)

#Utilizamos la instruccion to_datetime para convertir cadenas de caracteres en
#el formato de serie temporal.
df.Fecha = pd.to_datetime(df.Fecha, format='%Y/%m/%d')

#Guardamos el archivo de excel para proximos usos.
writer = pd.ExcelWriter('datos_covid.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='Hoja1', index=False)
writer.save()

#Guardamos en un archivo csv para proximos usos
df.to_csv('datos_covid.csv', columns=columns, index=False)

#%%
"""
Podemos convertir directamente los datos de fechas al leer un archivo csv.
La conversión a formato datetime, permite realizar operaciones sobre este 
tipo de dato (algo que no se puede con datos tipo cadena de texto):
"""
#La instruccion 'parse_dates' se encarga de convertir las fechas a tipo datetime
df = pd.read_csv('data/datos_covid.csv',dayfirst=True, parse_dates=['Fecha'], index_col=0)

#Podemos hacer que la columna 'Fecha' sea el indice del dataframe.
df.set_index('Fecha',inplace = True)

#Podemos extraer información de la columna de fechas.
df.index.year               #Extraer el año
df.index.month              #Extraer el mes

df.index.month_name()       #Extraer el nombre del mes
df.index.day_name()         #Extraer el nombre del dia

#Tambien podemos extraer las filas que hay en una fecha
df.loc['2021-08']

#O entre un rango de fechas.
df.loc['2021-07-29':'2021-08-03']

#%%
"""
Los dataframes de series de tiempo permiten realizar operaciones mediante el 
formato datetime. Esto facilita la extracción o agrupacion de datos a partir
de las propiedades, mes, año, dia, horas, minutos o segundos.
"""

import pandas as pd

#Creamos un nuevo dataframe para guardar los resultados
r = pd.DataFrame()

#Cargamos el archivo 'datos_covid' para las operaciones
df = pd.read_csv('datos_covid.csv',dayfirst=True, parse_dates=['Fecha'], index_col='Fecha')

#En el nuevo dataframe guardamos el numero de casos presentados de acuerdo a 
#la agrupación de fecha en una nueva columna.
r['Casos'] = (df.groupby("Fecha"))['Casos'].sum()

#Podemos determinar la suma de los casos producidos en opr mes. Para ello,
#agrupamos los valores del dataframe por el mes, y a ese resultado la sumatoria
#del resto de campos.
df.groupby(df.index.month_name('es_ES'), sort=False).sum()

#Podemos agrupar los datos utilizando multiples indices. En este caso, agrupamos
#por provincia y por mes. Del resultado, acumnulamos los valores
r = df.groupby(['Provincia',df.index.month_name('en_NZ')], sort=False).sum()

#De este resultado podemos obtener solo los valores de una provincia en particular
#para este caso, la provincia V
r.loc['V']


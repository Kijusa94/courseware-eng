#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:39:19 2023

@author: kijusa94
"""

"""
Las expresiones lambda se utilizan para crear lo que se denominan
funciones anónimas. Las funciones anónimas
son equivalentes a las funciones definidas por un usuario, pero
son bastante más rápidas que estas funciones. Sobre todo,
tienen mucho interés para trabajar con DataFrames.

La siguiente expresion:
    lambda_expr ::= "lambda" [parameter_list] ":" expresión
Es equivalente a:
    def (parameters):

    return expression

Veamos un ejemplo sencillo:
"""
#Creamos una función con el nombre doble. Esta funcion recibe el parametro x
#y retorna el valor x*2
doble = lambda x: x*2

#Aplicamos la funcion
doble(4)
doble(10)

#Otro ejemplo, puede ser determinar si un numero es par. La función se llama
#'par'. Esta función recibe el parametro x, y retorna True si el modulo de x
#entre 2 es 0 o retorna False si no lo es.
par = lambda x: True if x%2 ==0 else False

#Aplicamos la función
par(6)
par(11)

#%%
"""
Miremos su aplicación con dataframes. Primero genere los datos a utilizar.
O cargue el archivo 'datos_covid_lambda.csv'
"""

"""
import pandas as pd
import random

#PARA GENERAR LOS DATOS.
df = pd.DataFrame()
df['Mes'] = pd.date_range(start='2023-01-15', end='2023-12-15', periods=12).month_name('es_ES')
df['Casos'] = random.sample(range(10000,200000), 12)
df['Hospitalizados'] = random.sample(range(10,10000), 12)
df['UCI'] = random.sample(range(10,1000), 12)
df['Fallecidos'] = random.sample(range(0,100), 12)

#Guardamos en un archivo csv para proximos usos
df.to_csv('datos_covid_lambda.csv', index=False)
"""

#%%
"""
Ahora si, apliquemos expresiones lambda a los datos.
"""
import pandas as pd
import random

#PARA CARGAR LOS DATOS
df = pd.read_csv('datos_covid_lambda.csv', encoding='utf-8')

#Calculemos el total de casos del dataset
total = df.Casos.sum()

#Utilicemos la expresion lambda para calcular el porcentaje de casos de cada
#mes respecto al total de casos del año. #En este caso, 'x' es cada uno de los 
#valores de la columna 'Casos' a los cuales se les aplicará la la operación.
df['Porcentaje_Mensual'] = df['Casos'].apply(lambda x: round(x*100/total,2))

#Podemos utilizar expresiones lambda booleanas. Calculemos los meses que
#han tenido un porcentaje de casos mayor al 5%
df['mas5'] = df['Porcentaje_Mensual'].apply(lambda x: True if x>5 else False)

#Otro ejemplo, puede ser calcular la tasa de hospitalizados por cada caso,
#mensualmente
df['ratioHC']=df.apply(lambda x: round(x['Hospitalizados']/x['Casos'],3),axis=1)

"""
Las expresiones lambda, también pueden utilizar operaciones
o funciones definidas por el usuario. De ese modo, podemos realizar
operaciones tan complejas como queramos. Entonces, podemos definir una función
que reciba dos parámetros, aquí se harán todas las operaciones
que queramos y devuelva un resultado. Entonces, a la función
se le llama dentro de la expresión lambda, pasándole los valores
de la columna uno y de la columna dos del DataFrame df. Recordad
que siempre tenemos que indicar si trabajamos con las columnas,
que el eje es uno. 

def func (c1, c2):
    ...
return

df['col3'] = df.apply(lambda x: func(x.col1, x.col2), axis=1) 

"""























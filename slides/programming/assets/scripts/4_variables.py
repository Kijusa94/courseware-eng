#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:37:49 2023

@author: kijusa94
"""

"""
En este script retomaremos el uso de las variables.

Revismos algunas consideraciones al definir variables:
    1. Deben empezar por letra o simbolo de guión bajo "_"
    2. No deben empezar por un numero
    3. Solo puede ser letra, numero o subrayado (NO VAN ESPACIOS)
    4. Las variables son CASE SENSITIVE, es decir, se diferencia de minusculas
    y mayusculas. Por tanto, "MiNombre" es diferente de "minombre".
    
Tenga presente que a pesar de que los nombres de variables pueden ser cualquier
palabra, se sugiere que los nombres sean indicativos de la asignación.
"""
3MiVariable = 23        #Lanza error debido a que inicia con numero
MiVariable3 = 23        #El numero puede ir entre o al final
_miVariable = 23        #Puede usar guion bajo pero no caracteres especiales
_MIVARIABLE = 23        #A pesar de que se llama igual es otra variable por los CAPS

"""
RESPECTO AL TIPO DE DATO
Python maneja algo que se llama Tipado Dinamico. Esto permite que una variable
pueda actualizar el contenido y tipo de dato en ejecución. Ejecute cada linea
presentada a continuación y observe en el explorador de variables la
actualizacion del tipo y dato:
"""
miVariable = 23
miVariable = "hola mundo"
miVariable = 3.2 + 2.4j

"""
Sin embargo, Python es fuertemente tipado, esto quiere decir que las operaciones
entre datos, deben realizarse con valores del mismo tipo. Observe:
"""
numero = 23
cadena = "hola"
numero + 2
cadena + "mundo"

cadena + numero         #Arroja error porque la suma esta definida para mismos
                        #tipos de valores

"""
A pesar de no necesitar definir los tipos de datos, si es importante que los 
conozcamos para entender su funcionamiento y operaciones

Los tipos de datos básicos son los siguientes:
    1. TIPOS DE DATOS NUMERICOS: Almacenan numeros
        1.1 ENTEROS (int/long)
        1.2 REALES (float)
        1.3 COMPLEJOS
"""
numero = 23
#numero_largo = 3L
decimal = 3.0
complejo = 2 + 1j

"""
Otros tipos de datos básicos son:
    2. LOGICOS: Almacenan binarios v/f o 1/0 e implementan algebra booleana
"""
variable_logica = True
variable_logica = False

"""
Otros tipos de datos básicos son:
    3. SECUENCIALES: Almacenan multiples valores
        3.1 Cadenas de texto
        3.2 Listas
        3.3 Tuplas
"""
cadena = "hola mundo"

lista = ["hola", "mundo", "lista"]      #Note que va entre llaves. cada valor
                                        #se guarda en una posicion de la lista
                                        
tupla = ("manzana", "pera", "piña")     #Se diferencia de la lista al ser inmutable

#LAS LISTAS Y LAS TUPLAS SON HETEROGENEAS, ES DECIR, PUEDEN GUARDAR DATOS DE
#DIFERENTE TIPO

lista_heterogenea = ["hola", 3, True]
tupla_heterogenea = ("manzana", "pera", "piña")


diccionario = {"1":"hola", "2":"mundo", "w":"lista"} #Contienen clave y dato
diccionario["w"]                                         

#%%
a= 5
print(a)
#%%
a =10
print(a)
#%%

--



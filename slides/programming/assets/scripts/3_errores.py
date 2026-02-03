#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:50:49 2023

@author: kijusa94
"""

"""
De los errores se aprende.
A continuación, se presentan los casos tipicos de errores que se dan al programar
cuando se empieza a programar. Tenga presente los siguientes casos a la hora de 
programar.

SEA ORDENADO. Recuerde que el computador no entiende las instrucciones a menos 
de que se le indiquen de forma correcta. Sea paciente y lea detenidamente los
mensajes que arroja el interprete para identificar los tipos de errores.

Existen generalmente 2 tipos de errores: De sintaxis (algo mal escrito) y de 
ejecución (el interprete no lo puede ejecutar). Observe los ejemplos
"""

#EJEMPLO 1: ERROR DE ESCRITURA - FALTA UN PARENTESIS
print("hola mundo"

#EJEMPLO 2:ERROR DE ESCRITURA - FALTAN PARENTESIS
print "hola mundo"

#EJEMPLO 3: ERROR DE ESCRITURA - La instrucción print es en minuscula
Print("hola mundo")

#EJEMPLO 4: ERROR DE ESCRITURA - LAS VARIABLES NUMERICAS NO PUEDEN INICIAR CON CERO
numero = 034

#EJEMPLO 5: ERROR DE ESCRITURA - NO HAY OPERACION ENTRE VALORES.
"hola mundo" 34 34.5

#EJEMPLO 6: ERROR DE ESCRITURA - IDENTACIÖN. En Python los espacios al inicio iportan
print("hola")
    print("mundo")

#EJEMPLO 7: ERROR DE EJECUCION - CALCULOS NO POSIBLES
3/0

#EJEMPLO 8: ERROR DE EJECUCION - OPERACION ENTRE DIFERENTES TIPOS DE DATOS
a = "hola" + 2

#EJEMPLO 9: ERROR DE EJECUCION - ACCEDER A COSAS QUE NO EXISTEN
archivo = open("error.txt", "r")

#EJEMPLO 10: ERROR DE EJECUCION - ACCESO A VALORES NO DEFINIDOS
a = [1,2,3,4]
b = a[6]


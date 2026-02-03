#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:52:46 2023

@author: kijusa94
"""

"""
Estamos trabajando con un controlador RaspberryPi Pico, para realizar
la medición de Temperatura y Humedad en un proceso industrial. En este,
se disponen de dos motores para el sistema de calefacción y refrigeración 
del sistema. Los datos enviado por la tarjeta de control se presentan bajo
el siguiente formato:
    Estampa_de_tiempo,  Sensor1,    Sensor2,    Motor1,     Motor2
    HH:MM:SS,        NN.NN,      NN.NN,      NN.NN,      NN.NN

Elabore un código que permita extraer cada uno de los datos de la cadena
de forma independiente
"""

cadena = '19:38:23, 25.76, 70.23, 19000.00, 18950.00'

valores = cadena.split(',')

time_stamp = valores[0]
sensor1 = float(valores[1])
sensor2 = float(valores[2])
motor1 = float(valores[3])
motor2 = float(valores[4])
    
"""
EJERCICIO: De los datos obtenidos, extraíga:
    1. La hora. Expresela en pantalla en segundos
    2. Los minutos. Exprese en pantalla en segundos
    3. Sume el total de tiempo en segundos
    4. Presente el valor entero mas próximo del sensor1 (hacia abajo)
    5. Presente el valor entero mas próximo del sensor2 (hacia arriba)
    6. Promedie las velocidades de los valores obtenidos por los motores.
"""
#1, 2 y 3
hours = int(time_stamp.split(':')[0])
minutes = int(time_stamp.split(':')[1])
seconds = int(time_stamp.split(':')[2])
total_time_in_seconds = hours*3600 + minutes*60 + seconds

print(f'El total de horas transcurridas en segundos es: {hours*3600}')
print(f'El total de minutos transcurridas en segundos es: {minutes*60}')
print(f'El total de tiempo transcurridas en segundos es: {total_time_in_seconds}')


#4 y 5
import math

sensor1 = math.floor(sensor1)
sensor2 = math.ceil(sensor2)

print(f'el valor entero mas próximo del sensor1 (hacia abajo) es: {sensor1}')
print(f'el valor entero mas próximo del sensor2 (hacia arriba) es: {sensor2}')
 

#6
import statistics
avg_motor = statistics.mean([motor1, motor2])

print(f'El promedio de velocidad de los motores es: {avg_motor}')

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 18:32:04 2024

@author: juand
"""
def calcular_salario(h_trabajadas, costo_hora):
    if (h_trabajadas <= 40):   
        salario_basico = h_trabajadas * costo_hora
        salario_neto = salario_basico * 0.85
    elif (h_trabajadas > 40):
        salario_basico = 40 * costo_hora
        salario_h_extras = (h_trabajadas - 40) * costo_hora * 1.5
        salario_neto = (salario_basico + salario_h_extras) * 0.85
    return salario_neto

def clasificar_empleado(salario):
    if (salario <= 500):
        return 'Bajo'
    elif (salario > 500 and salario <= 1000):
        return 'Medio'
    elif (salario > 1000):
        return 'Alto'

def generar_reporte():
    for infoEmpleado in lista:
        if infoEmpleado['clasificacion'] == 'Bajo':
            listaB.append(infoEmpleado['nombre'])
        elif infoEmpleado['clasificacion'] == 'Medio':
            listaM.append(infoEmpleado['nombre'])
        elif infoEmpleado['clasificacion'] == 'Alto':
            listaA.append(infoEmpleado['nombre'])
    
    print("Empleados en salario bajo:", listaB)
    print("Empleados en salario medio:", listaM)
    print("Empleados en salario alto:", listaA)
    
lista = []
listaB = []
listaM = []
listaA = []

N = int(input("Ingrese el numero de empleados a registrar: "))

for i in range(0, N):
    nombre = input("Ingrese el nombre del empleado: ")
    horas = int(input("Ingrese el numero de horas trabajadas por el empleado: "))
    tarifa = float(input("Ingrese el pago por hora del empleado: "))
    
    lista.append({'nombre':nombre, 'horas_trabajadas':horas, 'tarifa':tarifa})


for infoEmpleado in lista:
    infoEmpleado['salario'] = calcular_salario(infoEmpleado["horas_trabajadas"], infoEmpleado['tarifa'])
    infoEmpleado['clasificacion'] = clasificar_empleado(infoEmpleado['salario'])

"""
for i in range(0, len(lista)):
    lista[i]['salario'] = calcular_salario(lista[i]["horas_trabajadas"], lista[i]['tarifa'])
    print(lista[i]['salario'])
    lista[i]['clasificacion'] = clasificar_empleado(lista[i]['salario'])
"""  
generar_reporte()

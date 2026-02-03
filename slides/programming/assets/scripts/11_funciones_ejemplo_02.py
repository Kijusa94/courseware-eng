# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 09:34:30 2025

@author: juand
"""

"""
    APLICACION PARA UN SISTEMA DE NOTAS
"""

lista_estudiantes = []

estudiante1 = {"cod":100, "nom":"Alejandra", "N1":2, "N2":3, "N3":5}
estudiante2 = {"cod":200, "nom":"Yackeline", "N1":1, "N2":5, "N3":5}
estudiante3 = {"cod":300, "nom":"Yessenia", "N1":3, "N2":3, "N3":3}

lista_estudiantes.append(estudiante1)
lista_estudiantes.append(estudiante2)
lista_estudiantes.append(estudiante3)


def ImprimirMenu():
    print("App de notas")
    print("1. Agregar estudiante (Nombre, Cod, N1, N2, N3)")
    print("2. Editar informacion de estudiante")
    print("3. Eliminar estudiante")
    print("4. Seleccionar estudiante")
    print("5. Calcular notas y determinar aprobado.")
    print("6. Sumar puntos de participacion")
    print("7. Salir")
    
while True:
    ImprimirMenu()
    opcion = input("Ingrese su opcion: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        cod = input("Ingrese el codigo del estudiante: ")
        n1 = input("Ingrese la nota del estudiante: ")
        n2 = input("Ingrese la nota del estudiante: ")
        n3 = input("Ingrese la nota del estudiante: ")
        
        estudiante = {"cod":cod, "nom":nombre, "N1":n1, "N2":n2, "N3":n3}
        
        lista_estudiantes.append(estudiante)
    
    elif opcion == "2":
        codigo = int(input("Ingrese el codigo del estudiante: "))
        
        for estudiante in lista_estudiantes:
            if (estudiante["cod"] == codigo):
                estudiante["N1"] = int(input("Ingrese la N1: "))
                estudiante["N2"] = int(input("Ingrese la N2: "))
                estudiante["N3"] = int(input("Ingrese la N3: "))
    
    elif opcion == "3":
        codigo = int(input("Ingrese el codigo del estudiante: "))
        for estudiante in lista_estudiantes:
            if (estudiante["cod"] == codigo):
                lista_estudiantes.remove(estudiante)
        
    
    elif opcion == 7:
        break

    else:
        print("Error. Ingrese una opcion válida")
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:52:01 2024

@author: juand
"""
lista = [10, 21, 312, 460, 176, 254]

while True:
    print("MENU PARA GESTION DE LISTAS")
    print("1. Listar elementos a la lista")
    print("2. Agregar elementos a la lista")
    print("3. Editar elementos a la lista")
    print("4. Eliminar elementos a la lista")
    print("5. Sume los elementos de la lista")
    print("6. Promedio los elementos de la lista")
    print("7. Maximo los elementos de la lista")
    print("8. Minimo los elementos de la lista")
    print("9. Desviacion estandar de los elementos de la lista")
    print("10. Insertar un valor en una posición deseada")
    print("11. Listar los numeros pares")
    print("12. Listar los numeros impares")
    print("13. Listar los numeros primos")
    print("14. Listar los numeros hermanos")
    print("15. Salir")
    
    opcion = int(input("Ingrese la opcion: "))

    if (opcion == 1):
        #Listar elementos
        for i in lista:
            print(i)
            
    elif (opcion == 2):
        #Agregar elementos
        valor = int(input("Ingrese el valor a agregar: "))
        lista.append(valor)

    elif (opcion == 3):
        #Editar un elemento
        idx = int(input("Ingrese el indice que desea modificar: "))
        lista[idx] = int(input("Ingrese el nuevo valor: "))   

    elif (opcion == 4):
        valor = int(input("Ingrese el valor a eliminar: "))
        lista.remove(valor)
            
    elif (opcion == 5):
        suma = 0
        for i in lista:
            suma = suma + i
        print(f"La suma de los elementos es {suma}")
        
    elif (opcion == 6):
        suma = 0
        for i in lista:
            suma = suma + i
        promedio = suma / len(lista)    
        print(f"El promedio de los elementos en la lista es {promedio}")
        
    elif (opcion == 7):
        maximo = 0
        for i in lista:
            if (i > maximo):
                maximo = i
        print(f"El valor maximo es {maximo}")
        
        
        
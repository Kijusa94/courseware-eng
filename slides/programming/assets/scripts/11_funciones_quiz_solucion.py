# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

def ImprimirMenu():
    print("APP Notas")
    print("1. Registrar")
    print("2. Editar")
    print("3. Elimianr")
    print("4. Listar")
    print("5. Salir")
 
def CalcularConcepto(nota_p):
    if (nota < 2):
        return "Reprobado"
    elif (nota > 2 and nota < 3):
        return "Habilita"
    elif (nota >= 3 and nota <= 5):
        return "Aprobado"
 
    
lista = []

while True:
    ImprimirMenu()
    opcion = int(input("Ingrese su opcion: "))
    
    if opcion == 1:
        cod = input("Ingrese codigo: ")
        nom = input("Ingrese nombre: ")
        nota = float(input("Ingrese nota: "))
        
        nuevo_registro = {"cod":cod, "nom":nom, "nota":nota, "con":CalcularConcepto(nota)}
        
        lista.append(nuevo_registro)
    
    elif opcion == 2:
        codigo = input("Ingrese codigo a buscar: ")
        
        for i in lista:
            if i["cod"] == codigo:
                i["nota"] = float(input("Ingrese nota: "))
                i["con"] = CalcularConcepto(i["nota"])

    elif opcion == 3:
        codigo = input("Ingrese codigo a buscar: ")
        
        for i in lista:
            if i["cod"] == codigo:
                lista.remove(i)
            
    elif opcion == 4:
        for i in lista:
            print(i)
        
        
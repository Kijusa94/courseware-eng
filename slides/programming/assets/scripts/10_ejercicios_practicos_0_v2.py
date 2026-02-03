# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:31:12 2024

@author: juand
"""
#%%
"""
1. Un comerciante compra un artículo a un costo dado. Determine el precio al cual debe venderlo si desea ganar el 15%.
"""
print("App de venta.")
precio = float(input("Indique el valor del producto: "))

print(f"Usted debe vender el producto a {precio * 1.15} para obtener el 15% de ganancia")

print("Usted debe vender el producto a " + str(precio * 1.15) + " para obtener el 15% de ganancia")

print("Usted debe vender el producto a", str(precio * 1.15), "para obtener el 15% de ganancia")

#%%
"""
2. Un alumno desea saber cual será su calificación final en cierta materia. Dicha calificación se compone de lo siguiente:

60% corresponde al examen escrito.
20% corresponde a las lecciones
15% corresponde a las tareas.
5% corresponde a las prácticas en el laboratorio

El dato del examen escrito es un valor entre 0 y 100 y los otros datos son valores entre 0 y 10. La calificación final debe ser un valor entre 0 y 20.
"""
print("App de notas.")
examen = int(input("Ingrese su nota de examen: "))
lecciones = int(input("Ingrese su nota de lecciones: "))
tareas = int(input("Ingrese su nota de tareas: "))
practicas = int(input("Ingrese su nota de laboratorios: "))

# Calculamos en escala de 20 (calificación máxima)
examen_escrito_escala_20 = (examen / 100) * 20
lecciones_escala_20 = (lecciones / 10) * 20
tareas_escala_20 = (tareas / 10) * 20
practicas_escala_20 = (practicas / 10) * 20

# Cálculo de la calificación final
calificacion_final = (examen_escrito_escala_20 * 0.60) + (lecciones_escala_20 * 0.20) + (tareas_escala_20 * 0.15) + (practicas_escala_20 * 0.05)

# Mostrar el resultado
print(f"La calificación final del alumno es: {calificacion_final:.2f}")


#%%
"""
3. En un almacén se descuenta 20% del precio al cliente si el valor a pagarse es mayor a $200. Dado un valor de precio, muestre lo que debe pagar el cliente.
"""
print("App de almacen")
valor = float(input("Ingrese el valor a pagar: "))

if (valor > 200):
    print("Usted tiene un descuento del 20% a su compra. El pago total es: {valor * 0.8}")
else:
    print("Usted no tiene derecho al descuento. El pago total es: {valor}")

"""
4. En un almacén se rebaja 10% del precio al cliente si compra mas de 20 artículos y 5% si compra hasta 20 artículos pero más de 10. Dado el precio unitario de un artículo y la cantidad adquirida, muestre lo que debe pagar el cliente .
"""
print("App de almacen")
precio_unitario = float(input("Ingrese el valor del producto: "))
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

if (cantidad > 10 and cantidad < 20):
    print(f"El valor a pagar es {cantidad * precio_unitario * 0.95}.")
elif (cantidad > 20):
    (f"El valor a pagar es {cantidad * precio_unitario * 0.8}.")
else:
    print("ERROR. Ha ingresado un valor no válido.")

#%%
"""
5. Una frutería ofrece las manzanas con descuento según la siguiente tabla:
Dado el precio por kilo, y el peso, determinar cuánto pagará una persona que compre manzanas es esa frutería.

kilos comprados	   | Descuento %
0 – 2	           |     0%
2.01 – 5	       |    10%
5.01 – 10	       |    15%
10.01 en adelante  |	20%
"""
print("App fruteria")
precio = float(input("Ingrese el precio por kilo: "))
peso = float(input("Ingrese el peso: "))

if (peso > 0 and peso <= 2):
    descuento = 0;
elif (peso > 2 and peso <= 5):
    descuento = 10;
elif (peso > 5 and peso <= 10):
    descuento = 15;
elif (peso > 10):
    descuento = 20;
else:
    print("Error")

print("Total a pagar:", peso * precio * (1 - descuento/100))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:31:52 2023

@author: kijusa94
"""

"""
Matplotlib es una librería que nos permite realizar gráficas con datos, que 
es muy robusta y versátil, y trabaja con el lenguaje de programación Python. 
Además, permite visualizar muchos tipos de gráficas, de líneas,
de barras, de dispersión, de cajas, tarta, etcétera. Prácticamente,
cualquier tipo de gráfica que se utiliza comúnmente en análisis de datos.
Además, es muy flexible a la hora de personalizar el resultado final.
Podemos incluir títulos, etiquetas, ejes, podemos formatear estos
ejes como nosotros queramos, añadir leyendas, estilos de líneas
y colores, etcétera. De modo que obtengamos una gráfica a nuestro gusto,
personalizada, como nosotros queramos.
Se combina con la librería Numpy y Pandas, que es la que
vamos a utilizar en este módulo.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/datos_covid.csv', encoding='utf-8')
plt.plot(df.Casos)
plt.plot(df.Hospitalizados)
plt.plot(df.UCI)
plt.show()
plt.show()

"""
Las figuras o graficas tienen elemenots como:
    Anatomia de la grafica
    Ejes: Limites y marcas
    Etiquetas: titulos, ejes, leyendas
    Colores y estilos
"""
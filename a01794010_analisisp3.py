# -*- coding: utf-8 -*-
"""A01794010 AnalisisP3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aaHHaxYW6BeiWYmTax82wfWeA_4VeWLG
"""

import pandas as pd


with open('/content/TC1.txt', 'r') as file:

    contenido = file.read()


palabras = contenido.split()


cantidad_total_palabras = len(palabras)


contador_palabras = {}

for palabra in palabras:
    palabra = palabra.lower()  # Convierte a minúsculas para no diferenciar entre mayúsculas y minúsculas
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Crea un DataFrame de pandas con los resultados
df = pd.DataFrame(list(contador_palabras.items()), columns=["Row Labels", "Count of TC1"])


print(f'Cantidad total de palabras en el archivo: {cantidad_total_palabras}\n')


print(df)


palabras_unicas = list(contador_palabras.keys())
frecuencias = list(contador_palabras.values())

import pandas as pd


with open('/content/TC2.txt', 'r') as file:

    contenido = file.read()


palabras = contenido.split()


cantidad_total_palabras = len(palabras)


contador_palabras = {}

for palabra in palabras:
    palabra = palabra.lower()  # Convierte a minúsculas para no diferenciar entre mayúsculas y minúsculas
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Crea un DataFrame de pandas con los resultados
df = pd.DataFrame(list(contador_palabras.items()), columns=["Row Labels", "Count of TC1"])


print(f'Cantidad total de palabras en el archivo: {cantidad_total_palabras}\n')


print(df)


palabras_unicas = list(contador_palabras.keys())
frecuencias = list(contador_palabras.values())

import pandas as pd


with open('/content/TC3.txt', 'r') as file:

    contenido = file.read()


palabras = contenido.split()


cantidad_total_palabras = len(palabras)


contador_palabras = {}

for palabra in palabras:
    palabra = palabra.lower()  # Convierte a minúsculas para no diferenciar entre mayúsculas y minúsculas
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Crea un DataFrame de pandas con los resultados
df = pd.DataFrame(list(contador_palabras.items()), columns=["Row Labels", "Count of TC1"])


print(f'Cantidad total de palabras en el archivo: {cantidad_total_palabras}\n')


print(df)


palabras_unicas = list(contador_palabras.keys())
frecuencias = list(contador_palabras.values())



import pandas as pd


with open('/content/TC4.txt', 'r') as file:

    contenido = file.read()


palabras = contenido.split()


cantidad_total_palabras = len(palabras)


contador_palabras = {}

for palabra in palabras:
    palabra = palabra.lower()  # Convierte a minúsculas para no diferenciar entre mayúsculas y minúsculas
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Crea un DataFrame de pandas con los resultados
df = pd.DataFrame(list(contador_palabras.items()), columns=["Row Labels", "Count of TC1"])


print(f'Cantidad total de palabras en el archivo: {cantidad_total_palabras}\n')


print(df)


palabras_unicas = list(contador_palabras.keys())
frecuencias = list(contador_palabras.values())



import pandas as pd


with open('/content/TC5.txt', 'r') as file:

    contenido = file.read()


palabras = contenido.split()


cantidad_total_palabras = len(palabras)


contador_palabras = {}

for palabra in palabras:
    palabra = palabra.lower()  # Convierte a minúsculas para no diferenciar entre mayúsculas y minúsculas
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Crea un DataFrame de pandas con los resultados
df = pd.DataFrame(list(contador_palabras.items()), columns=["Row Labels", "Count of TC1"])


print(f'Cantidad total de palabras en el archivo: {cantidad_total_palabras}\n')


print(df)


palabras_unicas = list(contador_palabras.keys())
frecuencias = list(contador_palabras.values())

df.to_csv('resultados.txt', sep='\t', index=False)
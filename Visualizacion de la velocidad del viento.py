# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:33:30 2024

@author: draja
"""

import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
file_path = r"C:\Users\draja\OneDrive\Documentos\Work1TNC\velocity_win\Encinas Johnson 2013-2024_v1.csv"

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(file_path)

# Verificar los primeros datos y las columnas del DataFrame
print(df.head())
print(df.columns)

# Eliminar espacios en blanco en los nombres de las columnas
df.columns = df.columns.str.strip()

# Convertir la columna de fecha a tipo datetime con el formato adecuado
if 'Fecha' in df.columns:
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

# Graficar los datos
plt.figure(figsize=(12, 6))

# Graficar solo si ambas columnas existen en el DataFrame
if 'Fecha' in df.columns and 'Velocidad del viento' in df.columns:
    plt.plot(df['Fecha'], df['Velocidad del viento'], marker='o', linestyle='-', color='b')
    plt.title('Velocidad del Viento a lo largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Velocidad del Viento')
    plt.xticks(rotation=45)  # Rote las etiquetas del eje x si son largas
else:
    print("Las columnas 'Fecha' o 'Velocidad del viento' no se encuentran en el DataFrame.")

plt.tight_layout()
plt.show()

print(df.describe())

print(df.corr())

import numpy as np

# Ajustar una línea de tendencia
z = np.polyfit(df['Fecha'].map(pd.Timestamp.toordinal), df['Velocidad del viento'], 1)
p = np.poly1d(z)

plt.figure(figsize=(12, 6))
plt.plot(df['Fecha'], df['Velocidad del viento'], marker='o', linestyle='-', color='b', label='Datos')
plt.plot(df['Fecha'], p(df['Fecha'].map(pd.Timestamp.toordinal)), color='r', linestyle='--', label='Tendencia')
plt.title('Velocidad del Viento con Línea de Tendencia')
plt.xlabel('Fecha')
plt.ylabel('Velocidad del Viento')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


import matplotlib.dates as mdates

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Velocidad del viento'])
plt.title('Velocidad del Viento')
plt.xlabel('Fecha')
plt.ylabel('Velocidad del Viento')
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


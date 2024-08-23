# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:33:38 2024

@author: draja
"""

import matplotlib.pyplot as plt

# Meses del año
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Datos de altura de marea para cada serie
datos = {
    'Serie 1': [-0.93, -0.2, -0.76, -0.35, 0.35, 1.38, 1.34, 0.81, 1.06, 1.28, -0.16, -0.61],
    'Serie 2': [5.88, 5.4, 5.91, 4.42, 3.84, 3.68, 3.46, 2.9, 3.62, 4.53, 4.86, 5.15],
    'Serie 3': [-0.11, 0.28, -0.31, 0.88, 1.6, 1.99, 1.44, 1.05, 0.59, -0.08, -1.08, -1.14],
    'Serie 4': [5.17, 3.81, 4.59, 3.25, 2.15, 3.49, 3.05, 3.49, 4.97, 5.39, 5.87, 5.77],
    'Serie 5': [0.45, 0.86, 0.69, 3.6, 3.78, 1.09, 1.03, 0.52, -0.78, -0.96, -0.32, -0.95],
    'Serie 6': [3.9, 3.99, 3.14, 1.45, 1.17, 3.69, 3.7, -0.11, 5.96, 5.87, 6.15, 5.71],
    'Serie 7': [0.66, -0.13, 1.33, 0.69, 0.74, 0.87, 0.28, 5.38, -1.37, -1.23, -0.56, -0.06],
    'Serie 8': [4.01, 4.78, 3.95, 4.27, 4.26, -0.08, 4.73, -1.11, 6.23, 5.56, 5.45, 5.1],
    'Serie 9': [-0.07, -0.61, 0.23, 0.1, 0, 4.96, -0.53, 5.89, -0.92, -0.63, 0.66, 1.1],
    'Serie 10': [4.67, 5.15, 3.55, 4.8, 4.85, -0.55, 5.67, -0.39, 5.99, 5.52, 4.21, 4.25],
    'Serie 11': [-0.69, -0.83, -0.32, -0.21, -0.55, 5.61, -1.05, 6.32, -0.16, 0.58, 1.31, 1.89],
    'Serie 12': [5.21, 5.45, 5.1, 5.35, 5.52, -0.74, 6.03, -0.32, 4.71, 3.94, 3.77, 3.56]
}

# Crear la gráfica
plt.figure(figsize=(12, 8))
for serie, valores in datos.items():
    plt.plot(meses, valores, label=serie, marker='o')

# Configurar etiquetas y título
plt.xlabel('Months')
plt.ylabel('Tide height (m)')
plt.title('Monthly Tide Height for the Year 2006')
plt.legend()
plt.grid(True)

# Mostrar gráfica
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

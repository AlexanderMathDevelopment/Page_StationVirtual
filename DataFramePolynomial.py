import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Presentd by: M.I. Alejandra Escalante Paredes
# Proposal equation: Polynomial
# The Nature Conservancy
# Delta river Colorado

# Definir las rutas de los archivos CSV
file_path_h = "C:\\Users\\draja\\OneDrive\\Documentos\\Work1TNC\\Database_2024\\Encinas Johnson_Corrected_Verified.csv"
file_path_v = "C:\\Users\\draja\\OneDrive\\Documentos\\Work1TNC\\Database_2024\\BasaDate_Model Math_Corrected_Verified.csv"

# Leer los archivos CSV en DataFrames
df_h = pd.read_csv(file_path_h)
df_v = pd.read_csv(file_path_v)

# Limpiar nombres de columnas eliminando espacios y caracteres especiales
df_h.columns = df_h.columns.str.strip()
df_v.columns = df_v.columns.str.strip()

# Ajustar los nombres de las columnas según la nueva disposición
# Ahora df_h tiene la altura de marea (H_t) y df_v tiene la velocidad del viento (V_t)
df_h = df_h[['Timestamp', 'Sea_Level']].rename(columns={'Sea_Level': 'H_t'})
df_v = df_v[['Timestamp', 'Wind_Speed']].rename(columns={'Wind_Speed': 'V_t'})

# Intercambiar los DataFrames
df_temp = df_h
df_h = df_v
df_v = df_temp

# Unir los DataFrames en base a la columna de tiempo
df = pd.merge(df_h, df_v, on='Timestamp')

# Definir las nuevas constantes
delta = 0.2
theta = 0.3

# Calcular H_nueva(t) usando la nueva fórmula predictiva
df['H_nueva'] = df['H_t'] + delta * df['V_t']**2 + theta * df['V_t']

# Asegurarse de que la altura de marea nueva no sea negativa si es necesario
df['H_nueva'] = df['H_nueva'].clip(lower=0)

# Mostrar las primeras filas para verificar el resultado
print("\nPrimeras filas del DataFrame con H_nueva(t):")
print(df.head())

# Graficar los resultados
plt.figure(figsize=(12, 6))
plt.plot(df['Timestamp'], df['H_t'], label='Original Tide Height (H(t))', color='blue')
plt.plot(df['Timestamp'], df['H_nueva'], label='New Tide Height (H_nueva(t))', color='red', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Tide Height')

# Añadir título y subtítulo
plt.title('Virtual Tide Station Encinas Johnson', fontsize=14)
plt.suptitle('The Nature Conservancy', fontsize=10, y=0.95)  # Ajusta 'y' para la posición del subtítulo

# Añadir la leyenda con el nombre del autor
plt.figtext(0.99, 0.01, 'Prepared by: **M.I. Mat Alejandra Escalante Paredes**', 
            horizontalalignment='right', fontsize=10, color='black', weight='bold')

plt.legend()
plt.grid(True)
plt.show()

# Guardar el resultado en un nuevo archivo CSV
output_file_path = "C:\\Users\\draja\\OneDrive\\Documentos\\Work1TNC\\Database_2024\\H_nueva.csv"
df.to_csv(output_file_path, index=False)

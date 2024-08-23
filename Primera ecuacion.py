import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Presented by M.I. Mat. Alejandra Escalante Paredes
#Model Sinocuidal
#The Nature Conservancy, Mexico
#DeltaRiver Colorado

# Rutas de Archivos en CVS
file_path_h = "C:\\Users\\draja\\OneDrive\\Documentos\\Work1TNC\\Database_2024\\Encinas Johnson_Corrected_Verified.csv"
file_path_v = "C:\\Users\\draja\\OneDrive\\Documentos\\Work1TNC\\Database_2024\\BasaDate_Model Math_Corrected_Verified.csv"

# Lectura de DataFrame
df_h = pd.read_csv(file_path_h)
df_v = pd.read_csv(file_path_v)

# Limpieza de columnas
df_h.columns = df_h.columns.str.strip()
df_v.columns = df_v.columns.str.strip()

# Ajuste de columnas
df_h = df_h[['Timestamp', 'Sea_Level']].rename(columns={'Sea_Level': 'H_t'})
df_v = df_v[['Timestamp', 'Wind_Speed']].rename(columns={'Wind_Speed': 'V_t'})

# Unir los DataFrames en base a la columna de tiempo
df = pd.merge(df_h, df_v, on='Timestamp')

# Definir las constantes por bibliografia
alpha = 0.5
beta = 0.1
gamma = 0.05

# Calcular H_nueva(t)
df['H_nueva'] = df['H_t'] + alpha * df['V_t'] * df['H_t'] + beta * df['V_t']**2 + gamma * np.sin(df['V_t']**3)

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

plt.legend()
plt.grid(True)
plt.show()

# Guardar el resultado en un nuevo archivo CSV
output_file_path = "C:\\Users\\draja\\OneDrive\\Documentos\\Work1TNC\\Database_2024\\H_nueva.csv"
df.to_csv(output_file_path, index=False)


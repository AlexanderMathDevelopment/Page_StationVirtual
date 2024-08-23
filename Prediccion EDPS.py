import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Definir la ruta del archivo Excel
file_path = "C:\\Users\\draja\\OneDrive\\Documentos\\Work1TNC\\Database_2024\\Nuevo_Altura_Marea.xlsx"

# Definir la ruta de la imagen a añadir
image_path = "C:\\Users\draja\OneDrive\Documentos\Work1TNC\TNCModelEquation\TNCLogoPrimary_RGB.png"  # Cambia esta ruta según tu archivo

# Leer el archivo Excel
df = pd.read_excel(file_path)

# Limpiar nombres de columnas
df.columns = df.columns.str.strip()

# Verificar si las columnas necesarias están presentes
if 'Timestamp' in df.columns and 'H_nueva' in df.columns:
    # Extraer y procesar los datos
    timestamps = pd.to_datetime(df['Timestamp'], format='%d/%m/%Y', errors='coerce')
    H_nueva = df['H_nueva'].values

    # Verificar si hay valores NaN en los timestamps y H_nueva
    if timestamps.isnull().any() or np.isnan(H_nueva).any():
        print("Error: Datos contienen valores NaN.")
        print("Fechas con errores:", timestamps[timestamps.isnull()])
        print("Valores H_nueva con errores:", H_nueva[np.isnan(H_nueva)])

        # Interpolación para rellenar valores NaN en H_nueva
        df['H_nueva'] = df['H_nueva'].interpolate(method='linear')
        H_nueva = df['H_nueva'].values  # Actualizar valores después de la interpolación

        # Recalcular valores NaN
        if np.isnan(H_nueva).any():
            print("Después de la interpolación, aún hay NaN en H_nueva.")
            print("Valores H_nueva con errores:", H_nueva[np.isnan(H_nueva)])
            # Opcional: Rellenar NaNs restantes con un valor predeterminado, por ejemplo, 0
            H_nueva = np.nan_to_num(H_nueva)

    # Convertir timestamps a números para simplificación
    time = (timestamps - timestamps.min()).astype(np.int64) / 1e9  # Tiempo en segundos

    # Crear una figura para la animación
    fig, ax = plt.subplots(figsize=(12, 6))
    line, = ax.plot([], [], lw=2)

    # Configuración de los ejes
    ax.set_xlim(0, len(H_nueva) - 1)
    ax.set_ylim(np.min(H_nueva) - 1, np.max(H_nueva) + 1)
    ax.set_xlabel('Time Index')
    ax.set_ylabel('Tide Height')
    ax.grid(True)

    # Añadir título y subtítulos
    plt.title('Virtual Tide Station "Encinas Johnson"', fontsize=14)
    plt.suptitle('The Nature Conservancy', fontsize=10, y=0.95)  # Ajusta 'y' para la posición del subtítulo
    plt.figtext(0.01, 0.01, 'Prepared by: M.I. Mat Alejandra Escalante Paredes', 
                horizontalalignment='left', fontsize=10, color='black', weight='bold')

    # Cargar la imagen (si la imagen no está disponible, usa una imagen de prueba)
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Image file not found: {image_path}. Using a placeholder image.")
        # Crear una imagen de prueba si no se encuentra el archivo
        from PIL import ImageDraw, ImageFont
        image = Image.new('RGB', (100, 100), color='white')
        d = ImageDraw.Draw(image)
        try:
            fnt = ImageFont.load_default()
            d.text((10, 40), "Logo", font=fnt, fill=(0, 0, 0))
        except IOError:
            pass

    imagebox = OffsetImage(image, zoom=0.1)  # Ajusta el zoom para la imagen según sea necesario
    ab = AnnotationBbox(imagebox, (0.05, 0.95), frameon=False, xycoords='axes fraction', boxcoords="axes fraction", pad=0.0, bboxprops=dict(boxstyle="round,pad=0.5", edgecolor="none"))
    ax.add_artist(ab)

    # Función de inicialización para la animación
    def init():
        line.set_data([], [])
        return line,

    # Función de actualización para la animación
    def update(frame):
        # Desplazar los datos de altura de marea para crear el efecto de movimiento
        shift = int(frame * len(H_nueva) / len(time)) % len(H_nueva)
        y = np.roll(H_nueva, shift)  # Desplazar los datos
        line.set_data(np.arange(len(H_nueva)), y)
        return line,

    # Crear la animación
    ani = animation.FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, interval=50)

    plt.show()

else:
    print("The columns 'Timestamp' or 'H_nueva' are not found in the file.")

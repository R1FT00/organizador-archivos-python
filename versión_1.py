import os
import shutil
os.system("cls")

# Carpeta origen:
carpeta_origen = r"C:\Users\Juan\Downloads"

# Diccionarios de tipos de archivos:
tipos_archivos = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav", ".flac"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Instaladores": [".exe", ".msi"],
}

# Listar archivos en la carpeta origen
archivos = os.listdir(carpeta_origen)

# Filtrar solo archivos
for archivo in archivos:
    ruta_completa = os.path.join(carpeta_origen, archivo)
    
    if os.path.isfile(ruta_completa):
        nombre, extension = os.path.splitext(archivo)
        print(f"Archivo: {archivo} | Nombre: {nombre} | Extensión: {extension}")



# Determinar la carpeta destino y mas
        categoria = "Otros"
        for tipo, extensiones in tipos_archivos.items():
            if extension.lower() in extensiones:
                categoria = tipo
                break

# Crear la carpeta destino si no existe
        carpeta_destino = os.path.join(carpeta_origen, categoria)
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

# Mover el archivo a la carpeta destino
        shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))
        print(f"→ Movido a: {categoria}")
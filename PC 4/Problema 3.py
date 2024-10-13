import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(url)
        if response.status_code == 200:
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(response.content)
            print(f"Imagen descargada correctamente: {nombre_archivo}")
        else:
            print("Error al descargar la imagen.")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

def comprimir_archivo(nombre_archivo, nombre_zip):
    try:
        # Crear archivo zip y añadir la imagen
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_archivo)
        print(f"Archivo comprimido correctamente en: {nombre_zip}")
    except Exception as e:
        print(f"Error al comprimir el archivo: {e}")

def descomprimir_archivo(nombre_zip):
    try:
        # Descomprimir el archivo zip
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall()
        print(f"Archivo descomprimido correctamente: {nombre_zip}")
    except Exception as e:
        print(f"Error al descomprimir el archivo: {e}")

def main():
    # URL de la imagen
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    
    # Nombre de la imagen descargada
    nombre_imagen = "imagen_descargada.jpg"
    
    # Nombre del archivo zip
    nombre_zip = "imagen_comprimida.zip"
    
    # Descargar imagen
    descargar_imagen(url, nombre_imagen)
    
    # Comprimir la imagen en un archivo zip
    comprimir_archivo(nombre_imagen, nombre_zip)
    
    # Descomprimir el archivo zip
    descomprimir_archivo(nombre_zip)
    
    # Limpiar archivos (opcional)
    if os.path.exists(nombre_imagen):
        os.remove(nombre_imagen)
    if os.path.exists(nombre_zip):
        os.remove(nombre_zip)
    print("Archivos temporales eliminados.")

if __name__ == "__main__":
    main()

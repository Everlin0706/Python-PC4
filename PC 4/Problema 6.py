def contar_lineas_codigo(archivo):
    """Cuenta las líneas de código excluyendo comentarios y líneas en blanco."""
    try:
        with open(archivo, 'r') as f:
            lineas_codigo = 0
            for linea in f:
                # Quitar espacios en blanco al principio y al final
                linea = linea.strip()
                # Ignorar comentarios o líneas vacías
                if linea and not linea.startswith("#"):
                    lineas_codigo += 1
        return lineas_codigo
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def main():
    archivo = input("Ingrese la ruta del archivo .py a analizar: ")
    
    # Verificar que el archivo termine en .py
    if not archivo.endswith('.py'):
        print("El archivo ingresado no tiene la extensión .py.")
        return
    
    # Contar las líneas de código
    lineas = contar_lineas_codigo(archivo)
    
    if lineas is not None:
        print(f"El archivo '{archivo}' tiene {lineas} líneas de código (sin contar comentarios ni líneas en blanco).")

if __name__ == "__main__":
    main()

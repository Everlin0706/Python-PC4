def leer_temperaturas(archivo):
    temperaturas = []
    try:
        # Leer el archivo de temperaturas
        with open(archivo, 'r') as f:
            for linea in f:
                # Cada línea tiene el formato: fecha, temperatura
                datos = linea.strip().split(',')
                if len(datos) == 2:
                    fecha, temp = datos
                    temperaturas.append(float(temp))
        return temperaturas
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
    except ValueError:
        print("Error en el formato del archivo.")
    return None

def calcular_estadisticas(temperaturas):
    if temperaturas:
        temp_min = min(temperaturas)
        temp_max = max(temperaturas)
        temp_promedio = sum(temperaturas) / len(temperaturas)
        return temp_promedio, temp_min, temp_max
    else:
        return None

def escribir_resumen(archivo, temp_promedio, temp_min, temp_max):
    try:
        # Escribir los resultados en un nuevo archivo
        with open(archivo, 'w') as f:
            f.write(f"Temperatura promedio: {temp_promedio:.2f}°C\n")
            f.write(f"Temperatura mínima: {temp_min:.2f}°C\n")
            f.write(f"Temperatura máxima: {temp_max:.2f}°C\n")
        print(f"Resumen escrito correctamente en {archivo}")
    except Exception as e:
        print(f"Error al escribir el archivo {archivo}: {e}")

def main():
    # Archivo de entrada
    archivo_temperaturas = 'temperaturas.txt'
    
    # Archivo de salida
    archivo_resumen = 'resumen_temperaturas.txt'
    
    # Leer las temperaturas del archivo
    temperaturas = leer_temperaturas(archivo_temperaturas)
    
    # Calcular las estadísticas
    if temperaturas:
        temp_promedio, temp_min, temp_max = calcular_estadisticas(temperaturas)
        
        # Escribir el resumen en un nuevo archivo
        escribir_resumen(archivo_resumen, temp_promedio, temp_min, temp_max)

if __name__ == "__main__":
    main()

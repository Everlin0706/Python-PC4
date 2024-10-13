import sqlite3
import pandas as pd

def obtener_tipo_cambio():
    """
    Obtiene el tipo de cambio actual del dólar desde la base de datos SQLite.
    
    Returns:
        float: El tipo de cambio del dólar en soles, o None si hay un error.
    """
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('SELECT compra FROM sunat_info ORDER BY fecha DESC LIMIT 1')
        tipo_cambio = cursor.fetchone()
        return tipo_cambio[0] if tipo_cambio else None
    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")
        return None
    finally:
        conn.close()

def procesar_ventas(archivo_csv, tipo_cambio):
    """
    Lee el archivo CSV de ventas y convierte los precios a soles.
    
    Parameters:
        archivo_csv (str): Ruta al archivo CSV de ventas.
        tipo_cambio (float): El tipo de cambio actual.
    """
    try:
        # Leer el archivo CSV
        ventas = pd.read_csv(archivo_csv)
        
        # Calcular el precio en soles
        ventas['precio_soles'] = ventas['precio_dolares'] * tipo_cambio

        # Mostrar los resultados
        print(f"{'Producto':<20} {'Precio (USD)':<15} {'Precio (S/.):<15}")
        print("-" * 50)
        
        # Iterar y mostrar cada producto
        for index, row in ventas.iterrows():
            print(f"{row['producto']:<20} {row['precio_dolares']:<15} {row['precio_soles']:<15.2f}")

    except FileNotFoundError:
        print(f"El archivo '{archivo_csv}' no se encontró.")
    except pd.errors.EmptyDataError:
        print(f"El archivo '{archivo_csv}' está vacío.")
    except pd.errors.ParserError:
        print(f"Error al procesar el archivo '{archivo_csv}'. Asegúrate de que está bien formado.")
    except Exception as e:
        print(f"Error inesperado al procesar el archivo: {e}")

def main():
    archivo_csv = 'ventas.csv'  # Asegúrate de que este archivo exista en el mismo directorio.
    
    # Obtener el tipo de cambio
    tipo_cambio = obtener_tipo_cambio()
    
    if tipo_cambio is not None:
        print(f"Tipo de cambio obtenido: {tipo_cambio:.2f} S/. por USD")
        # Procesar el archivo de ventas
        procesar_ventas(archivo_csv, tipo_cambio)
    else:
        print("No se pudo obtener el tipo de cambio.")

if __name__ == "__main__":
    main()

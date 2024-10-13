import csv

def leer_productos(archivo_csv):
    """
    Lee el archivo CSV y devuelve una lista de productos con sus datos.
    
    Parameters:
        archivo_csv (str): Ruta al archivo CSV de productos.
    
    Returns:
        list: Lista de diccionarios con datos de productos.
    """
    productos = []
    try:
        with open(archivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convertir cantidad y precio_unitario a float
                row['cantidad'] = int(row['cantidad'])
                row['precio_unitario'] = float(row['precio_unitario'])
                productos.append(row)
    except FileNotFoundError:
        print(f"El archivo '{archivo_csv}' no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    
    return productos

def calcular_precio_total(productos):
    """
    Calcula el precio total por producto.
    
    Parameters:
        productos (list): Lista de productos.
    
    Returns:
        list: Lista de productos con precios totales calculados.
    """
    for producto in productos:
        producto['precio_total'] = producto['cantidad'] * producto['precio_unitario']
    return productos

def escribir_resultados(productos, archivo_salida):
    """
    Escribe los resultados en un nuevo archivo CSV.
    
    Parameters:
        productos (list): Lista de productos con precios totales.
        archivo_salida (str): Ruta al archivo CSV de salida.
    """
    try:
        with open(archivo_salida, mode='w', newline='') as file:
            fieldnames = ['producto', 'cantidad', 'precio_unitario', 'precio_total']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for producto in productos:
                writer.writerow(producto)
        print(f"Resultados guardados en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")

def main():
    archivo_csv = 'productos.csv'        # Archivo de entrada
    archivo_salida = 'resultados.csv'     # Archivo de salida
    
    # Leer productos
    productos = leer_productos(archivo_csv)
    
    if productos:
        # Calcular precio total
        productos_con_totales = calcular_precio_total(productos)
        
        # Escribir resultados en un nuevo archivo CSV
        escribir_resultados(productos_con_totales, archivo_salida)

if __name__ == "__main__":
    main()

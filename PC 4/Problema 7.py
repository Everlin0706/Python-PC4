import requests
import sqlite3
from pymongo import MongoClient

# URL de la API de SUNAT para obtener el tipo de cambio del dólar
API_URL = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'

def obtener_datos_api():
    """Consulta la API de SUNAT y obtiene el tipo de cambio."""
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error en la API: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

def almacenar_en_sqlite(datos):
    """Almacena los datos en una base de datos SQLite."""
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        
        # Crear tabla si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sunat_info (
                fecha TEXT,
                compra REAL,
                venta REAL
            )
        ''')
        
        # Insertar los datos en la tabla
        for item in datos:
            cursor.execute('''
                INSERT INTO sunat_info (fecha, compra, venta)
                VALUES (?, ?, ?)
            ''', (item['fecha'], item['compra'], item['venta']))
        
        conn.commit()
        print("Datos almacenados en SQLite correctamente.")
    except sqlite3.Error as e:
        print(f"Error al trabajar con SQLite: {e}")
    finally:
        conn.close()

def almacenar_en_mongodb(datos):
    """Almacena los datos en MongoDB."""
    try:
        cliente = MongoClient('mongodb://localhost:27017/')
        db = cliente['sunat_db']
        coleccion = db['sunat_info']
        
        # Insertar los datos en la colección de MongoDB
        coleccion.insert_many(datos)
        print("Datos almacenados en MongoDB correctamente.")
    except Exception as e:
        print(f"Error al trabajar con MongoDB: {e}")

def mostrar_datos_sqlite():
    """Muestra los datos almacenados en SQLite."""
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM sunat_info')
        filas = cursor.fetchall()
        
        print("Datos de la tabla 'sunat_info' en SQLite:")
        for fila in filas:
            print(f"Fecha: {fila[0]}, Compra: {fila[1]}, Venta: {fila[2]}")
    except sqlite3.Error as e:
        print(f"Error al leer los datos de SQLite: {e}")
    finally:
        conn.close()

def main():
    # Obtener los datos de la API
    datos_api = obtener_datos_api()
    
    if datos_api:
        # Convertir los datos al formato adecuado
        datos = [
            {
                'fecha': item['fecha'],
                'compra': item['compra'],
                'venta': item['venta']
            }
            for item in datos_api
        ]
        
        # Almacenar en SQLite y MongoDB
        almacenar_en_sqlite(datos)
        almacenar_en_mongodb(datos)
        
        # Mostrar los datos almacenados en SQLite
        mostrar_datos_sqlite()

if __name__ == "__main__":
    main()

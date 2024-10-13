import os

def generar_tabla_multiplicar(n):
    """Genera la tabla de multiplicar del número 'n' y la guarda en un archivo."""
    nombre_archivo = f'tabla-{n}.txt'
    try:
        with open(nombre_archivo, 'w') as f:
            for i in range(1, 11):
                f.write(f'{n} x {i} = {n * i}\n')
        print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

def leer_tabla_multiplicar(n):
    """Lee la tabla de multiplicar desde el archivo 'tabla-n.txt' y la muestra por pantalla."""
    nombre_archivo = f'tabla-{n}.txt'
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                print(f"Tabla de multiplicar del {n}:")
                print(f.read())
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    else:
        print(f"El archivo {nombre_archivo} no existe.")

def mostrar_linea_tabla(n, m):
    """Muestra la línea 'm' de la tabla de multiplicar del número 'n'."""
    nombre_archivo = f'tabla-{n}.txt'
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                lineas = f.readlines()
                if 1 <= m <= len(lineas):
                    print(f"Línea {m} de la tabla del {n}: {lineas[m - 1].strip()}")
                else:
                    print(f"El archivo tiene menos de {m} líneas.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    else:
        print(f"El archivo {nombre_archivo} no existe.")

def main():
    while True:
        print("\nMenú:")
        print("1. Generar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Mostrar línea específica de una tabla de multiplicar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            try:
                n = int(input("Ingrese un número entero entre 1 y 10: "))
                if 1 <= n <= 10:
                    generar_tabla_multiplicar(n)
                else:
                    print("Por favor, ingrese un número entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        elif opcion == '2':
            try:
                n = int(input("Ingrese un número entero entre 1 y 10 para leer su tabla: "))
                if 1 <= n <= 10:
                    leer_tabla_multiplicar(n)
                else:
                    print("Por favor, ingrese un número entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        elif opcion == '3':
            try:
                n = int(input("Ingrese un número entero entre 1 y 10 para seleccionar su tabla: "))
                m = int(input("Ingrese el número de la línea que desea mostrar (1-10): "))
                if 1 <= n <= 10 and 1 <= m <= 10:
                    mostrar_linea_tabla(n, m)
                else:
                    print("Por favor, ingrese números entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

import random
from pyfiglet import Figlet

def obtener_fuente(figlet):
    fuentes_disponibles = figlet.getFonts()
    fuente = input("Ingrese el nombre de la fuente a utilizar (o presione Enter para una fuente aleatoria): ")
    if fuente not in fuentes_disponibles:
        fuente = random.choice(fuentes_disponibles)
        print(f"Fuente aleatoria seleccionada: {fuente}")
    return fuente

def main():
    figlet = Figlet()
    
    # Obtener el nombre de la fuente o seleccionar una aleatoria
    fuente_seleccionada = obtener_fuente(figlet)
    figlet.setFont(font=fuente_seleccionada)
    
    # Solicitar el texto al usuario
    texto = input("Ingrese el texto que desea imprimir: ")
    
    # Imprimir el texto con la fuente seleccionada
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()

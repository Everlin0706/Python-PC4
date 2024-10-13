import requests

def obtener_precio_bitcoin():
    try:
        # Consultar la API de CoinDesk para obtener el precio actual del bitcoin
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        precio_bitcoin = data["bpi"]["USD"]["rate_float"]
        return precio_bitcoin
    except requests.RequestException:
        print("Error al consultar la API de CoinDesk.")
        return None

def calcular_valor_bitcoins(n, precio_bitcoin):
    return n * precio_bitcoin

def main():
    try:
        # Solicitar al usuario la cantidad de bitcoins que posee
        n = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
        return
    
    precio_bitcoin = obtener_precio_bitcoin()
    
    if precio_bitcoin is not None:
        valor_total = calcular_valor_bitcoins(n, precio_bitcoin)
        # Mostrar el valor en dólares con el formato adecuado
        print(f"El valor de {n} bitcoins es: ${valor_total:,.4f} USD")
    else:
        print("No se pudo obtener el precio actual del bitcoin.")

if __name__ == "__main__":
    main()

# Conversor de Monedas

def convertir_moneda(monto, tasa_cambio):
    return monto * tasa_cambio

def conversor():
    print("Bienvenido al conversor de monedas")
    print("Opciones:")
    print("1. Pesos a Dólares")
    print("2. Dólares a Pesos")
    print("3. Euros a Dólares")
    print("4. Dólares a Euros")

    opcion = input("Elige una opción (1/2/3/4): ")

    if opcion in ['1', '2', '3', '4']:
        monto = float(input("Ingresa el monto a convertir: "))

        if opcion == '1':
            tasa_cambio = 0.05  # Ejemplo: 1 peso = 0.05 dólares
            print(f"{monto} pesos son {convertir_moneda(monto, tasa_cambio):.2f} dólares.")
        elif opcion == '2':
            tasa_cambio = 20.0  # Ejemplo: 1 dólar = 20 pesos
            print(f"{monto} dólares son {convertir_moneda(monto, tasa_cambio):.2f} pesos.")
        elif opcion == '3':
            tasa_cambio = 1.1  # Ejemplo: 1 euro = 1.1 dólares
            print(f"{monto} euros son {convertir_moneda(monto, tasa_cambio):.2f} dólares.")
        elif opcion == '4':
            tasa_cambio = 0.91  # Ejemplo: 1 dólar = 0.91 euros
            print(f"{monto} dólares son {convertir_moneda(monto, tasa_cambio):.2f} euros.")
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    conversor()
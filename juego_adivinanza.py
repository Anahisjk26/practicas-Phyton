import random


def jugar_adivinanza():
    print("Adivina la palabra secreta!")
    # Lista de palabras
    palabras = ["python", "programacion", "juego", "adivinanza", "computadora"]

    # Seleccionar una palabra secreta aleatoriamente
    palabra_secreta = random.choice(palabras)
    
    print("Ha sido seleccionada una palabra secreta. Tienes 3 intentos para adivinarla.")
    
    for i in range(len(palabra_secreta)):
        print("_", end=" ")
    
    intentos = 3

    while intentos > 0:
        intento = input("Introduce tu intento: ")
        if intento.lower() == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
        else:
            intentos -= 1
            print(f"Intenta de nuevo. Te quedan {intentos} intentos.")

    if intentos == 0:
        print(f"Lo siento, has perdido. La palabra secreta era '{palabra_secreta}'.")


if __name__ == "__main__":
    jugar_adivinanza()

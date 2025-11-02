import random


def jugar_adivinanza():
    print("Adivina la palabra secreta!")
    # Lista de palabras
    palabras = ["python", "programacion", "juego", "adivinanza", "computadora"]

    # Seleccionar una palabra secreta aleatoriamente
    palabra_secreta = random.choice(palabras)
    intentos = 3

    print("Ha sido seleccionada una palabra secreta. Tienes 3 intentos para adivinarla.")
    for i in range(len(palabra_secreta)):
        if i == 0:
            print(f"{palabra_secreta[i]} ", end="")
        print("_ ", end="")
    print()

    while intentos > 0:
        intento = input("Introduce tu intento: ").lower()
        if intento == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")
        if intentos == 2:
            pista = palabra_secreta[1]  # Primera letra como pista
            print(f"Pista: La primera letra de la palabra es '{pista}'.")
        else:
            pista = palabra_secreta[1:3]  # Primeras dos letras como pista
            print(f"Pista: Las primeras letras de la palabra son '{pista}'.")

    if intentos == 0:
        print(f"Lo siento, has perdido. La palabra secreta era '{palabra_secreta}'.")


if __name__ == "__main__":
    jugar_adivinanza()

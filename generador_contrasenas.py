# Generador de Contraseñas
import random
import string
#pasamos parametros 
def generar_contrasena(longitud, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_letters  # Letras mayúsculas y minúsculas

    if incluir_numeros:
        caracteres += string.digits  # Agregar números

    if incluir_simbolos:
        caracteres += string.punctuation  # Agregar símbolos

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def generador():
    print("Bienvenido al generador de contraseñas")

    try:
        longitud = int(input("¿De cuántos caracteres quieres la contraseña? "))
        incluir_numeros = input("¿Quieres incluir números? (s/n): ").lower() == 's'#convirte el digito en minuscula y lo compara con s
        incluir_simbolos = input("¿Quieres incluir símbolos? (s/n): ").lower() == 's'

        contrasena = generar_contrasena(longitud, incluir_numeros, incluir_simbolos)
        print(f"Tu contraseña generada es: {contrasena}")
    except ValueError:
        print("Por favor, ingresa un número válido para la longitud.")

if __name__ == "__main__":
    generador()
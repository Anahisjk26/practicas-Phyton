# Calculadora básica en Python
#se definen los metodos para las operaciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"
    
def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


#presentacion de menus y seleccion de opciones
def calculadora():
    print("calculadora lau ")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Verificar primo")

    opcion = input("Elige una opción (1/2/3/4/5/6/7): ")

    if opcion in ['1', '2', '3', '4', '5', '6', '7' ]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print(f"El resultado de la suma es: {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"El resultado de la resta es: {restar(num1, num2)}")
        elif opcion == '3':
            print(f"El resultado de la multiplicación es: {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"El resultado de la división es: {dividir(num1, num2)}")
        elif opcion == '5':
            print(f"El resultado de la potencia es: {potencia(num1, num2)}")
        elif opcion == '6':
            print(f"El resultado de la raíz cuadrada es: {raiz_cuadrada(num1)}")
        elif opcion == '7': 
            if es_primo(int(num1)):
                print(f"{int(num1)} es un número primo.")
            else:
                print(f"{int(num1)} no es un número primo.")
    print("Opción no válida. Por favor, elige una opción del 1 al 7.")

if __name__ == "__main__":
    calculadora()
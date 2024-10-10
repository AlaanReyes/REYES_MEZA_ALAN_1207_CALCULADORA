print("Welcome to CALCULADORA!")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

import math # define varias funciones matemáticas
def suma(x, y):
    # devuelve la suma de x e y
    return x + y

def resta(x, y):
    # devuelve la resta de x e y
    return x - y

def multiplicacion(x, y):
    # devuelve la multiplicacion de x e y
    return x * y

def division(x, y):
    # verifica si y es cero para evitar division por cero
    if y == 0:
        return "error: no puedes dividir por cero"
    return x / y

def factorial(x):
    # devuelve el factorial de x
    if x < 0:
        return "error: no se puede calcular el factorial de un numero negativo"
    return math.factorial(x)

def potenciacion(x, y):
    # devuelve x elevado a y
    return x ** y

def raiz_cuadrada(x):
    # devuelve la raiz cuadrada de x
    if x < 0:
        return "error: no se puede calcular la raiz cuadrada de un numero negativo"
    return math.sqrt(x)

def porcentaje(x, y):
    # devuelve el porcentaje de x basado en y
    return (x * y) / 100

def calculo_matriz():
    # solicita al usuario ingresar dos matrices
    print("ingresa los elementos de la primera matriz que quieras sacar(2x2):")
    matriz1 = [[float(input(f"elemento [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]

    print("ingresa los elementos de la segunda matriz que quieras sacar (2x2):")
    matriz2 = [[float(input(f"elemento [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]

    # calcula la suma de las matrices
    matriz_resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(2)] for i in range(2)]
    print("resultado de la suma de matrices:")
    for fila in matriz_resultado:
        print(fila)

def calculadora():
    # muestra las opciones de operacion
    print("selecciona la operacion que quieras realizar:")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. factorial")
    print("6. potenciacion")
    print("7. raiz cuadrada")
    print("8. porcentaje")
    print("9. calculo de matrices")
    print(" ") # espacio

    while True:
        # solicita al usuario que elija una operacion
        seleccion = input("ingresa el numero de la operacion (1-9): ")
        print(" ") # espacio

        if seleccion in ('1', '2', '3', '4', '5', '6', '7', '8'):
            try:
                # solicita los numeros al usuario
                num1 = float(input("ingresa el primer numero: "))
                if seleccion in ('1', '2', '3', '4'):
                    num2 = float(input("ingresa el segundo numero: "))
            except ValueError:
                # maneja el caso en que el usuario no ingresa un numero valido
                print("por favor, ingresa numeros validos.")
                continue
            # realiza la operacion seleccionada y muestra el resultado
            if seleccion == '1':
                print(f"{num1} + {num2} = {suma(num1, num2)}")
            elif seleccion == '2':
                print(f"{num1} - {num2} = {resta(num1, num2)}")
            elif seleccion == '3':
                print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
            elif seleccion == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
            elif seleccion == '5':
                print(f"factorial de {num1} = {factorial(int(num1))}")
            elif seleccion == '6':
                print(f"{num1} elevado a {num2} = {potenciacion(num1, num2)}")
            elif seleccion == '7':
                print(f"raiz cuadrada de {num1} = {raiz_cuadrada(num1)}")
            elif seleccion == '8':
                print(f"el {num1} % de {num2} = {porcentaje(num1, num2)}")
        elif seleccion == '9':
            # realiza el calculo de matrices
            calculo_matriz()
        else:
            # maneja una seleccion no valida
            print("seleccion no valida. intentalo de nuevo.")
        print(" ")
        # pregunta si el usuario quiere realizar otra operacion
        otra = input("¿quieres realizar otra operacion? (si/no): ")
        if otra.lower() != 'si':
            break
        print(" ") # espacio
if __name__ == "__main__":
    # inicio de la calculadora
    calculadora()
    

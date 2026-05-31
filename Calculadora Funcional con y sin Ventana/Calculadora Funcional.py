# Calculadora funcional
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b
def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: escribe un número válido.")
def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "5":
            print("Programa finalizado.")
            break
        if opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida. Intenta otra vez.")
            continue
        num1 = pedir_numero("Ingresa el primer número: ")
        num2 = pedir_numero("Ingresa el segundo número: ")
        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
        elif opcion == "4":
            resultado = dividir(num1, num2)
        print("Resultado:", resultado)
# Iniciar programa
calculadora()

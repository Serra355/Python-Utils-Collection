
def cantidad_Num(operacion):
    while True:
        try:
            return int(input(f"Cuantos numeros desea {operacion}: "))
        except ValueError:
            print("Numero no reconocido")


def pedir_Num(mensaje):
    while True:
        try: 
            return float(input(mensaje))
        except: 
            print("Input invalido")

def suma():
    print("\n-- -- SUMA -- --")
    cantidad = cantidad_Num("sumar")
    result = 0
    for i in range(cantidad):
        numero = pedir_Num(f"Ingresa el {i+1}º numero: ")
        result += numero
    print(f"Resultado de la suma: {result:g}")

def resta():
    print("\n-- -- RESTA -- --")
    cantidad = cantidad_Num("restar")
    result = pedir_Num("Ingresa el numero inicial: ")
    for i in range(cantidad):
        numero = pedir_Num(f"Ingresa el {i+1}º numero: ")
        result -= numero
    print(f"Resultado de la resta: {result:g}")

def multiplicacion():
    print("\n-- -- MULTIPLICACION -- --")
    cantidad = cantidad_Num("multiplicar")
    result = 1
    for i in range(cantidad):
        numero = pedir_Num(f"Ingresa el {i+1}º numero: ")
        result *= numero
    print(f"Resultado de la multiplicacion: {result:g}")

def division():
    print("\n-- -- DIVISION -- --")
    cantidad = cantidad_Num("dividir")
    result = pedir_Num("Ingrese el numero inical a dividir: ")
    for i in range(cantidad):
        while True:
            divisor = pedir_Num(f"Ingrese el {i+1}º divisor: ")
            if divisor == 0:
                print("Error, no se puede dividir entre 0. Prueba con otro numero")
            else:
                result /= divisor
                break
    print(f"Resultado: {result:g}")


def menu():    
    print("\nBienvenido/a a esta calculadora. Operaciones disponibles: ")
    print("Suma (+), Resta (-), Multiplicacion (x, ·, *), Division (/)")
    print("\nPara salir del programa escriba: exit")


print("-- CALCULADORA --")
while True:
    menu()
    operacion = input("\nQue operacion desea hacer: ")
    if operacion == "+":
        suma()
    elif operacion == "-":
        resta()
    elif operacion == "x" or operacion == "·" or operacion == "*":
        multiplicacion()
    elif operacion == "/":
        division()
    elif operacion == "exit":
        break
    else:
        print("Operacion no reconocida")




import json


def cargar_base_datos():
    try:
        with open("circuitos.json", "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print("Error: No se encuentra el archivo 'circuitos.json'.")
        return {}

def pedir_dato(mensaje, minimo = 0, maximo = float('inf')):
    while True:
        try:
            dato = float(input(mensaje))
            if minimo <= dato <= maximo:
                return dato
            else:
                print(f"Error: El valor debe estar entre {minimo} y {maximo}.")

        except ValueError:
            print("Error, dato invalido. Prueba de nuevo.")

def obtener_datos_circuito(base__datos):
    print("\n---- SELECCION DE CIRCUITO ----")
    print("Circuitos disponibles: Bahrain, Jeddah, Australia, Mónaco, Baku, Spa, Monza, Las Vegas, Spain \n")

    while True:
        entrada = input("Escribe el nombre del circuito (o escribe 'manual' para introducir los datos: )").lower().strip()

        if entrada == "manual":
            consumo = pedir_dato("Introduce el consumo manual (kg/vuelta): ", 1, 10)
            prob_sc = pedir_dato("Introduce la probabilidad de safety car (0-100%)", 0 , 100)
            return consumo, prob_sc

        elif entrada in base__datos:
            datos = base__datos[entrada]
            consumo = datos["consumo"]
            prob_sc = datos["prob_sc"]

            print(f"Datos cargados de {entrada.capitalize()}: ")
            print(f"    - Cosumo: {consumo} kg/vuelta")
            print(f"    - Prob. SC: {prob_sc}%")
            return consumo, prob_sc
        
        else:
            print("Circuito no encontrado en la base de datos. Intentalo de nuevo o escribe 'manual'.")

def pedir_vueltas():
    while True:
        try:
            vueltas = int(input("Cuantas vueltas tiene la carrera: "))
            return vueltas
        except ValueError:
            print("Error, dato invalido. Prueba de nuevo.")





print("-- -- F1 FUEL STRATEGY -- --\n")
consumo_circuitos = cargar_base_datos()
gasolina_x_vuelta, probabilidad_sc = obtener_datos_circuito(consumo_circuitos)
numero_vueltas = pedir_vueltas()
base = gasolina_x_vuelta * numero_vueltas
if probabilidad_sc >= 50:
    base = base * 0.9

resultado_final = base + 1

print("\n --- INFORME DE ESTRATEGIA --- ")
print(f"Combustible base necesario: {base:.2f} kg")
if probabilidad_sc >= 50:
    print("Estrategia Agresiva: Se ha descontado un 10% por alta probabilidad de SC.")
else:
    print("Estrategia Estándar: Probabilidad de SC baja.")

print(f"Muestra obligatoria FIA: +1.00 kg")
print(f"CARGA FINAL RECOMENDADA: {resultado_final:.2f} kg")

import string
import secrets


def repeticiones():
    while True:
        try:
            iteraciones = int(input("Cuantos caracteres quieres que tenga la contraseña (num > 8): "))
            if iteraciones < 8:
                print("El numero de caracteres no puede ser menor que ocho. Intentalo de nuevo.\n")
                continue
            else:
                return iteraciones
        except ValueError:
            print("Input incorrecto\n")

def contraseña(longitud):
    alfabeto_completo = string.ascii_letters + string.digits + string.punctuation
    contraseña = []

    for i in range(longitud):
        caracter_elegido = secrets.choice(alfabeto_completo)
        contraseña.append(caracter_elegido)
    return "".join(contraseña)

if __name__ == "__main__":
    print("-- -- GENERADOR DE CONTRASEÑAS -- --")
    longitud = repeticiones()
    password = contraseña(longitud)
    print(f"La contraseña generada es: {password}")
import random

# Variables: Lista de palabras y condiciones del juego
palabras = ["innovación", "crecimiento", "liderazgo", "estrategia", "emprendimiento", "negocios", "éxito", "mercado"]
vidas = 5
aciertos = 0
desaciertos = 0

# Generar una palabra aleatoria
palabra_aleatoria = list(random.choice(palabras).lower())
letras_adivinar = set(palabra_aleatoria)

# Reemplazando las letras por guiones bajos para mostrar al concursante
espacios = ["_"] * len(palabra_aleatoria)

# Validando el tipo de la letra
def input_letra():
    while True:
        letra = input("Ingresa una letra para completar la palabra: ").upper()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Ingresaste un dato inválido. Por favor, ingresa una sola letra.")

# Completando la palabra
def completar_palabra(espacios, letras_adivinar, letra):
    global vidas, aciertos, desaciertos
    if letra.lower() in letras_adivinar:
        for i in range(len(palabra_aleatoria)):
            if palabra_aleatoria[i] == letra.lower():
                espacios[i] = letra.upper()
                aciertos += 1
        print(f"¡Muy bien! Sigues adivinando. Ahora te falta completar: {espacios}")
    else:
        desaciertos += 1
        vidas -= 1
        print(f"¡Oh no! La letra {letra} no está en la palabra. Te quedan {vidas} vidas.")
    
    print(f"Tu status en el juego es:\n Vidas: {vidas} \n Aciertos: {aciertos} \n Desaciertos: {desaciertos}")
    return espacios

# Bienvenida al Juego
print("\nEMPIEZA EL GRAN JUEGO INTERACTIVO ¡ADIVINA LA PALABRA!\n")
respuesta = input("¿Quieres jugar? \n Responde Sí o No: ")
if respuesta.lower() == "si":
    print("¡VAMOS! ¡Comencemos a Jugar!")
    name = input("Ingresa tu nombre: ").upper()
    print(f"Ok {name}, la palabra a adivinar tiene {len(palabra_aleatoria)} letras: {espacios}")
    print("Tienes 5 vidas. Por cada intento erróneo perderás 1. Pierdes el juego al llegar a 0 vidas.\n¡Mucha Suerte!\n")
    
    while vidas > 0:
        print("\nSigamos jugando...")
        letra = input_letra()
        completar_palabra(espacios, letras_adivinar, letra)
        if "_" not in espacios:
            print(f"¡Felicidades {name}! Has adivinado la palabra: {''.join(palabra_aleatoria).upper()}")
            break
    else:
        print(f"¡Perdiste el Juego! La palabra era: {''.join(palabra_aleatoria).upper()}")
else:
    print("Okis ¡Hasta la próxima!")

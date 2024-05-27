import random
import unicodedata

# Variables: Lista de palabras y condiciones del juego
palabras = ["innovación", "crecimiento", "liderazgo", "estrategia", "emprendimiento", "negocios", "éxito", "mercado"]
vidas = 5
aciertos = 0
desaciertos = 0

# Generar una palabra aleatoria
palabra_aleatoria = list(random.choice(palabras).lower())

# Función para eliminar acentos
def eliminar_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# Crear el conjunto de letras a adivinar sin acentos
letras_adivinar = set(eliminar_acentos(''.join(palabra_aleatoria)))

# Reemplazando las letras por guiones bajos para mostrar al concursante
espacios = ["_"] * len(palabra_aleatoria)

# Validando el tipo de la letra
def input_letra():
    while True:
        letra = input("Ingresa una letra para completar la palabra: ").upper()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("\nIngresaste un dato inválido. Por favor, ingresa una sola letra.")

# Completando la palabra
def completar_palabra(espacios, letras_adivinar, letra):
    global vidas, aciertos, desaciertos
    letra_normalizada = eliminar_acentos(letra.lower())
    if letra_normalizada in letras_adivinar:
        for i in range(len(palabra_aleatoria)):
            if eliminar_acentos(palabra_aleatoria[i]) == letra_normalizada:
                espacios[i] = palabra_aleatoria[i].upper()
                aciertos += 1
        print(f"¡Muy bien! Sigues adivinando. Ahora te falta completar: {espacios}")
    else:
        desaciertos += 1
        vidas -= 1
        print(f"\n¡Oh no! La letra {letra} no está en la palabra. Aún te falta completar: {espacios}")
    
    print(f"Tu status en el juego es:\n Vidas: {vidas} --- Aciertos: {aciertos} --- Desaciertos: {desaciertos}")
    return espacios

# Bienvenida al Juego
print("\nEMPIEZA EL GRAN JUEGO INTERACTIVO ¡ADIVINA LA PALABRA!\n")
while True:
    respuesta = input("¿Quieres jugar? \n Responde Si o No: ")
    if respuesta.lower() == "si" and respuesta.isalpha():
        print("\n¡VAAAAMOOSSSS! ¡Comencemos a Jugar!")
        name = input("Ingresa tu nombre: ").upper()
        print(f"\nOk {name}, la palabra a adivinar tiene {len(palabra_aleatoria)} letras: {espacios}")
        print("Tienes 5 vidas. Por cada intento erróneo perderás 1. Pierdes el juego al llegar a 0 vidas.\n¡Mucha Suerte!\n")
    
        while vidas > 0:
            print("\nSigamos jugando...")
            letra = input_letra()
            completar_palabra(espacios, letras_adivinar, letra)
            if "_" not in espacios:
                print(f"\n¡Felicidades {name}! Has adivinado la palabra: {''.join(palabra_aleatoria).upper()}\n")
                break
        else:
            print(f"\n\n¡Perdiste el Juego! La palabra era: {''.join(palabra_aleatoria).upper()}")
            break
    elif respuesta.lower() == "no" and respuesta.isalpha():
        print("\nOkis ¡Hasta la próxima!")
        break
    else:
        print("Ingresaste un valor inválido. Vamos de nuevo.\n")    




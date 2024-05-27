import random
import unicodedata

# Variables globales
palabras = ["innovación", "crecimiento", "liderazgo", "estrategia", "emprendimiento", "negocios", "éxito", "mercado"]
vidas = 5
aciertos = 0
desaciertos = 0
palabra_aleatoria = []
letras_adivinar = set()
espacios = []

# Función para generar una nueva palabra aleatoria y reiniciar el juego
def iniciar_juego():
    global palabra_aleatoria, letras_adivinar, espacios, vidas, aciertos, desaciertos
    palabra_aleatoria = list(random.choice(palabras).lower())
    letras_adivinar = set(eliminar_acentos(''.join(palabra_aleatoria)))
    espacios = ["_"] * len(palabra_aleatoria)
    vidas = 5
    aciertos = 0
    desaciertos = 0

# Función para eliminar acentos
def eliminar_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


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
        letra_revelada = False
        for i in range(len(palabra_aleatoria)):
            if eliminar_acentos(palabra_aleatoria[i]) == letra_normalizada and espacios[i] == "_":
                espacios[i] = palabra_aleatoria[i].upper()
                letra_revelada = True
        #if letra_revelada:
                aciertos += 1 #decidí dar 1 acierto por cada letra revelada/impresa y no por cada intento.
        print(f"¡Muy bien! Sigues adivinando. Ahora te falta completar: {' '.join(espacios)}")
    else:
        desaciertos += 1
        vidas -= 1
        print(f"\n¡Oh no! La letra {letra} no está en la palabra. Aún te falta completar: {' '.join(espacios)}")
    
    print(f"Tu status en el juego es:\n Vidas: {vidas} \n Aciertos: {aciertos} \n Desaciertos: {desaciertos}")
    return espacios

# Bienvenida al Juego
print("\nEMPIEZA EL GRAN JUEGO INTERACTIVO ¡ADIVINA LA PALABRA!\n")
while True:
    respuesta = eliminar_acentos(input("¿Quieres jugar? \n Responde Si o No: ").lower())
    if respuesta == "si" and respuesta.isalpha():
        print("\n¡VAAAAMOOSSSS! ¡Comencemos a Jugar!")
        name = input("Ingresa tu nombre: ").upper()

        while True:
            iniciar_juego()
            print(f"\nOk {name}, la palabra a adivinar tiene {len(palabra_aleatoria)} letras: {' '.join(espacios)}")
            print("Tienes 5 vidas. Por cada intento erróneo perderás 1. Pierdes el juego al llegar a 0 vidas. Aciertos = número de letras adivinadas\n¡Mucha Suerte!\n")

            while vidas > 0:
                print("\nSigamos jugando...")
                letra = input_letra()
                completar_palabra(espacios, letras_adivinar, letra)
                if "_" not in espacios:
                    print(f"\n¡Felicidades {name}! Has adivinado la palabra: {''.join(palabra_aleatoria).upper()}\n")
                    break
            else:
                print(f"\n\n¡Perdiste el Juego! La palabra era: {''.join(palabra_aleatoria).upper()}")

            while True:
                jugar_de_nuevo = eliminar_acentos(input(f"¿Quieres volver a jugar {name}? Responde Si o No: ").lower())
                if jugar_de_nuevo == "si" and jugar_de_nuevo.isalpha():
                    break
                elif jugar_de_nuevo == "no" and jugar_de_nuevo.isalpha():
                    print(f"\nOkis ¡Hasta la próxima {name}!")
                    exit()
                else:
                    print(f"Ingresaste un valor inválido {name}. Vamos de nuevo.\n")
    elif respuesta == "no" and respuesta.isalpha():
        print("\nOkis ¡Hasta la próxima!")
        break
    else:
        print("Ingresaste un valor inválido. Vamos de nuevo.\n")
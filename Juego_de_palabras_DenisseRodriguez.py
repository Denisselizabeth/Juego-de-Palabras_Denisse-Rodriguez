import random

# Variables: Lista de palabras y condiciones del juego
palabras = ["innovación", "crecimiento", "liderazgo", "estrategia", "emprendimiento", "negocios", "éxito", "mercado"]
vidas = 5
aciertos = 0
desaciertos = 0

# Generar una palabra aleatoria
palabra_aleatoria = list(random.choice(palabras).lower())
#def elegir_palabra(palabras):
    #palabra_aleatoria = choice(palabras)
    #return palabra_aleatoria.upper()
letras_adivinar=set(palabra_aleatoria)  


# Reemplazando las letras por subguiones para mostrar al concursante
espacios=[]
list(filter(lambda i: espacios.append("_"),palabra_aleatoria))

#validando el type de la letra
def input_letra(letra):
    while True:
        if len(letra) == 1 and isinstance(letra, str):
            #return letra
            completar_palabra(espacios,letras_adivinar,letra)
            break
        else:
            print("Ingresate un dato inválido·")

#validando continuidad en el juego


#Completando la palabra
def completar_palabra(espacios,letras_adivinar,letra):
    global vidas, aciertos, desaciertos
    if letra in letras_adivinar:
        for i in range(len(palabra_aleatoria)):
            if palabra_aleatoria[i]==letra:
                espacios[i]=letra
                aciertos+=1
        print (f"¡Muy bien!. Ganaste la partida. \nAhora te falta completar:{espacios}")
        print(f"Tu status en el juego es:\n Vidas: {vidas} \n Aciertos: {aciertos} \n Desaciertos: {desaciertos}")
    else:
        desaciertos+=1
        vidas-=1
        print (f"¡Oh no ='(!. Perdista la partida pero sigues participando. \nAún falta por completar más letras:{espacios}")
        print(f"Tu status en el juego es:\n Vidas: {vidas} --- Aciertos: {aciertos} --- Desaciertos: {desaciertos}")
    return espacios
print (espacios)

#Bievenida al Juego
print("\nEMPIEZA EL GRAN JUEGO INTERACTIVO ¡ADIVINA LA PALABRA!\n")
respuesta = input("¿Quieres jugar? \n Responde Si o No: ")
if respuesta.lower() == "si":
    print("¡VAMOS! ¡Comencemos a Jugar!")
    name=input("Ingresa tu nombre: ").upper()
    print(f"Ok {name}, la palabra a adivinar tiene {len(palabra_aleatoria)} letras: {espacios}")
    print("Tienes 5 vidas. Por cada intento erróneo perderás 1. Pierdes el juego al llegar a 0 vidas.\n¡Mucha Suerte!\n")
    while vidas>=1: #and aciertos<len(letras_adivinar):
        print("\nSigamos jugando...")
        letra=str(input("Ingresa una letra para completar la palabra: ").upper())
        input_letra(letra)
    else:
        print(f"¡Perdiste el Juego! La palabra era: {palabra_aleatoria}")
else:
    print("Okis ¡Hasta la próxima!")
    exit()
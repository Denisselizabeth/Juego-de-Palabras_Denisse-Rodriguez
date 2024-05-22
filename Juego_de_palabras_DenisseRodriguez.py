import random

# Lista de palabras
palabras = ["innovación", "crecimiento", "liderazgo", "estrategia", "emprendimiento", "negocios", "éxito", "mercado"]

# Generar una palabra aleatoria
palabra_aleatoria = random.choice(palabras)
espacios = palabra_aleatoria.count
#for i in espacios:
    #espacios.append(" _ ")

list(filter(lambda letra: letra == " _ ",espacios))
print("BIENVENIDOS AL GRAN JUEGO INTERACTIVO ¡ADIVINA LA PALABRA!\n")
print(f"La Palabra a adivinar tiene: {espacios} letras")
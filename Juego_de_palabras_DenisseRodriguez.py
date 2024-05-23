import random

# Lista de palabras
palabras = ["innovación", "crecimiento", "liderazgo", "estrategia", "emprendimiento", "negocios", "éxito", "mercado"]

# Generar una palabra aleatoria
palabra_aleatoria = list(random.choice(palabras))

# Reemplazando las letras por subguiones para mostrar al concursante
espacios=[]
list(filter(lambda i: espacios.append("_"),palabra_aleatoria))
print("\nEMPIEZA EL GRAN JUEGO INTERACTIVO ¡ADIVINA LA PALABRA!\n")
print(f"La Palabra a adivinar tiene {len(palabra_aleatoria)} letras: {espacios}")
print("Tienes 5 vidas. Por cada intento erróneo perderás 1. Pierdes el juego al llegar a 0 vidas.\n¡Mucha Suerte!\n")

# Variables y frases de las condiciones del juego
vidas=5
intentos_incorrectos=5

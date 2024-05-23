import random

# Lista de palabras
palabras = ["innovación", "crecimiento", "liderazgo", "estrategia", "emprendimiento", "negocios", "éxito", "mercado"]

# Generar una palabra aleatoria
palabra_aleatoria = list(random.choice(palabras))
#letras = list(palabra_aleatoria)
print(palabra_aleatoria)
espacios=[]
#for i in letras:
    #espacios.append("_")
list(filter(lambda i: espacios.append("_"),palabra_aleatoria))
print(f"La Palabra a adivinar tiene {len(palabra_aleatoria)} letras: {espacios}")
#print("BIENVENIDOS AL GRAN JUEGO INTERACTIVO ¡ADIVINA LA PALABRA!\n")

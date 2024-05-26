import random

# Variables: Lista de palabras y condiciones del juego
palabras = ["innovación", "crecimiento", "liderazgo", "estrategia", "emprendimiento", "negocios", "éxito", "mercado"]
vidas=5
aciertos=0
desaciertos=0

# Generar una palabra aleatoria
#def elegir_palabra(palabras):
    #palabra_aleatoria = choice(palabras)
    #return palabra_aleatoria.upper()
palabra_aleatoria = list(random.choice(palabras).lower())
letras_adivinar=set(palabra_aleatoria)


# Reemplazando las letras por subguiones para mostrar al concursante
espacios=[]
list(filter(lambda i: espacios.append("_"),palabra_aleatoria))


#Completando la palabra
def completar_palabra(espacios,letras_adivinar,letra):
    while vidas>=1 and aciertos<len(letras_adivinar):
        print("Seguimos jugando...")
        letra=str(input("Ingresa una letra para completar la palabra").lower())
        try:
            if letra in letras_adivinar:
                for i in range(len(palabra_aleatoria)):
                    if palabra_aleatoria[i]==letra:
                        espacios[i]=letra
                        aciertos+=1
                        print ("¡Muy bien!. Ganaste la partida. \nAhora te falta completar:{espacios}")
                        print("Tu status en el juego es:\n Vidas: {vidas} \n Aciertos: {aciertos} \n Desaciertos: {desaciertos}")
            else:
                desaciertos+=1
                vidas-=1
                print ("¡Oh no ='(!. Perdista la partida. Aún falta por completar más letras:{espacios}")
                print("Tu status en el juego es:\n Vidas: {vidas} \n Aciertos: {aciertos} \n Desaciertos: {desaciertos}")
        except Exception as e:
            print (f"el error fue {e}") ### imprime el error que identifica python
    else:
        print("¡Perdiste el Juego! La palabra era: {palabra_aleatoria}")
    return espacios


#Bievenida al Juego
print("\nEMPIEZA EL GRAN JUEGO INTERACTIVO ¡ADIVINA LA PALABRA!\n")
respuesta = input("¿Quieres jugar? \n Responde Si o No: ")
try:
    if respuesta.lower() == "si":
        print("¡VAMOS! ¡Comencemos a Jugar!")
        name=input("Ingresa tu nombre: ").upper()
        print(f"Ok {name}, la palabra a adivinar tiene {len(palabra_aleatoria)} letras: {espacios}")
        print("Tienes 5 vidas. Por cada intento erróneo perderás 1. Pierdes el juego al llegar a 0 vidas.\n¡Mucha Suerte!\n")
        completar_palabra(espacios,letras_adivinar,letra)
    else:
        print("¡Hasta la próxima!")
        exit()
except Exception as e:
    print (f"el error fue {e}") ### imprime el error que identifica python

#try / except
#try: 
 #   print(num/num2)
#except ZeroDivisionError:
  #  print ("Error de división para 0")
#except TypeError:
   # print ("Ingresaste un número en vez de una letra")
#except ValueError: ### SyntaxError
    print ("Ingresaste un número en vez de una letra")
#except Exception as e:
 #   print("Error, no se puede dividir para 0")
  #  print (f"el error fue {e}") ### imprime el error que identifica python
#finally:
    #print ("Programa finalizado") 

#### otra forma de validar datos
## if radio <0
###   raise Exception ("El radio no puede tomar valor 0")

#errores a controlar: el tipo de variable a ingresar debe ser str y debe ser 1 única letra
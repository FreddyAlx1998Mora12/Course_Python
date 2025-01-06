"""Esta clase es una practica o ejercicio que hace lo siguiente:
1 - Por medio del terminal, se le pide al usuario responder preguntas
2 - Cada pregunta y respuesta sera almacenada en un archivo..."""
import os
import time

mensaje_bienvenida = """
------- Encuesta ------
Por favor, lee detenidamente las preguntas y responda lo que se le pide.
Muchas gracias por su atencion y comprension..
"""
print(mensaje_bienvenida)

# Variable para identificar actividad de encuesta
encuesta_activa = True
# Ruta de archivos a almacenarse o crearse
ruta_archivo = 'lista de invitados generados por EJERCICIO en Python.txt'

# Lista de preguntas
preguntas = ['Ingrese su nombre: ',
             'Ingrese su edad: ',
             'Cual es su lenguaje de programacion preferido: ',
             'Que lenguaje te gustaria aprender: ',
             'Que especialidad de la informatica te gustaria seguir: ']
respuestas = []

while encuesta_activa:
    # Itera cada pregunta y muestrale al user
    for pregunta in preguntas:
        respuesta = input(pregunta)
        respuestas.append(respuesta)

    # Muestra las respuestas ingresadas
    print(respuestas)

    # Almacenamos en un archivo
    # Una vez realizadas las preguntas y almacenadas las respuestas
    # Simultaneamente escribe en el archivo
    with open(ruta_archivo, 'a') as archivo:
        for pregunta, respuesta in zip(preguntas, respuestas):
            archivo.write(f'{pregunta}\n\t{respuesta}\n')
        archivo.write('\n' + '-' * 40 + '\n\n')
    pregunta_control = input('Desea ingresar algun otro dato? S/N: ')

    if 'n' in pregunta_control.lower():
        # Sale de la encuesta
        encuesta_activa = False
    else:
        # Limpia las respuestas y vuelve al inicio bucle
        respuestas = []

print('Gracias por usar nuestro programa de coleccion de datos..')
# Espera 5 segundos
time.sleep(5)
# Limpia la consola
os.system('cls')

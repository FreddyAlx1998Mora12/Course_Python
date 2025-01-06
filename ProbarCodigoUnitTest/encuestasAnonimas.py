from claseEncuestas import EncuestaAnonima

# Definimos una pregunta para instanciar una clase
question = "Que lenguaje de progrmacion te gustaria aprender?"
question2 = "Que campo de la informatica te gustaria especializarte?"

# Instanciamos una clase o objeto, e inicializamos la pregunta
encuesta1 = EncuestaAnonima(question)
encuesta2 = EncuestaAnonima(question2)


def ejecutar_encuesta(encuesta):
    # Muestra la pregunta y empieza a recopilar informacion
    encuesta.mostrar_pregunta()

    print("Presione \'q\' para finalizar recopilacion de datos. ")

    while True:
        respuesta = input("Respuesta: ")
        if respuesta == "q":
            break

        # Guarda la respuesta recopilada
        encuesta.guardar_respuestas(respuesta)

    # Una vez finalizado el buvle de ejecucion o encuesta
    print('\nGracias por participar en la encuesta..')


ejecutar_encuesta(encuesta1)
print()
encuesta1.muestra_resultados()
print()
ejecutar_encuesta(encuesta2)
print()
encuesta2.muestra_resultados()

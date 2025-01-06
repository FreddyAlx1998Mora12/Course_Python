"""Programacion Funcional """

# Simularemos como si se tratara de un traductor de idiomas


def saludar(opcion):
    """Funcion saludar, segun la opcion o idioma elegido"""
    def saludar_es():
        """Funcion que saluda en el idioma espaniol """
        print("Eligio Espaniol... Hola!")

    def saludar_en():
        """Funcion que saluda en el idioma ingles """
        print("You selected language English... Hi! or Hello!")

    def saludar_fr():
        """Funcion que saluda en el idioma frances elegido """
        print("Elegie le idieme, de franche, hole!, vah! Saluts! Bonjour!")

    # Funcion guardado en tipo diccionario clave:valor
    funcion_lenguage = {"es": saludar_es,
                        "en": saludar_en,
                        "fr": saludar_fr}

    # Retorna la funcion lenguaje con la clave de la opcion dada..
    return funcion_lenguage[opcion]


opcion_idioma = input(
    "Elige su idioma....\n Espaniol = \"es\", Ingles = \"en\", Frances = \"fr\" = ")

resultado = saludar(opcion_idioma)

# En resultado se almacena la funcion saludar.saludar_es() o una de ellas, asi que para ver su resultado debemos usar la variable
# resultado seguido de ()
# En pocas palabras lo que retorna es una funcion no una variable concreta en si...

resultado()

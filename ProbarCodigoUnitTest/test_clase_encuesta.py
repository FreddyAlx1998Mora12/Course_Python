import unittest as ut
from claseEncuestas import EncuestaAnonima as e


class Test_ClaseEncuesta(ut.TestCase):
    # Metodo que permite la creacion de una clase
    def setUp(self):
        """Metodo que crea una clase encuesta con sus variables definidas (pregunta),
        listas para usarse una sola vez a nivel de toda la clase de test,
        con una lista de respuestas para usarse en cada metodo.
        Es decir, evita la instanciacion repetitiva para cada metodo o funcion"""

        pregunta = 'Pregunta: Que idioma te gustaria aprender?'
        # crea un objeto encuesta
        self.encuesta = e(pregunta)
        self.respuestas = ['English', 'Frances', 'Chino', 'Catalan']

    # Creamos una funcion sobre que es lo que vamos a evaluar
    def testear_almacenamiento_respuesta(self):
        """Funcion que testea si un elemento se guarda bien y se encuentre en el eobjeto"""
        # Empezamos a usar la clase como si fuese POO

        # pregunta
        # q = 'Que idioma te gustaria aprender?'
        # instanciamos objeto
        # encuesta = e(q)  # Sin setup
        # muestra pregunta
        # encuesta.mostrar_pregunta()  # Sin setUp

        self.encuesta.mostrar_pregunta()  # Con Setup nos ahorramos las 2 lineas anteriores

        # guarda una respuesta
        # encuesta.guardar_respuestas('english')  # Modificaremos de acuerdo al setUp
        self.encuesta.guardar_respuestas(self.respuestas[0])  # Lo que hace es guardar una respuesta del self.respuesta

        # Verifica si el elemento que guarde esta en la lista de respuestas
        # Es decir, en la variable del Objeto, responses es una variable de tipo lista del objeto Encuesta

        # self.assertIn('english', encuesta.responses)  # Prueba que falla
        # print(self.encuesta.responses)
        self.assertIn('English', self.encuesta.responses)  # Prueba que pasa

    def testear_almacenamiento_varias_respuestas(self):
        """Funcion testea el almacenamiento de varias respuestas"""

        q = 'Cuantos idiomas te gustaria aprender?'  # Pregunta
        r = ['ingles', 'frances', 'portugues']  # respuestas

        # Instnaciamos
        # encuesta = e(q)  # Sin setUp
        # encuesta.mostrar_pregunta()  # Sin setUp
        # Guardaremos cada una de las respuestas
        for respuesta in r:
            # encuesta.guardar_respuestas(respuesta)  # Sin setUp
            self.encuesta.guardar_respuestas(respuesta)

        # Verificaremos si los mismos elementos q guardamos se alamacenaron
        for respuesta in r:
            self.assertIn(respuesta, self.encuesta.responses)


if __name__ == '__main__':
    ut.main()

"""Clase para someter a prueba unitaria"""
# Metodos assert que ofrece la clase unittest
# assertEqual(a,b) -> Verifica que a == b
# assertNotEqual(a,b) -> Verifica que a != b
# assertTrue(a) -> Verifica que a sea True
# assertFalse(a) -> Verifica que a sea False
# assertIn(elemento, lista) -> Verifica que el elemento este en lista
# assertNotIn(elemento, lista) -> Verifica que el elemento no este en lista


class EncuestaAnonima:
    """Clase que recoge respuestas anonimas a una pregunta de una encuesta"""
    def __init__(self, question):
        self.question = question
        self.responses = []

    def mostrar_pregunta(self):
        """Muestra la pregunta del sondeo"""
        print(self.question)

    def guardar_respuestas(self, new_response):
        """Guarda la respuesta del sondeo"""
        self.responses.append(new_response)

    def muestra_resultados(self):
        """Muestra todos los resultados, pregunta y respuestas"""
        print('Pregunta:', self.question)
        print('Respuestas:', end="\t")
        for resp in self.responses:
            print(f'- {resp}')

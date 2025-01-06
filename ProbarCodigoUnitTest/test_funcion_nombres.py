"""Testeo de funcion nombres
Para testear funciones, debe solo tener en una clase con la/las funciones
que se necesitan poner a prueba."""

import unittest as ut
from funcion_nombres import formatearNombres


# Clase que hereda las funcionalidades de TestsUnitarios
class TestFuncionNombres(ut.TestCase):
    """Pruebas para 'funcion_nombres.py' funciones de nombres"""

    def test_nombres_apellidos(self):
        """Funcion que comprueba datos como Cristhian Lara
        o nombres compuestos como Maria Jose Ramirez"""
        # Algo que recalcar, no es muy conveniente en este caso
        # de alguna forma manejar excepciones, dado que la prueba
        # resulta como un test passed independiemente del resultado obtenido y esperado
        try:
            # Verifica si el resultado obtnido es igual al dato esperado
            self.assertEqual(formatearNombres('cristhian', 'lara'),
                             'Cristhian David Lara')
        except AssertionError as e:
            print('\nResultado Final Testing: No paso la prueba de testeo. ', e)
        else:
            # Caso de exito, quiere decir que la prueba paso con exito.
            print('Resultado Final Testing: Paso la prueba de testeo con exito. ')


# Si se esta ejecutando en rama principal
if __name__ == '__main__':
    # Ejecuta primero la unittest, lo que ejecutara la clase
    ut.main()

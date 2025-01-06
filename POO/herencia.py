"""Herencia de Clases y Herencias Multiples"""

# Clase Padre


class Acuatico:
    """Atributos de Clase Padre"""

    def __init__(self):
        pass

    def nadar(self):
        print("Estamos bajo el agua")

    def salir_superficie(self, dato=''):
        print("Ey "+dato+"!, Escapamos a ver que hay afuera del planeta...")

    def entrar_agua(self):
        print("Explorando a mar adentro....")

# Clase Hijo


class Tortuga(Acuatico):
    # Redefine el constructor de la clase Padre
    def __init__(self, nombre, edad):
        super().__init__()
        self.nombre = nombre
        self.edad = edad

    def caminar_superficie(self):
        print("Estoy Caminando fuera del agua...")


class Pinguino(Acuatico):
    def __init__(self):
        super().__init__()


tortuga_1 = Tortuga("Kerly", 1231)
pinguino_1 = Pinguino()
pinguino_1.salir_superficie()

# tortuga_1.nadar()
tortuga_1.salir_superficie(tortuga_1.nombre)
# tortuga_1.caminar_superficie()
# tortuga_1.entrar_agua()
print()
# pinguino_1.salir_superficie()

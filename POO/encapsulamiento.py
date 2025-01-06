"""Encapsulamiento de Clases"""
# Encapsulamiento se refiere a el concepto de ocultar los detalles internos de un objeto y
# exponer solo una interfaz para interactuar con él.
# Se logra mediante el uso de modificadores de acceso (público, privado y protegido) para los atributos y métodos de una clase.


class Auto:
    """Atributos de un Automovil"""

    def __init__(self, marca, anio, modelo, estado):
        # Para indicar que una variable o metodo es de tipo PRIVATE se asigna al inicio de la variable o metodo un _
        self._marca = marca
        self.__anio = anio
        self.__modelo = modelo
        self.estado = estado

    def __str__(self) -> str:
        return f"{self.getMarca} {self.get_modelo} {self.get_anio}"

    # Los denominados getters and setters se basa principalmente de la siguiente forma.
    """Getters and Setters de Anio"""
    @property
    def get_anio(self):
        return self.__anio

    @get_anio.setter
    def set_anio(self, nuevo_dato):
        self.__anio = nuevo_dato

    """Getters and Setters de Modelo"""
    @property
    def get_modelo(self):
        return self.__modelo

    @get_modelo.setter
    def set_modelo(self, nuevo_dato):
        self.__modelo = nuevo_dato

    # Para acceder a una variable de tipo privado se acccede mediante propiedades
    @property
    def getMarca(self):
        return self._marca

    # Para modificar una variable de tipo privado se utiliza el @variable.setter
    @getMarca.setter
    def setMarca(self, nueva_marca):
        self._marca = nueva_marca


"""MANIPULACION DE VARIABLES"""

# creamos un objeto de tipo Auto
mi_auto = Auto("Chevrolet", 2010, "Aveo Emotion Full GLS", "Apagado")
mi_auto_2 = Auto("Citroen", 2018, "C-Elyssee", "Apagado")

# print(mi_auto.getMarca)
# print(mi_auto.getMarca, mi_auto.get_anio, mi_auto.get_modelo)
# print(mi_auto_2.getMarca, mi_auto_2.get_anio, mi_auto_2.get_modelo)

# Almacenamos en una lista de objetos cada auto creado
mis_autos = [mi_auto, mi_auto_2]

# Aunque a pesar de que sus atributos son de tipo privado y protegido, no se puede acceder directamente a ellos
# ya que como vemos, en la terminal nos estaria manifestando la p

print(mis_autos)

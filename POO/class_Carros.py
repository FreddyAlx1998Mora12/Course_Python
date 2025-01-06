"""Clase que abarca la estructura basica y sencilla de un carro"""


class Car:
    """Clase que describe caracteristicas de un vehiculo"""

    def __init__(self, marca, modelo, year):
        """Define los atributos y caracteristicas"""
        self.marca = marca
        self.modelo = modelo
        self.anio = year
        self.kilometraje = 0

    def __str__(self):
        """Funcion que presenta datos de la clase Car y retorna un formato limpio"""
        datos_carro = f"{self.marca} - {self.modelo} - {self.anio} - {self.kilometraje} km"
        return datos_carro.title()

    def leer_kilometraje(self):
        """Funcion que da lectura al kilometraje del vehiculo"""
        print(f"El carro cuenta con un recorrido de {self.kilometraje} km")

    def actualizar_kilometraje(self, km):
        if km >= self.kilometraje:
            self.kilometraje = km
        else:
            print("No se puede retroceder los kilometros")

    def mover_vehiculo(self, km):
        """Funcion que simula el movimiento del vehiculo y incrementa los km"""
        self.kilometraje += km


class Bateria:
    def __init__(self, tamanio_bateria=120):
        self.bateria = tamanio_bateria

    def describir_bateria(self):
        print(f"Este vehiculo electrico tiene una capacidad de bateria de {self.bateria}-kWh")


class ElectricCar(Car):
    """Clase que representa los aspectos propio de un CARRO electrico
    Hereda caracteristicas de un vehiculo comun."""

    def __init__(self, marca, modelo, year):
        # Instancia la clase padre
        # Inicializa desde la clase Padre
        super().__init__(marca, modelo, year)
        # Atributos unicamente propios de ElectricCar
        # self.bateria = tamanio_bateria
        self.bateria_vehiculo = Bateria()

    def actualizar_bateria(self):
        # Actualiza la bateria del vehiculo electrico que por cada 3 km se reduce el nivel de bateria
        if self.kilometraje % 3 == 0:
            self.bateria_vehiculo.bateria -= self.kilometraje // 3
            print('Justo ahora se reduce 1 kWh')
        else:
            self.bateria_vehiculo.bateria -= self.kilometraje // 3
            print('Aun no se reduce su proximo nivel de bateria')


# Creando objetos Car
mi_carro = Car('opel', 'sorca', 2012)

# Presentar la variable creada
# Debemos recordar que mi_carro.__str__() devuelve un string
print(mi_carro.__str__())

mi_carro.leer_kilometraje()
mi_carro.mover_vehiculo(3)
mi_carro.leer_kilometraje()
mi_carro.actualizar_kilometraje(4)
mi_carro.leer_kilometraje()

# Creando objeto Carro Electrico
mi_carro_electrico = ElectricCar('tesla', 'sxt', 2020)

print(mi_carro_electrico.__str__())

# Accede a los metodos de la clase superior Padre
mi_carro_electrico.leer_kilometraje()
mi_carro_electrico.bateria_vehiculo.describir_bateria()
mi_carro_electrico.actualizar_kilometraje(7)
mi_carro_electrico.leer_kilometraje()
mi_carro_electrico.actualizar_bateria()
mi_carro_electrico.bateria_vehiculo.describir_bateria()
mi_carro_electrico.mover_vehiculo(9)
mi_carro_electrico.leer_kilometraje()
mi_carro_electrico.actualizar_bateria()
mi_carro_electrico.bateria_vehiculo.describir_bateria()

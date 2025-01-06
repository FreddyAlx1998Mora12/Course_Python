"""Clases, otro tipo de clases que se va a realizar"""


class Perro:
    """Clase que representa un Perro con nombre, edad y numero de vacunas"""

    # Inicializa los atributos
    def __init__(self, nombre, edad, raza, numero_vacunas=0):
        self.nombre = nombre
        self.raza = raza
        self.edad = int(edad)
        # Atributo o valor predeterminado
        self.numero_vacunas = numero_vacunas

    def __str__(self):
        """Impresion de los nombres y edad de mascota"""
        return (f"Nombre: {self.nombre},\n "
                f"Edad: {self.edad},\n "
                f"Raza: {self.raza},\n "
                f"Dosis de vacunas {self.numero_vacunas}\n")

    def saludar(self):
        print(f"El can llamado {self.nombre.upper()} "
              f"tiene edad: {self.edad}, esta saludando..")

    def sentarse(self):
        print(f"El can {self.nombre.capitalize()} esta sentado...")

    def actualizarNumeroVacunas(self, nuevo_dosis_vacuna):
        self.numero_vacunas = nuevo_dosis_vacuna


# Herencia
class Chihuahua(Perro):
    """Herencia de la clase Perro"""

    def __init__(self, nombre, edad, numero_vacunas, tamanio_mascota):
        """Instancia las variables de la clase base, ademas de un dato diferente, el tamanio"""
        # Lo que hace super, es que esas incializaciones las incializa desde la clase superior
        super().__init__(nombre, edad,'Chihuahua', numero_vacunas)
        self.tamanio = tamanio_mascota
        # Instancias como Atributos
        self.alimentacion = Comida(tipo_comida='Balanceado Especializado', peso='103 kg')

    def mostrar_tamanio(self):
        print(f'el tamanio es {self.tamanio}')


class Comida:
    """CLase que describe atributos de una alimentacion especializada"""

    def __init__(self, peso, tipo_comida):
        self.peso = peso
        self.tipo_comida = tipo_comida

    def describir_comida(self):
        return f"Cantidad: {self.peso}, Tipo Balanceado: {self.tipo_comida}"


# Instancias
mi_mascota_1 = Perro("Polo", 5, 'Labrador')
mi_mascota_2 = Perro('Kiro', 10, 'Labrador', 1)

# Instancia de la clase derivada de Perro, o clase hija
mascota_pequenia = Chihuahua('loqui', 2, 2, 187)

# Accede al metodo de la subclase
mascota_pequenia.mostrar_tamanio()

# Imprimiremos el tipo de dato o variable que es la variable alimentacion
# Evidentemente es una instancia de una clase, de la clase COMIDA(arg1, arg2)
print(type(mascota_pequenia.alimentacion), 'Tipo de dato Alimentacion')

# Acceder a variables de la instancia Comida()
mascota_pequenia.alimentacion.peso = '204 kg'
mascota_pequenia.alimentacion.tipo_comida = 'ProCan'

print(mascota_pequenia.alimentacion.describir_comida())

# Accede a los metodos de la clase superior o clase padre
mascota_pequenia.sentarse()
# print(mascota_pequenia.__str__())

# Acceder a los atributos se accede con un objeto.atributo
nombre_mascota = mi_mascota_1.__str__()
print(nombre_mascota)

# Acceder a los metodos
mi_mascota_1.saludar()
mi_mascota_2.saludar()

mi_mascota_1.sentarse()
mi_mascota_2.sentarse()

tu_mascota = Perro("Kira", 3, 'runita')
tu_mascota.saludar()
tu_mascota.sentarse()

# Para modificar algun valor directamente
mi_mascota_2.edad = 8
mi_mascota_1.numero_vacunas = 2
print(mi_mascota_1.__str__())
# mi_mascota_2.saludar()

# Para modificar directamente por metodo
tu_mascota.actualizarNumeroVacunas(5)

print(mi_mascota_1.__str__())
print(mi_mascota_2.__str__())
print(mascota_pequenia.__str__())
print(tu_mascota.__str__())

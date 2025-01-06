"""Clases -> Una clase en el paradigma POO, representa a un modelo estructurado de una entidad o objeto que tiene atributos y propiedades
del mundo real, y a su vez que se los pueden relacionar con una u otras caracteristicas similares, siempre y cuando esto se maneja mediante
un modelo de Clase...."""

# Por Ejemplo podemos decir que una persona, un animal o objeto pueden representarse como una clase...


class Persona:
    """Clase Persona que posee atributos, y propiedades."""
    # Definimos las variables o atributos de la Clase Persona
    def __init__(self, nombre, apellido, dni, sexo, 
                 estado_civil, edad, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
    
    # Una Persona tiene sus funciones o las funciones que pueden realizar en un entorno
    def saludar(self):
        return (f"Hola {self.nombre.title()}, como estas?")
    
    def calcular_edad(self):
        """Funcion para Calcular la edad actual"""
        anio_actual = 2023 - self.fecha_nacimiento
        return anio_actual, "Su edad actual"
    

# Crear un Objeto de la Clase Persona
persona_1 = Persona("freddy", "Matailo Mora", 123456789,
                    'M', "Soltero", 00, 1998)

"""Manipulacion de la Clase Persona"""
# Imprime el objeto persona en formato de diccionario, sintaxis similar a JSON.
print(persona_1.__dict__)

# Uso de la funcion Saludar declarada en la Clase Persona
nombre_persona = str(persona_1.nombre)

saludo = persona_1.saludar()
print(saludo, "-> Es un Saludo despues de entrar a la funcion")

# Uso de la funcion para calcular la edad que tiene como 
# parametro el anio de nacimiento
edad_actual = persona_1.calcular_edad()

print(edad_actual, "-> Edad Actual")

# Manipula los atributos de la clase persona
persona_1.edad = edad_actual[0]
# la razon por lo de edad actual [0] por que en esa variable se almacena una 
# variable de tipo tupla (25, 'su edad actual')

print()
print(persona_1.__dict__)

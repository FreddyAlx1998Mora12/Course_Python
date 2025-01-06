"""Ejercicio Practico que involucra una persona, o caso de la vida real"""


class Persona:
    """Describe a una persona con datos sencillos"""
    def __init__(self, **kwargs):
        # Dentro de la variable kwargs(evidentemente es un dict)
        # Encuentre la clave 'nombre', si encontro, asigna el value
        # Sino, asignale INKNOW
        self.nombre = kwargs.get('nombre', 'UNKNOW')
        self.apellido = kwargs.get('apellido', 'UNKNOW')
        self.edad = kwargs.get('edad', 0)

    def __str__(self):
        dato_persona = f'{self.nombre} {self.apellido} {self.edad}'
        return dato_persona.title()

    def saludar(self):
        mensaje = f'Hola, mis datos completos son: {self.__str__()}'
        print(mensaje)


class Usuario(Persona):
    """Describe a un usuario"""
    def __init__(self, username, password, **kwargs):
        # Pasa el diccionario a la clase padre y busca cada uno de las claves
        super().__init__(**kwargs)
        self.user = username
        self.password = password
        self.role = Admin()
        self.intentos_inicio_sesion = 0

    def descripcion(self):
        print('Nombre Persona:', self.nombre.title(), 'Usuario:', self.user)

    def incrementar_iniciar_sesion(self):
        if self.intentos_inicio_sesion < 3:
            self.intentos_inicio_sesion += 1
            print('Inicio de sesion nro', self.intentos_inicio_sesion)
        else:
            self.intentos_inicio_sesion = 3
            print('Ha superado los intentos de inicio de sesion')

    def reestablecer_iniciosesion(self):
        self.intentos_inicio_sesion = 0
        print('Se reestablecio los intentos de iniciar sesion, intentos actuales:', self.intentos_inicio_sesion)


class Admin:
    def __init__(self):
        self.rol = 'admin'
        self.privilegios = ['create', 'read',
                            'update', 'delete']

    def mostrar_rol(self):
        print('Rol:', self.rol)

    def mostrar_privilegios(self):
        print('Los privilegios son:')
        for privilegio, numero in zip(self.privilegios, range(len(self.privilegios))):
            print(f'{numero+1}.- {privilegio}')


persona1 = Persona(nombre='gloria', apellido='delgado', edad=35)
persona1.saludar()

usuario1 = Usuario('gloriauser', '12345',
                   nombre=persona1.nombre,
                   apellido=persona1.apellido,
                   edad=persona1.edad)

usuario1.descripcion()
usuario1.incrementar_iniciar_sesion()
usuario1.incrementar_iniciar_sesion()
usuario1.incrementar_iniciar_sesion()
usuario1.incrementar_iniciar_sesion()
usuario1.incrementar_iniciar_sesion()
usuario1.reestablecer_iniciosesion()

usuario1.role.mostrar_rol()
usuario1.role.mostrar_privilegios()

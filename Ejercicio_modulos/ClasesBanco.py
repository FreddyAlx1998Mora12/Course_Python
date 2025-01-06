"""
Ejercicio de banca virtual a nivel de consola.
Persona y banca o Cuenta
Practica POO y Refactorizacion
"""


class Persona:
    """Clase que describe atributos de una persona"""

    def __init__(self, nombre, apellido, domicilio, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.domicilio = domicilio
        self.sexo = sexo

    # Obtiene los datos de la Persona
    def getDatosCompletos(self):
        datos = (f'Nombres Completos: {self.nombre} {self.apellido}, '
                 f'\nDireccion: {self.domicilio}'
                 f'\nGenero: {self.sexo}')
        return datos.title()


class Banco:
    """Clase que describe atributos de una banca"""

    # Inicializa atributos de un banco
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.listaClientes = []

    # Obtiene un numero de clientes a partir de una lista de clientes que tienen cuenta
    def obtenernumerodeClientes(self):
        return len(self.listaClientes)

    def anadirCliente(self, cuenta_cliente):
        # Almacena objetos de tipo Cuenta que pertence a un cliente
        if cuenta_cliente.banco.nombre == self.nombre:
            if cuenta_cliente not in self.listaClientes:
                self.listaClientes.append(cuenta_cliente)
            else:
                print('Ya eres parte del banco..')
        else:
            print('No perteneces a este banco...')

    # Obtiene la sumatoria de los ingresos de los clientes
    def obtenerCapitalTotal(self):
        capital = 0
        for cuenta_cliente in self.listaClientes:
            capital += cuenta_cliente.saldo
        return capital


class Cuenta:
    """Clase que describe atributos de una cuenta de un Banco"""

    # Instancia atributos de un numero de cuenta
    def __init__(self, dni, persona, banco, saldo=0, tipo_cuenta='Ahorros'):
        self.dni = dni
        self.persona = persona
        self.banco = banco
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
        self.ingresos = []
        self.egresos = []

    def mostrarDatsCuenta(self):
        return (f'Cuenta Bancaria: {self.dni} \n{self.persona.getDatosCompletos()}'
                f'\nBanco: {self.banco.nombre}')

    def depositar(self, monto):
        self.ingresos.append(monto)
        self.saldo += monto

    def retirar(self, monto):
        # Verificar que el monto no sea mayor al saldo actual
        if monto < self.saldo:
            self.egresos.append(monto)
            self.saldo -= monto
        else:
            print('Saldo insuficiente..')

    def mostrarSaldo(self):
        # Muestra el saldo total que tiene, solo dinero depositado
        return self.saldo

    def mostrarEgreso(self):
        # Muestra el movimiento de los ingresos
        return self.egresos

    def mostrarIngresos(self):
        return self.ingresos




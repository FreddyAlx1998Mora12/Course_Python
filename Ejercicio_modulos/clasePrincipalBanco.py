# FROM (desde) import clases interna
from ClasesBanco import Persona as P
from ClasesBanco import Cuenta as c
from ClasesBanco import Banco as b

# Instanciamos personas
persona = P("chris", "evans", "Guayaquil", "M")
persona1 = P("Carlos", "Pérez", "Av. Siempre Viva 123, Quito", "M")
persona2 = P("Ana", "Gómez", "Calle Luna, Guayaquil", "F")
persona3 = P("Luis", "Martínez", "Calle del Sol, Cuenca", "M")
persona4 = P("María", "Fernández", "Av. del Río 456, Loja", "F")
persona5 = P("Jorge", "Ramírez", "Callejón del Gato 789, Manta", "M")

# Instanciamos Bancos
banco = b('Banco de Loja', 'Loja')
banco_2 = b('Banco de Guayaquil', 'Guayaquil')
banco_3 = b('Banco Pichincha', 'Pichincha')

# Creamos cuentas para cada banco
cuenta_bancaria = c(1111111111, persona, banco)
cuenta_bancaria1 = c(6666666666, persona1, banco)
cuenta_bancaria2 = c(2222222222, persona2, banco_2)
cuenta_bancaria3 = c(3333333333, persona3, banco_2)
cuenta_bancaria4 = c(4444444444, persona4, banco_3)
cuenta_bancaria5 = c(5555555555, persona5, banco)

# print(persona.getDatosCompletos())
print(cuenta_bancaria.mostrarDatsCuenta())
print('-----'*10)
print(cuenta_bancaria1.mostrarDatsCuenta())
print('-----'*10)
print(cuenta_bancaria2.mostrarDatsCuenta())
print('-----'*10)
print(cuenta_bancaria3.mostrarDatsCuenta())
print('-----'*10)
print(cuenta_bancaria4.mostrarDatsCuenta())
print('-----'*10)
print(cuenta_bancaria5.mostrarDatsCuenta())
print('-----'*10)

# Anadiremos los clientes a su respectivo banco
banco.anadirCliente(cuenta_bancaria)
banco.anadirCliente(cuenta_bancaria1)
banco.anadirCliente(cuenta_bancaria5)
banco_2.anadirCliente(cuenta_bancaria2)
banco_2.anadirCliente(cuenta_bancaria3)
banco_3.anadirCliente(cuenta_bancaria4)

# Simularemos que realizaremos solo depositos en un banc
cuenta_bancaria1.depositar(10)
cuenta_bancaria1.depositar(350)
cuenta_bancaria1.depositar(50)

cuenta_bancaria2.depositar(100)
cuenta_bancaria2.depositar(290)
cuenta_bancaria2.depositar(500)

cuenta_bancaria3.depositar(1025)
cuenta_bancaria3.depositar(48)
cuenta_bancaria3.depositar(25)

cuenta_bancaria.depositar(10)
cuenta_bancaria.depositar(35)
cuenta_bancaria.depositar(50)

cuenta_bancaria4.depositar(134)
cuenta_bancaria4.depositar(90)
cuenta_bancaria4.depositar(20)

cuenta_bancaria5.depositar(380)
cuenta_bancaria5.depositar(210)
cuenta_bancaria5.depositar(15)

# Simularemos que retiraremos dinero
cuenta_bancaria.retirar(10)
cuenta_bancaria.depositar(505)
cuenta_bancaria.retirar(50)
cuenta_bancaria.retirar(210)

cuenta_bancaria1.retirar(190)
cuenta_bancaria1.retirar(10)

cuenta_bancaria2.retirar(250)
cuenta_bancaria2.retirar(50)

cuenta_bancaria3.retirar(100)

cuenta_bancaria4.retirar(200)

cuenta_bancaria5.retirar(90)
cuenta_bancaria5.depositar(30)

print('Numero de Clientes:', banco.obtenernumerodeClientes(),
      ',Banco:', banco.nombre, ',Capital:', banco.obtenerCapitalTotal())
print('Numero de Clientes:', banco_2.obtenernumerodeClientes(),
      ',Banco:', banco_2.nombre, ',Capital:', banco_2.obtenerCapitalTotal())
print('Numero de Clientes:', banco_3.obtenernumerodeClientes(),
      ',Banco:', banco_3.nombre, ',Capital:', banco_3.obtenerCapitalTotal())

print('-----'*10,'\nCuenta Cliente....')
# Mostraremos los movimientos o saldo actual de cada cuenta
print(cuenta_bancaria.mostrarDatsCuenta())
print('Saldo Disponible:', cuenta_bancaria.mostrarSaldo())
print('Movimientos Ingresados:', cuenta_bancaria.mostrarIngresos())
print('Movimientos Egresados:', cuenta_bancaria.mostrarEgreso())
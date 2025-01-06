"""
    Esta clase, se enfoca en la importacion de modulos, asi como el uso de diferentes modulos de clase
    Este modulo principal, siimulara una concensionaria de vehiculos
"""
import concensionaria as c

# Muestra al usuario las marcas de vehiculos disponibles
c.mostrar_marca_vehiculos()
# Pide al usuario seleccionar la marca interesada
dato_usuario = c.entrada_usuario('Si desea ver los modelos... seleccione o ingrese el numero: ')
# Muestra los modelos
c.mostrar_marca_modelos(dato_usuario)
dato_usuario = c.entrada_usuario('\nSeleccione el modelo a alquilar: ')
c.seleccionar_vehiculo(dato_usuario)
# print(vehiculos.modelos)



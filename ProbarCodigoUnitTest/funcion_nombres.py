"""Clase para realizar la prueba de codigo"""

# Hare uso de una funcion que hice en inicios
# from funciones import ingresar_nombre # No me resulto como esperaba

print('Pruebas de funciones Testing')
nombre, apellido = '', ''


def formatearNombres(nombres, apellidos):
    return f'{nombres.capitalize()} {apellidos.capitalize()}'


# while True:
#     if not nombre:
#         nombre = input('Ingrese el nombre: ')
#
#     if not apellido:
#         apellido = input('Ingrese el apellido: ')
#
#     if 'q' in nombre.lower() or 'q' in apellido.lower():
#         break
#
#     datos_formateados = formatearNombres(nombre, apellido)
#     print(datos_formateados)
#     # Limpia
#     nombre, apellido = '', ''

print('Pruebas finalizadas de la funcion nombres')

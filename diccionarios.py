"""Diccionarios"""
# Sabemos que los diccionarios llevan una clave : valor
# Dentro de un diccionario se puede almacenar sinnumeros de variables
# Sean arryas, diccionarios, tuplas, dato : valor
# Su sintaxis es simple, sabemos que los diccionarios son elementos iterables
# La sintaxis se basa en {} como si fuese un formato tipo JSON, y para acceder
# a algun elemento se lo hace mediante variable_dicc[clave]

# Imaginemos los datos de una persona almacenado en una variable
persona_dict = {'nombres': 'Joaquin Snyder',
                'apellidos': 'Benavidez Perez',
                'edad': 25,
                'direccion_domicilio': 'Olmedo',
                'pais': 'Ecuador',
                'estado cuenta': [100, 200, 253, 500],
                'telefonos': ('a','sd', 5932222131, 7389123)}

# Si deseamos imprimir un dato en concreto accedemos por medio de la clave
print(f"Dato Nombres de la persona {persona_dict['nombres'].upper()}, Apellidos: {persona_dict['apellidos'].upper()}")
print('Estado de Cuenta de la Persona', persona_dict['estado cuenta'])

# Tipo de dato clave: valor almacenado en clave estado cuenta y cada dato
print(type(persona_dict['estado cuenta']))
print(type(persona_dict['nombres']), type(persona_dict['edad']), type(persona_dict['telefonos']))

# Si deseamos que nos traiga un dato que puede, como no puede existir
# diccionario.get('clave', 'mensaje si no encontro dato clave')
estado_civil = persona_dict.get('estado_civil', 'No existe una clave de estado civil registrado..!')
print(estado_civil)

# Los diccionarios al igual que las listas tambien tienen su dinamismo
# Modificacion
print(f"El valor a modificar es direccion de domicilio, antes = {persona_dict['direccion_domicilio']}")
persona_dict['direccion_domicilio'] = 'Olmedo Piedra redond modified'
print('Ahora el valor modificado es, ',persona_dict['direccion_domicilio'])

# Creacion de una clave : valor
persona_dict['estado_civil'] = 'Casado'

# print(persona_dict)

# Eliminacion de un dato clave : valor, al igual que un array
del persona_dict['telefonos']

# print(persona_dict)

# ---------Ejemplo Lenguajes de POO
favorite_languages = {
    'Hugo': 'Python',
    'Freddy': 'Java and Python',
    'Santiago': 'PhP',
    'Joel': 'C'
}

# Aniadiremos un diccionario en otro diccionario
persona_dict['lenguaje_amigos'] = favorite_languages

# Desearia ver el lenguaje favorito de Hugo
language_hugo = favorite_languages['Hugo']

print('Lenguaje de programacion favorito de Hugo es',language_hugo)

# Iterar en bucle los diccionarios, itera cada ITEMS
# Para saber datos key:value iterar con ITEMS
print('\nLa clave : valor de cada item es...')
for clave,valor in persona_dict.items():
    print(f'{clave} = {valor}')
    # Itera un subdiccionario denominado lenguaje_amigos
    for k,v in persona_dict['lenguaje_amigos'].items():
        print(f'{k} = {v}')

# Para saber solo datos claves o keys, iterar con .keys
print('\nSolo ver datos key o datos clave que contiene el dict persona ')
for dato_clave in persona_dict.keys():
    print(f'- {dato_clave}')

# Trabajar con keys facilidad la busqueda y verificacion de datos externos
if 'Juan' not in persona_dict['lenguaje_amigos'].keys():
    print('Juan, no estas en esta lista, lo siento..!')

# Se puede saber datos valores o values, iterar con .values
print('\nSolo ver datos value o datos valor que contiene el dict persona ')
for dato_valor in persona_dict.values():
    print(f'- {dato_valor}')

# Para trabajar con datos repetidos

# Un dato tendra el mismo lenguaje
# Creando nuevos datos en el subdiccionario lenguaje_amigos
persona_dict['lenguaje_amigos']['Juan'] = 'Python'
persona_dict['lenguaje_amigos']['Diego'] = 'PhP'
persona_dict['lenguaje_amigos']['Daniel'] = 'PhP y Java'

print(persona_dict['lenguaje_amigos'])

# Ahora para evitar repeticion de los datos se utiliza un set
# Para esto se utilizara un 'conjunto'
# Un conjunto es una coleccion con datos unicos
print('\nConjunto de datos claves repetitivos en dict persona')
print('Los lenguajes elegidos por las personas ingresadas son')

# Con set, PYTHON identifica los elementos que se repiten y crea un conjunto con ellos
for lenguaje in set(persona_dict['lenguaje_amigos'].values()):
    print('-',lenguaje)

# Anidacion, se puede almacenar dentro de una lista, diccionarios
# Crearemos una flota de extraterrestres, una lista de aliens
aliens = []
for n_alien in range(5):
    n_alien = {'id': n_alien+1, 'color': 'blue', 'raza': 'marcian', 'origen': 'marte'}
    # Almacena cada n_alien creado, en list aliens
    aliens.append(n_alien)

# Ahora en aliens tenemos una LISTA que contiene DICCIONARIOS
print('Lista de aliens creados \n Cantidad de aliens', len(aliens),
      '\n Lista de aliens.. dict')

# Cada dato de la lista aliens que se itera presenta como un dato type dict
for alien in aliens:
    print(alien, type(alien))

print('Datos Modificados//////////////////')

# Si se desea modificar los 2 primeros aliens
for alien in aliens[:2]:
    # Axioma, Bloque para modificar
    # SI el dato value del dato key/color/ es blue
    if alien['color'] == 'blue':
        # Modifica valores
        alien['color'] = 'green'
        alien['raza'] = 'hight sky'
    # otra manera de comparar un valor es
    if 'marte' in alien.values():
        alien['origen'] = 'jupiter'
for alien in aliens:
    print(alien, type(alien))

# Para iterar un DICCIONARIO en un DICCIONARIO
# Haremos por ejemplo un diccionario de usuarios registrados
usuarios_registrados = {
    'diego_mat': {
        'nombre': 'diego josue',
        'apellidos': 'matailo mora',
        'edad': 22,
        'deportistas_favorits': {
            'futbol': ('CR7', 'Ronaldinho', 'Neymar', 'Messi'),
            'rally': ['Guerrero', 'Navas', 'Rojas']
        }
    },
    'frealx_mat': {
        'nombre': 'freddy alexander',
        'apellidos': 'matailo mora',
        'edad': 25,
        'deportistas_favorits': {
            'futbol': ('CR7', 'Ronaldinh', 'Messi'),
            'rally': ['Quirola', 'Cuenca', 'Rojas'],
            'basketball': ['Kobe Brynt', 'Michael Jordan', 'J Murphy']
        }
    }
}

print('\n'*2,'DICCIONARIO DENTRO DE UN DICCIONARIO\n')

# Iterar y imprimir los items que conforma un diccionario
for usuario, info_usuario in usuarios_registrados.items():
    # print(usuario, info_usuario)
    print(f"Usuario: {usuario},"
          f"\n\tDatos;"
          f"\n\t\tNombres completos: {info_usuario['nombre'].title()} {info_usuario['apellidos'].title()},\n\t\t"
          f"edad: {info_usuario['edad']},\n\t"
          f"Sus deportistas favoritas son:")
    # Ahora iteraremos otro subdiccionario del subdiccionario
    # info_usuario['deportistas_favorits'] es un diccionario
    for deporte, deportistas in info_usuario['deportistas_favorits'].items():
        print(f'\t\tDeporte: {deporte.upper()},\n\t\t\tDeportistas:')
        # deportistas son coleccion de datos lista y tupls
        for deportista in deportistas:
            print('\t '*3, '-', deportista)



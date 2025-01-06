"""
JSON -> Javascript Object Notation, en espaniol Objetos de Notacion Javascript
Son formatos para mostrar informacion de modo que Javascript pueda interpretar,
modelar, y mostrar dicha informacion, es como un lenguaje comun a nivel de
LENGUAJES, comunmente JSON es similar a un dict en Python.
Dicho de otra forma, JSON es una estructura de datos.
"""
# Json.dump -> convierte desde Python a un archivo JSON
# json.loads -> parse un formato json a un tipo de dato dict, array

import json

# Variable tipo formato json -> str
x_json = '{"nombre": "Vinicio", "edad": "95", "sexo": "Masculino", "direccion": "Loja-Ecuador"}'

# Convertir a un formato python
dato_dict = json.loads(x_json)

# Mostramos al usuario
for key, value in dato_dict.items():
    print(key,':', value)

print(type(dato_dict), type(x_json))

# ----------------- JSON.DUMPS -----------------
# json.dumps(arg1, arg2)
# arg1 dato oargumento que se quiere almacenar,
# arg2 donde el dato se va a almacenar.

# lista de numeros
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# archivo que se creara y se almacenara
archivo = 'files_txt/numeros.json'

# abre si exite, crea si no exite el archivo
with open(archivo, 'w') as file_object:
    # lista y datos_dict son objetos de datos iterables
    # file object es el dato o archivo que alojara los objetos
    # json.dump(lista, file_object)
    json.dump(dato_dict, file_object)

# Ahora para leer lo que contiene o intentar parsear un archivo.json a python
# Recordemos que
with open(archivo) as file_object_json:
    datos = json.load(file_object_json)

print(type(datos), datos)

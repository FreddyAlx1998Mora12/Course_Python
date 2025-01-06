"""
Clase que se demostrara como funciona el manejo de excepciones o errores
"""

# Para el manejo de errores o excepciones se utiliza el sgt bloq
# try ..... except ERROR: .....

ruta_archivo = 'files_txt/libroEjemplo.txt'
libro = ''
# Rastrear el tipo de error que puede lanzar Python
try:
    a = 5
    b = 3
    print(a / b)

    with open(ruta_archivo, encoding='utf-8') as file_object:
        libro = file_object.read()

except ZeroDivisionError as e:
    print(type(e), 'No se puede dividir para 0.')

except TypeError as e:
    # TypeError es un error de tipo de dato
    print(type(e), 'Existio un tipo de error de tipo de dato.\nNo puede dividirse entre un entero y un caracter')

except FileNotFoundError as e:
    print('El archivo que deseas buscar, no se encontro')

else:
    # Bloque que hace algo cuando se ha comprobado con exito el try
    print('Se ejecuta este codigo cuando no hay errores...')
    palabras = libro.split()
    print(libro[:150], 'Nro de palabras', len(palabras))

finally:
    print('Ejecuta este codigo, finalmente, independientemente de si hubo o no errores')
    print('Numero de palabras bloque finally', len(palabras))

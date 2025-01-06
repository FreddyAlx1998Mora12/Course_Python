nombre_cadena = "Este es el comienzo..."
descripcion_cadena = """
En la consola, se va a visulizar tal cual como lo estoy detallando, 
me parece interesante esto, debo de conocer muchas cosas sobre esto....
ANIMOOOS...
"""

print(nombre_cadena,descripcion_cadena)

descripcion_len = """A CONTINUACION VAS A VER UNA DE LAS 
TANTAS FUNCIONES DE PYTHON EN STRINGS, LONGITUD DE LA CADENA...."""

#print(descripcion_len,len(descripcion_cadena))

descripcion_cadena_primeraletra = """\nEsta funcion permite sacar la primera letra o n letra
a partir de tomar la variable como una lista, es decir, podemos ingresar a un valor
por los [] o a su vez [:]"""

print(descripcion_cadena_primeraletra,descripcion_cadena[:5])

formatear_string = """Es casi similar a la sintaxis de java para concatenar, y en tiene
caracteristicas similares a las que usabamos para el front en angular utilizando {} o + de concatenacion ---> """

nombre = "Freddy"
apellido = "Matailo"

print(formatear_string, f"{nombre[:3]} {apellido}")

# Tambien se utilizan metodos y funciones como .strip() para eliminar espacios
# replace() -> que sirve para reemplazar una cadena de caracteres de la secuencia por el nuevo arg..
# find() -> que encuentra tal cadena de caracteres en una secuencia,
# devuelve el indice en donde se encuentra....
# upper()
# lower()
# lstrip() -> elimina espacios de la izquierda
# rstrip() -> al igual que el anterior pero a la derecha
# capitalize() -> toma la primera letra o indice de la secuencia de caracteres en mayuscuka
# title() -> Convierte la cadena de caracteres a formato titulo..
# "" in variable - > al igual que find devuelve un boolean

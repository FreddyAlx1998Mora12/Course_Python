""""Tuplas """
# Sabemos que las tuplas son tambien una coleccion de datos, a dieferencia
# de las listas, las tuplas son colecciones inmutables, es decir,
# valores que no se pueden cambiar, Python a esto conoce como Lista inmutables
# Su sintaxis, es similar a un array, solo cambia el [] por ()

# Dimensiones de un cuadrdado o un espacio en especifico
dimensiones = (220, 35)

print(type(dimensiones))
# Imprime que la variable dimensiones es un variable tipo tuple
# Python entiende que es una tupla por que la informacion se almacena dentro de un ()

print("Tupla 1:", dimensiones)

# Iterar como un array
for dimension in dimensiones:
    print(dimension)

# Modificar como un array, y ojo al error que me saldra
# dimensiones[0] = 354
# print(dimensiones)
# TypeError: 'tuple' object does not support item assignment

# Si se desea modificar, se deberia sobreescribir la tupla o la misma variable
dimensiones = (450, 135)
print("Tupla 2:", dimensiones)

# Por ejemplo un menu o bufe de comida
menu_desayuno = ("cafe", "batidos", "sandwichs", "tigrillo", "bolones", "humitas", "tamales")
print("----- Menu del dia -----")
for elemento in menu_desayuno:
    print("- ", elemento.title())


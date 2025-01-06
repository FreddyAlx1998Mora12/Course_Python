import math

# Sabemos la sintaxis de una lista en python debe seguirse asi
# nombre_variable = [dato, dato]
# la palabra dato, son diversos tipos de datos,
# ya sean char '', cadenas "", entero nro, listas[], etc..
# ---------------------
# Dinamismo = se le llama dinamismo por la forma de interaccion con cada dato
# dentro de una lista, es decir, se puede, insertar, eliminar, modificar, etc


# ----> Modificacion de una variable
marca_carros = ["chevrolet", "citroen", "audi", "BMW", "Volkswagen", "lexus"]

# Imprimiremos la cadena
print("Arreglo original:", marca_carros)

# Modificaremos la variable chevrolet por un PEUGEOT, ya sea conociendo el indice del arreglo
marca_carros[0] = "peugeot"
print("Lista modificada:", marca_carros)  #= imprimira la nueva

# Modificaremos el ultimo indice de la lista por JEEP
marca_carros[-1] = "jeep"
print("Lista modificado ultimo valor:", marca_carros)

# Modificaremos el indice que contenga el dato bmw por un volvo,
# para ello se debe encontrar el indice de la lista
# que contenga la palabra bmw por medio de index
indice_bmw = marca_carros.index("BMW")
marca_carros[indice_bmw] = "volvo"
print("Lista modificada, indice que contenga bmw:", marca_carros)

marca_carros.append('Mercedez')
# Modificaremos el valor del indice medio de la lista ya sea usando la operacion
# (len(marca_carros)+1)//2 aunque, hay que tomar en cuenta que
# la lista solo recorre indices decimales y no float

indice_medio = math.floor(len(marca_carros) / 2)
# math.floor, se utiliza para obtener un indice entero con redondeo inferior

print(f"Valor medio de {len(marca_carros)} // 2 = ", indice_medio)
marca_carros[indice_medio] = "tesla"
print("Lista modificada, valor medio", marca_carros)

# ----> Aniadir nuevos elementos
# Añadir elementos al inicio de la lista, sabiendo que
# logicamente el indice inicio de una lista es 0
# Para anadir en cualquier posicion, se debe especificar el indice donde se vaya a guardar y la lista se ira desplazando
marca_carros.insert(0, "Chevrolet")
marca_carros.insert(0, "BMW")
marca_carros.insert(0, "Lexus")
print("\nLista con nuevos elementos al inicio", marca_carros)

# Anade elementos al final
marca_carros.append("Skoda")
print("Lista con nuevos elementos al final", marca_carros)

# ----> Eliminar elementos
# Sabemos que para eliminar elementos nos referimos a 2 maneras, ya sea
# una eliminacion logica, o
# una eliminacion permanente de informacion....
# y lo mas mas facil es mediante la palabra del de delete

# elimina el dato que contenga el indice de la lista, puede eliminarce cualquier indice que se conozca o desea eliminar
print(f"Numero de elementos antes de eliminar un dato {len(marca_carros)}\nElemento indice 0 eliminado!!!..")
del marca_carros[0]
# Ojo, tambien se puede eliminar n elementos utilizando slice o trozo [:]
print("Lista modificada, elemento indice 0 eliminado", marca_carros)

# deseo eliminar el elemento chevrolet
indice_marca_chevrolet = marca_carros.index("Chevrolet")
del marca_carros[indice_marca_chevrolet]
print("Lista modificada, elemento Chevrolet eliminado", marca_carros)

# Ahora si deseo hacer una ELIMINACION LOGICA,
# es decir que no se ha borrado por completo, mas bien se oculta el elemento
# Para ello tenemos la funcionalidad del metodo POP(),
# lo que hace que al eliminar el elemento nos da la oportunidad de
# trabajar con el elemento eliminado, pop() elimina el ultimo elemento,
# y tambien se elimina un indice siempre y
# cuanndo se especifique un id por ejemplo

# Vamos a eliminar un elemento de la lista de marca de carros,
# y lo vamos a dar de baja o quitar de la lista
last_car_deleted = marca_carros.pop()
print(f"El elemento que se elimino de la lista es {last_car_deleted}\nAlmacen de marcas deleted..")
cars_deleted = [last_car_deleted]
# anadire un nuevo elemento eliminado, es decir, sacare el elemento
# que tenga el indice 2 de la lista, es decir, citroen
cars_deleted.append(marca_carros.pop(2))
print(cars_deleted)

print(f"Lista Actualizada!!\n{marca_carros}")
# Una manera similar a la anterior, podemos usar la palabra REMOVE,
# que elimina por COMPLETO un elemento, pero,
# podemos acceder al dato cuando lo sacamos en otra variable,
# y siempre y cuando se encuentra en la lista
marca_BMW = 'BMW'
marca_carros.remove(marca_BMW)
print(f"Se elimino el dato {marca_BMW} de la lista..!\nLista Actualizada!!\n{marca_carros}")

# OJO, remove elimina a la primera ocurrencia que aparece,
# si se desea eliminar un elemento que tenga elementos identicos
# se deberia usar un bucle para que se encargue de eliminar todos los elementos posibles

# ---> Ordenar o organizar elementos de una lista
# Ordenar elementos por el metodo sort(), pero cabe recalcar que
# el metodo sort ordena permanentemente la lista
# marca_carros.sort()
print(f"La lista ordenada con sort= {sorted(marca_carros)}")
print(marca_carros)

# Ordenar elementos con metodo sorted(), lo que ordena la lista temporalmente
marca_carros.reverse()
print(f"Lista ordenada en inversa: {marca_carros}")

# Partir una lista, es decir sacar un trozo de una lista
# solamente con especificar desde una posicion inicial, hasta la posicion final
# usando el slice

print(f"Lista partida desde la posicion 2 hasta el antepenultimo: {marca_carros[1:len(marca_carros) - 1]}")
print(f"Lista partida desde la posicion 4 al ultimo sin indice : {marca_carros[3:]}")
print(f"Lista partida de los ultimos 3 elementos con indice negativo: {marca_carros[-3:]}")
print(
    f"Lista partida de los ultimos 2 elementos antepenultims con indices negativos: {marca_carros[-3:len(marca_carros) - 1]}")

# Pasar un trozo de lista e iterar en un bucle, no es tan complejo,
# de hecho es lo mismo que pasar un array o iterar un array con bucle for,
# solo que la diferencia le pasamos que trozo desea iterar
# Iterare los ultimos 3 marcas de carros
for marca_carro in marca_carros[-3:]:
    print("Marca elegida:", marca_carro.title())

# Copiar una lista
# No es lo mismo lista1 = lista2, ya que ambas variables son por efecto la misma lista
# lo correcto para copiar una lista y que cada una almacene valores diferentes en base a una copia se realiza lo sgt
copia_marca_carros = marca_carros[:]

marca_carros.insert(0, "Mitsubishi")
copia_marca_carros.append("Skoda")

print(
    f"Copia de arrays...\nLista original con un elemento insertad {marca_carros}\nLista copia con elemento insertad {copia_marca_carros}")

# Ahora, que pasa si ponemos que copia_marca_carros = marca_carros
copia_marca_carros2 = marca_carros
copia_marca_carros2.insert(0, "MacLaren")
marca_carros.append("Lexus")

print("Listas cuando ponemos copia_marca_carros = marca_carros ", copia_marca_carros2, marca_carros)
# En efecto, en consola nos muestra que el mismo array o list
# pertenecen o son la misma para ambas variables, o viceversa,
# las variables copia_marca_carros2 y marca carros apuntan a la misma lista

# Ejercicio en la que consiste sacar los
# 3 primeros elementos de una lista,
# los 3 elementos medios de la lista, y
# 3 ultimos elementos de la lista

print(
    f"------Excersices Slices------\n"
    f"Lista {marca_carros}\n"
    f"3 primeros elementos de la lista: {marca_carros[:3]}\n"
    f"3 elementos medios: {marca_carros[(len(marca_carros) // 2) - 1:(len(marca_carros) // 2) + 2]}\n"
    f"3 ultimos elementos:{marca_carros[-3:]}")

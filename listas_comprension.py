# Estas listas son muy demasiado utiles diria a la hora de trabajar con POO.
# Consultee....
# Una lista de comprensión en Python es una forma concisa y eficiente de crear y manipular listas.
# Permite generar una nueva lista aplicando una expresión a cada elemento de una secuencia, como otra lista, una cadena de caracteres, una tupla, un rango, etc.
# Es una característica poderosa y ampliamente utilizada en Python debido a su legibilidad y capacidad para simplificar el código.
# Ya que esto nos permite extraer ciertos tipos de elementos por varieddad por ejemplo

# Lista de Usuarios
usuarios = ['Kerly', 'Freddy', 'Hugo',
            'Santiago', 'Cristhian',
            'Fer', 'Diego', 'Lilian',
            'Emily', 'Allison', 'Lu']

# Creo un nuevo objeto lista con numeros id
usuarios_enumerados = enumerate(usuarios, start=1)

for user in usuarios_enumerados:
    print(user, "Indice de la tuplas", user[0])

# Las listas comprension nos permite (read top)
# Su sintaxis

# nueva_lista = [expresión for elemento in secuencia o [] if condición]

# Donde

# expresión es el valor que se agregará a la nueva lista.
# elemento es una variable que representa cada elemento de la secuencia.
# secuencia es la secuencia de elementos de la cual se generarán los valores para la nueva lista.
# condición (opcional) es una expresión booleana que filtra los elementos que se incluirán en la nueva lista.

# Por ejemplo de la lista de usuarios, quiero filtar los usuarios que tengan el id par....
filtro_pares_usuarios = [(usuario[1], f"id = > {usuario[0]}")
                         for usuario in usuarios_enumerados if usuario[0] % 2 == 0]
# print(filtro_pares_usuarios)

# print()

# Filtrar usuarios cuya primera letra empiece con una vocal
vocales = ['a', 'e', 'i', 'o', 'u']
filtro_vocal_usuario = [
    usuario for usuario in usuarios_enumerados if usuario[0].lower() in vocales]

# print(filtro_vocal_usuario)

# Matriz
a = range(1, 10)
b = ['a', 'b']

matriz_ab = [
    str(array_a) + array_b for array_a in a for array_b in b]

print(matriz_ab)

# Para que la matriz me imprima de la siguiente forma
# | 1a , 2b |
# | 2a , 3b |

matriz2 = [a+'-'+b for a in matriz_ab for b in matriz_ab if a[0]
           < b[0] and a[1] != b[1]]


# print('matriz 2 =', matriz2[0::2])


# matriz3 = |['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a'] + ['2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b']|
# matriz3 = matriz_ab[0::2] + matriz_ab[3::2]
fil_a = matriz_ab[0::2]
# elimino el ultimo ya que para unir y hacer una matriz deben ser la misma cantidad de numeros
# fil_a.pop(-1)
fil_b = matriz_ab[1::2]
print("fila a =", fil_a)
print("fila b =", fil_b)


def funcion_ordenar(dato_a, dato_b):
    return (f"|{dato_a} , {dato_b}|")


matriz3 = map(funcion_ordenar, fil_a, fil_b)
# En matriz 3 se guarda un generador debido a que utilice una funcion map
# Los generadores solo se pueden utilizar una sola vez
matriz_r = list(matriz3)
print("matriz 3 = ", matriz_r)
# print('->', matriz_r)
for m3 in matriz_r:
    print(m3)

# De acuerdo al libro y siguiendo el ejemplo de la clase iterables-bucles, hare un ejemplo de lista de compresion
# Una lista de cuadrados o cubos
squares = [value**3 for value in range(1,11)] #La expresion a guardarse en squares es el value**n combinando con un for
# que va desde 1 hasta 11 -1.
print("Lista de cuadrados: ",squares)



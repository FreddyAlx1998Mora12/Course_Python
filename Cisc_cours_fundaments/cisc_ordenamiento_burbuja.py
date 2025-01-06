"""Ordenamiento de un array por metodo burbuja y por metodo recursivo"""

array_numeros = [2, 10, 5, 1, 8, 3, 14]


def burbuja(array):
    # Con este for es para recorrer todos los elementos
    for j in range(len(array)):
        # Con este for hace los recorridos y comparacion
        for i in range(len(array) - 1):
            # Compara con el siguiente elemento
            if array[i] > array[i + 1]:
                # Si es mayor, cambia
                array[i], array[i + 1] = array[i + 1], array[i]

    return array


def quick_sort(array):
    # No hay mas de 2 elementos
    if len(array) <= 1:
        return array

    # valor pivote, elemento del centro del array
    pivote = array[len(array) // 2]

    # Lista de numeros menores al numero pivote
    # List comprehension
    izq_menor = [x for x in array if x < pivote]
    # Lista de numeros meyores al numero pivote
    # List comprehension
    der_maior = [x for x in array if x > pivote]
    # List comprehension
    centro = [x for x in array if x == pivote]

    # regresa una union de los listas de numeros menores centro y derecho
    return (quick_sort(izq_menor) +
            quick_sort(centro) +
            quick_sort(der_maior))


print(array_numeros)
print(burbuja(array_numeros))
print('Ordenamiento Quick sort', end=' ')
print(quick_sort(array_numeros))

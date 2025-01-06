"""
Contador de palabras de multiplpes archivos, controlando excepciones
"""

# Archivos que estan en la misma carpeta o direccion raiz
archivos = ['archivo anexado.txt', 'archivo inexistente',
            'lista de invitados generados por EJERCICIO en Python.txt',
            'archivos de palabras.txt', 'archivo_escritura.txt']
archivos_inexistente = []


# funcion que cuenta el numero de palabras de un archivo
def contar_palabras(archivo):
    try:
        # Abre el archivo en modo lectura
        with open(archivo, 'r') as file_object:
            # ALmacena el contenido del archivo en una variable libro
            libro = file_object.read()

    except FileNotFoundError:
        print(f'No se encuentra el siguiente: {archivo}')
        archivos_inexistente.append(archivo)
    else:
        # Si encontro el archivo, haz lo siguiente
        # Divide los primeros 150 caracteres para contar letra por letra
        palabras = libro[:150].split()
        print(f'El archivo {archivo.__getattribute__('name')} tiene {len(palabras)} palabras.')


# Itera cada item de la lista de archivos
for archivo in archivos:
    contar_palabras(archivo)

print('Resultado de archivos que no existem o no fueron analizados: ', archivos_inexistente)

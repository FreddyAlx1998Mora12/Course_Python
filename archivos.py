
"""Clase para trabajar con lectura y modificacion de archivos y excepciones."""
ruta = 'files_txt/archivo prueba.txt'
with open(ruta) as archivo:
    # archivo.read() -> lee el archivo, lee informacion, lee bits,
    # lee todo el contenido
    # readline() -> lee una linea a la vez
    # readlines() -> lee todas las lineas y devuelve en un []
    contenido_archivo = archivo.read().rstrip()

print(contenido_archivo.rstrip())

# Lectura de linea por linea
# 'r' -> read, leectura
# 'w' -> write, escritura
# 'b' -> binary
# 'a' -> append
print('\nLectura de archivo, linea por linea.\n')
with open('files_txt/archivo prueba.txt', 'r') as archivo:
    for linea_linea in archivo:
        # tomar en cuenta que la lectura tambien lee la ultima linea
        print('-', linea_linea.rstrip())

print('\nAlmacenar en una lista de lineas\n')
with open('files_txt/archivo prueba.txt', 'r') as archivo:
    lineas = archivo.readlines()
    print('Lista de lineas:',lineas)

print()

dato_concatenado = ''
# imprimir linea por linea
for linea in lineas:
    dato_concatenado += linea.rstrip()
    dato_concatenado += ' , '
    # print(linea.rstrip())

# Eliminaremos los ultimos caracteres especialmente el , unido al final
dato_concatenado = dato_concatenado.rstrip(' \t\n, ')

print(dato_concatenado)

# Si deseariamos buscar un dato en especifico
nombre = 'ALEXANDRE PATO'
fecha_cumpleanios = '31/03/2002'

# Funciona como esperaba
if nombre in dato_concatenado:
    print('Su nombre existe')
else:
    print('Su nombre no existe')

# Nunca comparar if a and b in c
# Correcion, if a in c and b in c
if nombre.lower() in dato_concatenado and fecha_cumpleanios in dato_concatenado:
    print('Su nombre y su fecha de cumpleanios existe en el archivo..')
else:
    print('Sus datos desedos no existe en el archivo..')

# -------- Escritura de archivos ---------
# Si Python no encuentra este archivo, lo crea
ruta_archivo_2 = 'files_txt/archivo_escritura.txt'

# Abre el archivo en modo escritura, lo que significa que
# Python eliminara el contenido existente antes de modificar
with open(ruta_archivo_2, 'w') as archivo:
    # Escribe esta nueva cadena de caracteres en una linea
    # La escritura no devuelve un archivo modificado
    archivo.write('Estamos entendiendo el lenguaje de programacion\n')
    # Escribe esto como otra linea
    archivo.write('\tEs una nueva linea escrita, estoy escribiendo, wooow...')

# Python creo este file
ruta_archivo_3 = 'files_txt/archivo_creado desde una clase.txt'
with open(ruta_archivo_3, 'w') as archivo:
    archivo.write('Archivo creado con programacion, desde una clase de python... Esta interesante esto')


# ------- Actualizacion de archivos --------

# Si deseo escribir y leer haria lo siguiente
# modo r+ es modo actualizacioon
# Cuando escribes usando write() en modo 'r+', estás sobrescribiendo
# los datos existentes desde la posición actual del cursor.
# No estás insertando texto, sino reemplazando los bytes existentes.

with open(ruta_archivo_3, 'r+') as archivo:
    # Escribe al inicio
    archivo.write('Esta escribiendo y leyendo a la vez..')
    # Mueve el cursor de vuelta a la posicion 0
    archivo.seek(0)
    contenido = archivo.read()  # Leer el contenido después del cursor
    print(contenido)  # Mostrar el contenido

    # Mueve el cursor al final del contenido
    archivo.seek(0, 2)
    # Escribe en la posicion del cursor
    archivo.write('\nEstoy escribiendo al final del archivo por medio del cursor...')
    # Mueve el cursor al inicio
    archivo.seek(0)
    # Lee y presenta el archivo actualizado..
    contenido = archivo.read()

    print(contenido)


# ----------- Insertar Cadenas en Archivos --------------
ruta_archivo_4 = 'files_txt/archivo anexado.txt'

# A diferencia del modo 'r+', el modo 'a'
# Python no borra el contenido, mas bien, inserta al final
# Solo es un modo de escritura o indexacion,
# Lo cual insertara segun sean las veces que se ejecute
with open(ruta_archivo_4, 'a') as objeto_archivo:
    objeto_archivo.write('Primera creacion de la cadena...')
    objeto_archivo.write('\n')
    # Por que no escribir el contenido de otro archivo
    objeto_archivo.write('Insertando otra cadena')
    objeto_archivo.write('\n')

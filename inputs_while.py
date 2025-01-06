"""
    ENTRADAS DEL USUARIO Y BUCLES WHILE
"""
# la funcion input, pausa el programa, y espera un dato
# el dato almacenado por defecto es una cadena de caracteres
prompt_nombre = "Hola.. Ingrese su nombre: "
# nombre = input(prompt)

prompt_edad = "Ahora, Ingrese su edad: "
# Acepta solo entrada de datos numericos, sino, exist un error
# edad = int(input(prompt))

# Algo que se debe tomar en cuenta
# Si se ingresa un valor incorrect, salt ValueError, para ello se debe tratar con excepciones

# print("Tu nombre ingresado es", nombre,
#       "Tienes", edad, "anios.")

"""
      Ejercicio con entrada en el consiste alquilar un coche
"""

lista_coches_disponible = ['Subaru', 'Mercedez', 'Opel', 'Citroen', 'Honda', 'Toyota']

prompt = """
Bienvenido a la concensionaria de alquiler de Vehiculos..!
      Ingrese que marca de coche desearia alquilar : 
"""

coche_seleccionado = input(prompt)

while True:
    if coche_seleccionado.title() in lista_coches_disponible:
        print(f"Disponemos del coche que seleccionaste, marca {coche_seleccionado.title()}")
        break
    else:
        print('Lamentamos no tener la marca de vehiculo deseada... pero puedes revisar nuestro catalogo')
        request = input("Deseas revisar el catalogo? (S/N): ")

        if request.lower().startswith('n'):
            break
        else:
            print("Nuestro catalogo es el siguiente listado")
            for coche in lista_coches_disponible:
                print('-', coche)
            coche_seleccionado = input("Ingrese el coche que desea alquilar: ")

# print(coche_seleccionado)
# Use break cuando se usen bucles infinitos
# Puede usar banderas o flag, dando un valor boolean y se evalue en while

"""
    Uso del continue
    la sentencia continue, salta una linea de codigo en especifico
    omite cierto bloque de codigo y continua con la siguiente ejecucion
"""

# Contar del 1 al 10 y que solo muestre impares

sumador = 0
while sumador <= 10:
    sumador += 1
    if sumador % 2 == 0:
        print(f'salto este numero {sumador}')
        # Con continue, Python ignora el resto de codigo
        continue
        # ignora la siguiente linea
        print(f'salto este numero {sumador}')
    print(sumador)


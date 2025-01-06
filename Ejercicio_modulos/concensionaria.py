"""
Clase o archivo que simula una consensionaria de vehiculos
"""
# Variable predefinidad de vehiculos disponibles
marca_carros = {"chevrolet": ['sail', 'grand vitara', 'aveo', 'dmax'],
                "citroen": ['c3', 'c5', 'c-elysee', 'c3-aircross'],
                "audi": ['q5', 'a4', 'q5 quattro'],
                "BMW": ['x1', '320i', '330i', 'x3'],
                "volkswagen": ['polo', 'golf', 'tiguan', 'virtus']}
modelos = []


def entrada_usuario(mensaje):
    return int(input(mensaje))


def mostrar_marca_vehiculos():
    indice = 0
    menu = '\nLa lista de marca que dispone la concensionaria son:\n'
    print(menu)
    for marca in marca_carros.keys():
        indice += 1
        if marca != 'BMW':
            print(f"{indice} -{marca.title()}-")
        else:
            print(f"{indice} -{marca}-")


def mostrar_marca_modelos(numero):
    """Simulara un switch case"""
    global modelos
    if numero == 1:
        """eligio chevrolet"""
        print('Marca Chevrolet')
        modelos = list(enumerate(marca_carros['chevrolet'], start=1))
        for modelo in modelos:
            print(f'\t{modelo[0]} -{modelo[1].title()}')
        # print(type(modelos), modelos)

    elif numero == 2:
        """eligio citroen"""
        print('Marca Citroen')
        modelos = list(enumerate(marca_carros['citroen'], start=1))
        for modelo in modelos:
            print(f'\t{modelo[0]}- {modelo[1].title()}')

    elif numero == 3:
        """eligio audi"""
        print('Marca Audi')
        modelos = list(enumerate(marca_carros['audi'], start=1))

        for modelo in modelos:
            print(f'\t{modelo[0]}- {modelo[1].title()}')
    elif numero == 4:
        """eligio BMW"""
        print('Marca BMW')
        modelos = list(enumerate(marca_carros['BMW'], start=1))
        for modelo in modelos:
            print(f'\t{modelo[0]}- {modelo[1].title()}')

    elif numero == 5:
        """eligio volkswagen"""
        print('Marca Volkswagen')
        modelos = list(enumerate(marca_carros['volkswagen'], start=1))
        for modelo in modelos:
            print(f'\t{modelo[0]}- {modelo[1].title()}')
    else:
        """eligio otro numero"""
        print('No elegiste el numero adecuado..')
    return modelos


def seleccionar_vehiculo(indice):
    modelo_dato = list(modelos[indice-1])
    print(f"Eligio el vehiculo de modelo {modelo_dato[1].title()}")

# Las funciones o tambien llamados metodos,
# son aquellos fragmentos de codigo que cumplen una funcionalidad
# en el sistema, ya sean estas funcionalidades que
# tengan o no parametros predefinidos para su funcionalidad
# Por ejemplo, la computadora tiene la funcion de
# abrir_un_programa(prog) que tiene un parametro prog,
# y de argumento le mandamos que programa queremos que lo abra,
# en pocas palabras una funcion es una serie de tareas o logicas
# que evalua y realiza la maquina y a su vez nos devuelve un valor

"""VAMOS A REALIZAR UN PROGRAMA SENCILLO UTILIZANDO LAS FUNCIONES....."""


# Funcion sin parametros ni argumentos
def ingresar_funcion():
    # retorna una impresion de pantalla
    return print("Retorna la funcion")


ingresar_funcion()


# Funcion con parametros y argumentos
# nombre y apellido son parametros
def ingresar_nombre(nombre, apellido):
    print(f"Tu nombre y apellido son: {nombre} {apellido}")


# freddy Alexndr son argumentos
ingresar_nombre("freddy", 'Alexndr')


def multiplicar_datos(dato, veces):
    # return print(dato*veces, veces)
    print(f"{dato * veces} - {veces}")


multiplicar_datos("hola", 3)


# Funcion con parametros por default, y argumentos opcionales
# Tomar en cuenta el tipo de dato que sea opcional.... si es str -> "", si es int -> 0, o cualquiera de las dos -> : any
def request_funcion(dato_1, dato_2: any):
    return "Tienes 2 dato" if len(dato_1) and dato_2 else "Solo tienes un dato.."


print(request_funcion("Holaa", 3))
print(request_funcion("holiii", 'siuu'))


# Funciones con argumentos nombrados, que por si, necesariamente todos sus parametros deben tener al menos un argumento
def argumentos_funcion(nombre, apellido, direccion):
    print(f"""Tu nombre es {nombre}""")
    print(f"""Tu apellido es {apellido}
    y tu direccion es {direccion}""")
    # print(f"""Tu nombre es {nombre}""")


# argumentos de palabra clave
argumentos_funcion(direccion="San Pablo de Tenta",
                   nombre="Freddy",
                   apellido="Matailo")


# Valores predeterminados
# Consejo, el orden de los paramtros importa, al final utilice los predeterminados
def describe_pet(name_animal, anymal_type='dog'):
    print(f"Su mascota es un/a {anymal_type},\n"
          f"Su nombre es: {name_animal}")


# Al omitir el parametro y argumento anymal_type, por defecto es un dog
describe_pet(name_animal='Polo')


# Por ultimo y mas importante una funcion con un solo parametro y multiples argumentos o xargumentos (xargs)....
# como God manda, poner * a lado de la variable en plural,
# el simbolo *, es decir, *numeros, *variables, etc.. lo cual esta se va a pasar como una variable iterable...

def xargs_funcion(*variables):
    resultado = ""
    for variable in variables:
        resultado += str(variable) + "-"
    resultado = resultado[:-1]
    return resultado


print(xargs_funcion(1, 5, 6, "hola"))


# Y por ultimo, que casi me olvido, los parametros por palabras claves argumentadas es decir por keywords arguments, 
# cualquier variable en un solo parametro.. en sus argumentos se podria decir que es similar a un diccionario por que a una variable, 
# le asignamos un valor... 

def kwargs_funcion(**datos):
    for dato in datos:
        # print(dato)
        print(f"{dato} = {datos[dato]}")
    print(datos, "-> Vaya, esto es similar a un diccionario o a un objeto con sus datos, amazing!!")

    variable_iterable = list(datos)
    # print(variable_iterable[2])
    print(variable_iterable[:])
    # for indice in variable_iterable[:1]:
    #     print(indice)


kwargs_funcion(dato_1="Este es un datoo",
               dato_2="Es dato 2",
               description=1203202)

kwargs_funcion(nombre="Freddy",
               apellido="Matailo",
               direccion=1203202)

# Si en algun momento de nuestro programa desearemos clonar una lista
# basta con pasar a la funcion la lista [:]

marca_zapatos = ['nike', 'adidas', 'puma', 'lotto', 'umbro']
zapatosFacturads = []


def facturar_zapatos(zapatosPedids):
    # Mientras existen elementos en zapatos pedidos ejecuta.
    while zapatosPedids:
        zapato = zapatosPedids.pop()
        print(f"Estamos facturando la siguiente marca {zapato}")
        zapatosFacturads.append(zapato)


def mostrar_zapatos(zapatos):
    for zapato in zapatos:
        print('-', zapato)


# Reali
facturar_zapatos(marca_zapatos[:])
mostrar_zapatos(zapatosFacturads)


# Si en caso de que quiero solamente imprimir un valor,
# deberiamos indicar al iterador la posicion datos[0:1] o
# su clave  o datps["dato_1"]

# Realizaremos una mezcla de argum posicionales y arbitrarios (*args)
#

def cocinar_pizza(porciones, *ingredientes):
    """Resume la cantidad de porciones y los ingredientes"""
    print(f"Se estan haciendo cocinar {porciones}, con los siguientes ingrediente.")
    for i in ingredientes:
        print('-', i)


cocinar_pizza(5, 'papperoni', 'pina', 'queso')

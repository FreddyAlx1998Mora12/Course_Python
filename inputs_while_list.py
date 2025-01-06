"""
Como la clase inputs_while estabamos trabajando con datos,
ahora trabajaremos con listas o diccionadrios, subiremos el nivel de complejidad
para trabajar con este tipo de datos
"""
import time


# el ejemplo consiste en verificar una lista de usuarios
usuarios_noVerificados = ['emilio','alberto','luis','victor']
# lista que se llenara cuando se han verificado
usuarios_verificados = []

# Mientras no hayan elementos que ejecutar en la lista
while usuarios_noVerificados:
    # empieza a sacar el ultimo elemento
    usuario = usuarios_noVerificados.pop()
    print(f"Verificando...el siguiente dato {usuario}")
    # pausaremos mientras verifica
    time.sleep(2)
    print('Usuario varificado..')
    usuarios_verificados.append(usuario.title())

print('Se termino la verificacion, la lista de usuarios verificados son \n', usuarios_verificados)

# Para elmimar un dato especifico en una lista
mascotas = ['polo', 'kira', 'kiro', 'masha', 'gato', 'gato', 'perro']

while 'gato' in mascotas:
    # Mientras gato esta en la lista de mascotas seguira eliminando
    mascotas.remove('gato')

print("Se terminaron de eliminar los datos repetidos o dato gato de la lista mascota, lista actualizada", mascotas)

# Haremos que el usuario realice una lista de hobbies
# controlaremos con un flag
flag_ingreso = True
# Lista de Hobbies
hobbies = []
while flag_ingreso:
    hobbie = input("Ingrese un hobbie: ")
    hobbies.append(hobbie)

    mensaje = input("Desea ingresar algun otro hobbie? (s/n) : ")
    if mensaje.lower().startswith('n'):
        flag_ingreso = False

print("\n\tTu lista de hobbies son : ", hobbies)
print()
# Asi como con listas se podria realizar con diccionarios
personas = {}

print("""
------ Registro de Personas ------
""")
flag_ingreso = True
while flag_ingreso:
    registro_personal = {}
    nombre = input("Ingrese su nombre: ")
    edad = int(input('Ingrese su edad (solo numeros) : '))
    estatura = int(input('Ingrese su estatura (solo numeros) m: '))
    peso = int(input('Ingrese su peso(solo numeros) kg:'))

    registro_personal['edad'] = edad
    registro_personal['peso'] = peso
    registro_personal['estatura'] = estatura

    # diccionarios key : value
    personas[nombre] = registro_personal

    mensaje = input("Desea registrar otra persona? (s/n) : ")
    if mensaje.lower().startswith('n'):
        flag_ingreso = False

print("\n------ Registro de Personas ------")
for persona, datos_persona in personas.items():
    print(f"Nombre: {persona},"
          f"\nSus datos son:")
    for dato, valor in datos_persona.items():
        print(f'\t- {dato} = {valor}')
    print()

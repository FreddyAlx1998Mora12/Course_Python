# Realizaremos una calculadora basica haciendo uso de bucles y validaciones de caracteres...
import math

bienvenida = """Bienneidos a la Calculadora Basica interactiva de \"Python\""""

print(bienvenida)

# Variable para repetir la calculadora
respuessta_reinicio = True

while respuessta_reinicio:
    #Pediremos al user dos numeros, ingresara mediante terminal o entrada
    #n_1 = int(input('>> Ingrese un numero = '))
    n_1 = input('>>1. Ingrese un numero = ')

    #n_2 = int(input('>>2. Ingrese un segundo numero = '))
    n_2 = input('>>2. Ingrese un segundo numero = ')

    #Control de errores o en caso que el usuario ingrese cadena de caracteres
    #Ejecuta while mientras la condicion es verdadera o se cumpla...
    while not n_1.isnumeric():
        n_1 = input('>>1. Ingrese un numero = ')

    while not n_2.isnumeric():
        n_2 = input('>>2. Ingrese un segundo numero = ')
    
    print("""
    Elija el numero de la operacion que desea realizar.....
    -> 1 : Suma
    -> 2 : Resta
    -> 3 : Multiplicacion
    -> 4 : Division
    -> 5 : Exponencia
    -> 6 : Modulo

    """)

    digito_elegido = int(input('Digite su respuesta en numero(1-6) : '))
    
    def resultado_operacion(n1, n2, digito_el):
        n1 = int(n1)
        n2 = int(n2)
        if digito_el == 1:
            return n1 + n2
        elif digito_el == 2:
            return n1 - n2
        elif digito_el == 3:
            return n1 * n2
        elif digito_el == 4: 
            return n1 / n2 if n1 > n2 else n2 / n1
        elif digito_el == 5:
            return math.pow(n1,n2)
        else:
            if digito_el == 6:
                return n1%n2      
    
    print(f'Su resultado de la operacion: {resultado_operacion(n_1,n_2, digito_elegido)}')
    respuesta_string = input("\n\nDesea volver a repetir una operacion matematica en esta calculadora? (S/N) = ")

    # REVISAR AQUI, NO EVALUA LA RESPUESTA, BUCLE INFINITO......RESUELTO
    #respuessta_reinicio = False if respuesta_string.strip().lower().find('n') >= 0 else True
    #print(respuesta_string.strip().lower().find('n'))

    #mas simple es s = true, n n = false
    respuessta_reinicio = "s" in respuesta_string.strip().lower()

    print(respuessta_reinicio)


print('Gracias por utilizar mi calculadora basica interactiva..... :[]')

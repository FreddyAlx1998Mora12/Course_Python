"""Juego Ahorcado
Requerimientos:
Adivinar la palabra esocgida aleatoriamente por la computadora
Ingresar letra por letra, validando que no ingrese numeros usando try except
"""
import random
import time


def palabra_adivinanza():
    # Lista de palabras
    palabras = ['futbol', 'basket', 'voleybol', 'ecuavoly', 'tenis', 'natacion', 'boxeo', 'ciclismo']
    # elegira aleatoriamente cualquiera de ellas
    palabra = random.choice(palabras)

    return palabra


def dibujar_espacios_vacios(palabra):
    # Indica la cantidad de letras que debe poner
    caracter = " ____ "

    espacio = [caracter for i in range(0, len(palabra))]

    # CODIGO INNECESARIO
    # for i in range(0, len(palabra)):
    #     espacio.append(caracter)

    for e in espacio:
        print(e, end="")

    # return espacio
    return [" ____ " for _ in palabra]


def lista_sujeto_ahorcado():
    # 5 intentos para adivinar la letra
    intentos = [
        r"""
                        ---------------
                                      |
                                      |
                                     
    
    
    
    
    
    
    
    
    
    
    
    
    
                        """,
        r"""
                ---------------
                              |
                              |
                             ...
                            .....
                             ...
 
 
 
 
 
 
 
 
 
 
 
                """,
        r"""
                ---------------
                              |
                              |
                             ...
                            .....
                             ...
                              |
                              |
                              | 
                              |  
                              |
                              |
                              | 
                         
                         
                         
                         
                """,
        r"""
        ---------------
                      |
                      |
                     ...
                    .....
                     ...
                      |
                      |
                    / | 
                   /  |  
                      |
                      |
                      | 
                 
                 
                 
                 
        """,
        r"""
                ---------------
                              |
                              |
                             ...
                            .....
                             ...
                              |
                              |
                            / | \
                           /  |  \
                              |
                              |
                              | 
                           
                           
                           
                           
                """,
        r"""
                ---------------
                              |
                              |
                             ...
                            .....
                             ...
                              |
                              |
                            / | \
                           /  |  \
                              |
                              |
                            _ | 
                           /     
                          /       
                          |       
                         _|       
                """,
        r"""
                ---------------
                              |
                              |
                             ...
                            .....
                             ...
                              |
                              |
                            / | \
                           /  |  \
                              |
                              |
                            _ | _
                           /     \
                          /       \
                          |       |
                         _|       |_
                """
    ]
    return intentos


def limpiar_consola():
    print("\n" * 25)


def funcion_principal():
    # Variable que define el estado del juego
    juego_activo = True
    numero_intentos = len(lista_sujeto_ahorcado()) - 1
    mensaje = """
    --------------------------------------
    \t\tJUEGO DEL AHORCADO.
    Adivina la palabra, y salva el sujeto
    ______________________________________
    """
    print(mensaje)
    palabra_adivinar = palabra_adivinanza()
    # print(palabra_adivinar)
    espacios_letras = dibujar_espacios_vacios(palabra_adivinar)
    sujeto_ahorcado = lista_sujeto_ahorcado()
    print()
    print(sujeto_ahorcado[0])
    while juego_activo:
        # Validaremos que el usuario no ingrese numeros
        # Para esta ocasion utilizaremos el manejo de excepciones try except
        # Aunque se puede evitar con un bucle while, hasta que el usuario ingrese un dato correcto
        try:
            letra = input('Ingrese una letra: ')
            # Si la letra es un numero, lanza una excepcion que es un error de tipo

            if letra.isnumeric():
                raise TypeError('dato numerico o dato no valido')

        except TypeError as e:
            print(f'Ingreso un {e}, vuelva a ingresar solo letras, espere..')
            time.sleep(1)
            # limpiar_consola()

        else:
            if letra in palabra_adivinar:
                # list comprehension = [] para ahorrar el CODIGO INNECESARIO
                # indices = [] -> VARIABLE INNECESARIA
                indices = [i for i in range(len(palabra_adivinar)) if palabra_adivinar[i] == letra]

                # CODIGO INNECESARIO, for y ifs en una linea
                # for i in range(len(palabra_adivinar)):
                #     # verifica que una o n letras coincide con las n coincidencias de la palabra
                #     if letra == palabra_adivinar[i]:
                #         indices.append(i)

                # Reemplazamos la letra por el espacio
                for indice in indices:
                    espacios_letras[indice] = f" {palabra_adivinar[indice].upper()} "
            else:
                # Si la letra no es la correcta, dibuja el ahorcado y disminuye
                print(f'No es la letra, te quedan {numero_intentos - 1} intentos, intente con otra letra..')
                numero_intentos -= 1
                print(sujeto_ahorcado[6 - numero_intentos])

            # Muestra las letras adivinadas
            for e in espacios_letras:
                print(e, end="")
            print()
            # Verifica si hay espacios, o si alcanzo el numero maximo de intentos
            if " ____ " not in espacios_letras:
                juego_activo = False
                print("\nAdivinaste la palabra, felicidades...!")
            elif numero_intentos == 0:
                print(f'\nAlcanzo el numero maximo de intentos, la palabra era {palabra_adivinar}\n')
                juego_activo = False
                print(r'.../|\....GAME OVER.../|\....')


funcion_principal()

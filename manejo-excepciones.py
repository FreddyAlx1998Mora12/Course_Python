"""
    Manejo de Excepciones con Python, la buena practica de gestionar las excepciones son, 
    identificando y capturando desde la excepcion mas especifica y mas intuitiva a la mas general y ambigua (Se podria decirlo asi...)
"""

# Podemos crear por ejemplo cuando se pide un valor y el usuario escriba letras
# deberiamos mandarle que ha ingresado un valor incorrecto, o a su vez 

flag = True

while(not flag):

    try:
        dato = int(input("Ingrese un dato numerico = "))
        flag = not flag
    except ValueError:
        print("Ouups, digito un valor incorrecto... vuelva a intentarlo")
        # flag != flag
# print(dato, " -> es el numero que digitaste")


# Por ejemplo puede ser que en una operacion aritmetica deseamos dividir un numero para cero.. 
# Utilizaremos el validador de datos

def division(n1 , n2):
    try:
        return n1//n2
    except ZeroDivisionError:
        print()
        print("No es posible dividir entre cero..")
        return "No se pudo realizar la operacion..."


while(flag):
    try:
        numero_1 = int(input("Ingrese el primer numero = "))
        numero_2 = int(input("Ingrese el segundo numero = "))
        resultado = division(numero_1, numero_2)
        print(resultado, "- > Resultado de operacion")
        # Se puede utilizar este tipo de bandera, pero lo mas idoneo seria poner el break...
        # flag = not flag
        break

    except ValueError:
        # Execute when division for zero
        print("Ocurrio un error....")
        print("Dato invalido, vuelva a intentarlo...")
    else:
        # Execute si no ha ocurrido un error,
        # pero no se ejecutaria la excepcion
        # flag = not flag
        # print(division(numero_1, numero_2), "- > Resultado de operacion")
        pass

"""
    Manejo de Multiples Excepciones
"""
try:
    # Código que puede generar excepciones
    pass
except (ValueError, TypeError):
    # Manejo común para excepciones de tipo Value Error y tipo Type Error
    pass
except Exception:
    # Manejo de la excepción de tipo C o general
    pass

"""
    Excepciones forzadas
    utilizando el raise -> Que nos permite lanzarle o acivarle un error..
"""
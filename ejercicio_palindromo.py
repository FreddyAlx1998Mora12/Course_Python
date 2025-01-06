# Realizaremos un ejercicio que consiste en la entrada de numeros y cadenas de textos, en la cual se va a evaluar
# si la cadena o el numero que se ingreso, al tergiversar sus letras o palabras tiene el mismo signficado.

# Pediremos al usuario ingresar su valor
"""Ejercicio - > Palindromos"""
variable = input("Ingrese su valor = ")

def cadena_revertida(dato):
    """Funcion para invertir la cadena ingresada, y a su vez formatearla..."""
    dato_revertid = ""

    # Por slicing
    # dato_revers = dato[::-1]
    # return dato_revers
    
    # Por iterador for
    for cadena in reversed(dato):
        dato_revertid += str(cadena)

    # limpiamos TODOS(inicio, medio, final) los espacios en blanco con replace
    dato_revertid = dato_revertid.replace(" ", "").lower()

    return dato_revertid,dato

def funcion_palindromo():
    datos_cadenas = cadena_revertida(variable)
    dato1 = str(datos_cadenas[0])
    dato2 = str(datos_cadenas[1]).replace(" ","").lower()

    bool = True if dato1 == dato2 else False

    return print(f"Su Valor ingresado {variable} -> su cadena invertida es {dato1} =>", "Por lo tanto es un palindromo" if bool else "No es un palindromo.")

print(funcion_palindromo())

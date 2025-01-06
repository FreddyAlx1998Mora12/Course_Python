# Cadena de comparadores en if, else, con operadores logicos...
# Los operadores logicos son 
# not -> valor contrario o es diferente, en java se utiliza de la siguiente forma if(!True){......}
# and -> y 
# or -> o
# 
# y en los condicionales se evaluan siempre y cuando sus comparaciones o condiciones se cumplen o son VERDADERAS 

# gas = True
# encendido = False
# edad_cocinero = 15


# if gas and (encendido and edad_cocinero > 19):
#     print("Puedes cocinar algo..... ")
# elif encendido and edad_cocinero > 12:
#     print("Pide ayuda a tus mayores...")
# else:
#     encendido_comentario = "Cocina Apagada" if encendido else "Ya estuvo apagada..."
#     print("Lo siento no puedes cocinar nada.. :(, su cocina esta en modo: ", encendido_comentario)

# ////////////////////////////////////////
# Otro ejercicio es....

edad = int(input("Escribe su edad: "))

# Una buena practica en if para evitar poner if edad >10 and edad <25...
if 28 <= edad >= 11:
    print("Puedes entrar a la piscina")

# Esto es como las clases de operaciones logicas,
# donde al cumplir las condiciones logicas de una condicion,
# y tomando en cuenta la funcionalidad de las condicionales,
# esto permiten una ejecucion del codigo, por ejemplo
# cuando se cumple una condicion de operador AND quiere decir que
# sus condiciones deben ser absolutamente todas TRUE para que se de su ejecucion,
# asi mismo con OR, con NOT....

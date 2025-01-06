# importamos un modulo olibreria para trabajar con nnumeros.
import math

numero_entero = 2
numero_flotante = 5.023
numero_complejo = 2 + 2j

# round() -> evalua al numero mas cercano ya sea hacia arriba o hacia abajo, por lo general reciben numeros flotantes
print(round(numero_flotante), ">> round de numero flotante")

# abs() -> significa devuelve a un valor absoluto es decir siempre positivo
print(abs(-998))

# math.ceil() -> nos devuelve el numero int superior mas cercano
print(math.ceil(numero_flotante), '>> nos devuelve del metodo ceil')

# math.floor() -> nos devuelve el numero int inferior mas cercano, ex = 1.3 >> 1
print(math.floor(numero_flotante), '>> nos devuelve del metodo floor')
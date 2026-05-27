from string import digits, ascii_letters
import time

# Segun la notacion big O esto corresponde a un n elevado a la 4
# Lo que corresponde un passcode, un codigo de 4 digitos,
# Lo que se demuestra es la rapidez de buscar coincidencias con un n^4

# print(time.time())
# Esto es mas facil encontrar las posibles combinaciones en numeros decimales (0-9) 10^4
for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                print(i, j, k, l)

# Seria una serie de posibilidades desde a a z que corresponde aproximadamente 26 letras
# Sumando las 26 letras en mayusculas, 52 posibles combinaciones, en 4 digitos, seria 56^4
for i in ascii_letters:
    for j in ascii_letters:
        for k in ascii_letters:
            for l in ascii_letters:
                print(i, j, k, l)

# print(time.time())

# Tambien se pueden combinar, las letras con los numeros
# PRECAUCION, NO EJECUTAR CON MAS BUCLES
for i in digits+ascii_letters:
    for j in digits+ascii_letters:
        for k in digits+ascii_letters:
            for l in digits+ascii_letters:
                print(i, j, k, l)

# Cuanto mas corta es la contrasenia, es mucho mas facil encontrar las
# posibles coincidencias, cuanto mas mezclado y larga, es una contrasenia segura

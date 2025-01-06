# Comentarios en python, Este es un fichero o clase de bucles, para recordar.... 
# En primer lugar vamos a utilizar unas condicionales y su sintaxxis... 

# Bueno en primer lugar voy a importar una libreria para los random...
import random

lista_comida = ['frutas', 'verduras', 'mariscos', 'enlatados', 'frutos secos']

"""if len(lista_comida) < 1 : 
    print("Es una lista vacia")
else: 
    print("La lista contiene elementos")"""
#print(len(lista_comida))

# If en una linea seria similar a esto...
# A if Condicion else B, donde se evalua la condicion y si se cumple retorna A, caso contrario B..

if_line = f"La lista tiene un numero de {len(lista_comida)} elementos" \
    if len(lista_comida) > 1 else "La lista esta vacia, no contiene elementos"

#print(if_line)

# if..else..
n = random.randint(0, 4)
if lista_comida[n] == 'verduras':
    print("Son verduras ", n)
else:
    print('No son verduras ', n)

# If.. elif...elif.. else - utilizando metodo random... random.choice,
# random. choice para elegir un elemento aleatorio de una lista o secuencia..

tipo_comida_rndm = random.choice(lista_comida)

if tipo_comida_rndm == 'verduras':
    print('Son verduras')
elif tipo_comida_rndm == 'frutas':
    print('Son Frutas')
elif tipo_comida_rndm == 'mariscos':
    print('Son mariscos')
else:
    print(
        f"El elemento escogido es: {tipo_comida_rndm}"
        f", no es ni verdura, ni fruta, ni marisco, ni cumplen tus condiciones....!")

# Si se desea saber si un elemento esta dentro de una secuencia basta con

print('frutas' in lista_comida)

banned_users = ['lorena','rosario','gilmar']
user_new = 'diego'

if user_new not in banned_users:
    print(user_new.capitalize(), 'puedes postularte..')

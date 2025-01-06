#los iterables son aquellos elementos que se pueden iterar, ya sea una secuencia de caracteres como por ejemplo
# "Esto puede ser una lista de char o de caracteres", a la vez que una lista lista = [1, True, "hi", [22*3, 4+4, 'etc']]
# tupla = (22, 'abs', "casa", True) y diccionario = {"Bojack": "Sarah Lynn", "Freddy": "Johannson"}
# Se iteran en bucles for... 

#lista de numeros y cadenaa
# range(inicio, final-1, salto) -> rango desde n hasta k-esimo numero
# range(final) -> 0....final-1
lista_n = list(range(2,10,3))
# print(lista_n)
cadena = "Mi nombre es Rocket Groot"
# print(lista_n)

for numeros in lista_n:
    # print(numeros)
    print(numeros, 'h '*numeros)
contador = 0
# cadena = cadena.split()
for letra in cadena:
    print(letra,contador)
    contador += 1

# Lista de Raza de animales
razas_perros = ["labrador retriever", "golden retriever", "bull terrier", "pastor aleman", "bullDog"]

for raza in razas_perros:
    print(f"Interesante el can de raza {raza.title()}, me gusta su inteligencia, y su sentido de convivencia.")
print("Ya sabemos quienes son el mejor amigo del hombre... ;D")

# lista de cuadrados
squares = []
for n in range(11):
    # ** indican exponente
    squares.append(n**2)
print("Lista de cuadrados",squares,"-- 0 , 1 , 2 ... 11-1")

#
print("Estadistica sencilla:", min(squares), max(squares), sum(squares), sum(squares)/len(squares))
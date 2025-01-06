# El ejercicio consiste basicamente en crear una lista de invitados, si pudiese invitar a 3 personas a una cena
# quienes serian esas 3 personas, debe realizar una lista con esas 3 personas y usa la lisra enviar una invitacion para cada uno.
# 2. Acaba de enterarse de que uno de sus invitados no podran asistir a la cena, por lo tanto, debe pensar en otra persona para
# que cubra la vacante, y ademas de ello invitarle a la cena.
from random import random, randrange

invitados_especiales = ["Lorena", "Victor", "Ray Eugenio", "Elvia", "Kerly"]


# Metodo invitacion de cena
def invitarCena(nombre):
    print(f"Hola {nombre}, ud es un invitado especial a mi cena, desea aceptarlo?")
    pass


for invitado in invitados_especiales:
    invitarCena(invitado)

# Todos Aceptaron, pero ocurre que Kerly no puede
indice_invitado_ausente = invitados_especiales.index('Kerly')
invitados_ausentes = [invitados_especiales.pop(indice_invitado_ausente)]

# Nueva invitacion
nuevo_invitado = 'Diego'
invitarCena(nuevo_invitado)

#Invitado acepto, forma parte la lista de los invitados
invitados_especiales.append(nuevo_invitado)

print(f"\nLista de Invitados: {invitados_especiales}\nLista de invitados ausentes: {invitados_ausentes}")

# Existe la disponibilidad de una mesa mas para mas invitados, puedo disponer de mas invitaciones
invitados_especiales_2 = ['Kerly L', 'Diana', 'Joffre', 'Lilian', 'Eli', 'Dany']

print(f"\n2da Lista de Invitados: {invitados_especiales_2}")
# Enviar invitaciones
for invitado in invitados_especiales_2:
    invitarCena(invitado)

#Aceptaron todos a excepcion de 2 invitados, los invitados que no aceptaron son Eli y Dany
invitado_ausente = "Eli"
invitado_ausente_2 = 'Dany'

print(f"Los invitados que no pudieron asistir son {invitado_ausente} - {invitado_ausente_2}")
invitados_especiales_2.remove(invitado_ausente_2)
invitados_especiales_2.remove(invitado_ausente)  # elimina por valor, pop elimina por indice...

print(f"\n2da Lista de Invitados Actualizados: {invitados_especiales_2}")

invitados_ausentes.insert(len(invitados_ausentes), invitado_ausente_2)  #Inserta el elemento al final de la lista..
invitados_ausentes.insert(0, invitado_ausente)  #inserta el elemento al inicio de la lista

print(f"Lista de invitados ausentes: {invitados_ausentes}")


# Sucede el evento de que la mesa no llegara a tiempo y por lo tanto, solo se puede invitar en una sola mesa a 4 personas, es decir
# que se debe invitar en una sola mesa a dos invitados de ambas listas.... eliminar y enviar un mensaje diciendo que lo siente..

#crearemos un metodo o funcion para imprimir el mensaje o enviar mensaje
def lamentarInvitacion(nombre):
    print(f"Hola! {nombre}, lo siento mucho por las molestias causadas...")


# metodo para eliminar invitados
def eliminarInvitado(indice, lista_invitados):
    invitado_extraido = lista_invitados.pop(indice)
    lamentarInvitacion(invitado_extraido)
    invitados_ausentes.append(invitado_extraido)


# Eliminaremos hasta que en la lista sean 2 personas, para ello, la eleccion de la persona sera al azar, o aleatorio
for invitado in invitados_especiales_2:
    if len(invitados_especiales_2) > 1:
        eliminarInvitado(randrange(0, len(invitados_especiales_2)), invitados_especiales_2)

for invitado in invitados_especiales:
    if len(invitados_especiales) > 1:
        eliminarInvitado(randrange(0, len(invitados_especiales)), invitados_especiales)

# Presentare la lista de los invitados
print(
    f"Los invitados elegidos son: {invitados_especiales} {invitados_especiales_2}\nLos invitados eliminados y ausentes: {invitados_ausentes}")

# Eliminaremos los 2 ultimos de la lista con la sentencia del
del invitados_ausentes[-2:]
print(invitados_ausentes)

# Eliminamos toda la informacion de la lista...
del invitados_ausentes[:]
print(invitados_ausentes)

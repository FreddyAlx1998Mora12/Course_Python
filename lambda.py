# Lambda
# variable = lambda parametro : cuerpo de funcion
# Tambien puede recibir iterable como argumentos 

# importar un modulo y una variable 
from listas_comprension import usuarios_enumerados

usuarios = usuarios_enumerados

# usamos las variables map(), reduce() o filter
# variable = funcion_iteradores(lambda parametro : cuerpo o funcion simple expresion, iterable)
filtro_usuario = map(lambda user : user[0].lower() in ['a', 'e', 'i'], usuarios)
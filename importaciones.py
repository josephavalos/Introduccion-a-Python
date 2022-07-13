# Modulo
"""
Es un archivo Python que contiene
definiciones y sentencias.
"""
# Importacion
"""
Es una sentencia que da acceso a las
funciones y constantes definidas en el
modulo importado.

Su sintaxis es:
import <modulo>

Cuando llamamos a la funcion
que esta definida en ese modulo
la llamamos asi:
<modulo>.<funcion>(<args>)

Por ejemplo:
"""
import math
print(math.pow(9, 2))

"""
Para acceder a una constante importada
de un modulo, lo hacemos de la siguiente
manera:
<modulo>.<constante>

Por ejemplo:
"""
print(math.pi)

"""
Para importar con un nombre diferente al modulo
se puede hacer asi:
import <modulo> as <nombre_alternativo>

Cuando llamamos a la funcion
que esta definida en ese modulo
con nombre alternativo:
<nombre_alternativo>.<funcion>(<args>)

Por ejemplo:
"""
import math as matematicas
print(matematicas.pow(9, 2))

# Otra forma de importar es
"""
Para importar un elemento especifico de un
modulo se hace asi:
from <modulo> import <elemento>

Por ejemplo:
"""
from math import pow
print(pow(9, 2))
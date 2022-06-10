# Ciclo for
"""
Estructura de control en programacion que permite
ejecutar una o varias lineas de codigo multiples
veces.

Lo usamos cuando sabemos con antelacion CUANTAS VECES
debemos repetir ciertas instrucciones.

Su sintaxis es:
for <var> in range(<inicio>, <fin>):
    # Codigo
"""
for i in range(4):
    print(i)

"""
Se puede personalizar aun mas la funcion range
si usamos 3 parametros...

range(start, stop, step)

start: El valor del parametro start (0 si no se 
utiliza el parametro).

stop: El valor del parametro stop.

step: El valor del parametro step (1 si no se utiliza
el parametro.)
"""

# Iterando en listas y tuplas
'En lista...'
for num in [1, 2, 3]:
    print(num)

'En tupla...'
for num in (1, 2, 3):
    print(num)

# Iterando en diccionarios
'En claves...'
letras = {'a': 1, 'b': 2}
for clave in letras:
    print(clave)

'En valores...'
for valor in letras.values():
    print(valor)

'En pares clave-valor...'
for clave, valor in letras.items():
    print(clave, valor)
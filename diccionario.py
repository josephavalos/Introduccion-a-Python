# Diccionarios
"""
Es una coleccion de pares clave-valor.

Por ejemplo:
"""

diccionario = {'A': 45, 'B': 30}

# Caracteristicas
"""
- Las claves deben ser unicas e inmutables.
- Los valores asosiados pueden ser de cualquier tipo.
- La clave se una para acceder a su valor asociado.
- Los pares clave-valor pueden ser modificados, añadidos
  y eliminados.
"""
# Acceder a los valores...
"""
Para acceder a un valor se hace de la siguiente
manera:
<diccionario>[<clave>]
"""
print(diccionario['A'])

# Otra forma de acceder a los valores...
'Utilizando el metodo get()'
print(diccionario.get('B'))

# Añadir y Modificar
"""
La sintaxis es la siguiente:
<diccionario>[<clave>] = <nuevo_valor>
"""
# Modificando...
diccionario['A'] = 90
print(diccionario)

# Añadiendo...
diccionario[1] = 45
print(diccionario)

# Eliminar o borrar
"""
La sintaxis es la siguiente:
del <diccionario>[<clave>]
"""
# Eliminando clave añadida...
del diccionario[1]
print(diccionario)

# Revisar si existe en el diccionario.
print('A' in diccionario)
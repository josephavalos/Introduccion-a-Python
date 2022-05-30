variable = 'Jose'
"""
Con la funcion type() podemos ver el tipo de datos que guarda la
variable, en este caso sera class 'str' haciendo referencia a String.
"""
print(type(variable))

variable = 2
"""
Ahora tiene guardado un 2 por lo tanto tiene pertenecera al tipo
de dato integer que lo muestra como class 'int'
"""
print(type(variable))


# Tamaño (Length)

variable = 'Jose'
"""
La variable en este caso tiene 4 caracteres formados por la 
palabra "Jose".
"""
print(len(variable))

"Pero si imprimimos un len vacio me va dar cero."
print(len(""))
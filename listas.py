# Las listas se definen con corchetes.
letras = [2, 'jose', 3.1416, 'ricardo', True]

# Accediendo a un valor especifico de la lista
print(letras[1])

# Rebanando lo que hay en el indice 1
'Primero se lo asigno a una variable'
index1 = letras[1]
'Aca lo rebano con el formato <cadena>[inicio:fin:paso]'
print(index1[1:5:2])

# Rebanando lo que hay en el indice 2
index2 = letras[2]
"""
Con la funcion round(numero, decimales) definimos
cuantos decimales llevara el numero, en este caso
se definen 2 decimales...
"""
print(round(index2, 2))

'Otra forma de quitar decimales es con la funcion format()'
print('{:.2f}'.format(index2))

# Negando valor booleano
index4 = letras[4]
print(not index4)


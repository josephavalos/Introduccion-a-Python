# Uso de funcion append()
lista = ['hola', 1, 'tres', 2, True, False]

"""
La funcion append() agrega un nuevo elemento al final
de la lista.

Su sintaxis es asi:
<listas>.append(<elemento>)
"""
lista.append(5)
print(lista)

# Uso de insert()
"""
La funcion insert() agrega un nuevo elemento
donde se le indique.

Su sintaxis es asi:
<listas>.insert(<indice>, <elemento>)
"""
lista.insert(0, 'jose')
print(lista)

# Uso de remove()
"""
La funcion remove(), elimina un elemento
que nosotros especifiquemos. 

Su sintaxis es asi:
<listas>.remove(<elemento>)
"""
lista.remove('jose')
print(lista)

# Verificar si un elemento se encuentra en una lista.
vocales = ['a', 'e', 'i', 'o', 'u']
print('u' in vocales)

# Obtener el indice de una del elemento de una lista.
print(vocales.index('a'))

# Cambiar valor en un indice especifico.
vocales[0] = 'jose'
print(vocales)
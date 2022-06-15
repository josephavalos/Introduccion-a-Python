# Funcion
"""
Es un bloque de codigo reutilizable que realiza 
una sola tarea especifica.

Su sintaxis es:
def <funcion>():
    # Codigo
"""
def mostrar_mensaje():
    print('Hola mundo')

mostrar_mensaje()
mostrar_mensaje()
mostrar_mensaje()

# Parametro
"""
Variable que se incluye en la definicion de la
funcion para representar y guardar un valor que
podemos pasar cuando llamamos a la funcion.
"""
def mostrar_doble(num):
    print(num * 2)

num = int(input('Digite un valor: '))
mostrar_doble(num)

def sumar(x, y):
    print(x + y)

lista = [1, 2]
sumar(lista[0], lista[1])

# Funcion con retorno
"""
Retorna un valor luego de completar la tarea.

Su sintaxis es:
def <funcion>(params):
    # Codigo
    return <valor>

Cuando se ejecuta 'return', la ejecucion de la 
funcion se detiene inmediatamente.

Si NO HAY una sentencia 'return' en la funcion, el
valore retornado por defecto sera 'None'. 
"""
def mostrar_suma(x, y):
    return x + y

print(mostrar_suma(lista[0], lista[1]))

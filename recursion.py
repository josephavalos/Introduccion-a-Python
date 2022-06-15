# Recursion
'Definir algo en terminos de si mismo.'
'La funcion recursiva es una funcion que se llama a si misma.'

# Sucesion de Fibonacci
"""
Es un ejemplo muy famoso de una sucesion recursiva

Cada numero de la secuencia es el resultado de
sumar los dos numeros anteriores.
fib(n) = fib(n-1) + fib(n-2)

La secuencia empieza con los numeros 0 y 1...
0, 1, 1, 2, 3, 5, 8, 13, 21,...
"""
def fibonacci(n):
    """
    n: posición en la sucesión (iniciando en 0)
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))

"""
Las Funciones Recursivas
Deben tener:
- Caso base
- Caso recursivo

Para que sea recursiva siempre tiene que volver
a su Caso base.
"""

# Selecciona el resultado de esta llamada
# a la funcion factorial:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
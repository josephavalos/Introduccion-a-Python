# SyntaxError
"""
Error en la sintaxis del programa.
Ocurre cuando no se siguen las reglas
formales para escribir código en
Python.
"""

# Excepcion
"""
Error detectado durante la ejecución
de un programa.
"""

# IndexError
"""
Es una excepcion que se produce cuando
tratamos de acceder a una cadena de caracteres
con un indice que esta mas alla de lo
permitido

Por ejemlo:
'Hola, mundo'[45]
"""

# KeyError
"""
Ocurre cuando tratamos de acceder a una clave
que no existe en un diccionario.

Por ejemplo:
puntos = {
    "Nora":87,
    "Gino":100,
    "Loretto":67,
    "Talina":45
}
puntos['Jack']
"""


# NameError
"""
Se genera cuando el nombre de
una variable no se reconoce.

Por ejemplo:
lista_colores
"""

# ZeroDivisionError
"""
Error de division por cero

Por ejemplo:
5 / 0
"""

# Try y Except
"""
try:
   # Intenta ejecutar este código
except:
   # Si ocurre una excepción,detente
   # inmediatamente y ejecuta éste código

Por ejemplo:
"""
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

try:
    resultado = num1 / num2
    print(f'{num1} / {num2} = {resultado}')
except:
    print('Alerta, Excepcion')

"""
Tambien se puede agregar el
tipo de error en el except:
"""
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

try:
    resultado = num1 / num2
    print(f'{num1} / {num2} = {resultado}')
except ZeroDivisionError:
    print('Alerta, Excepcion')

# Para trabajar con la Excepcion
"""
Se puede asignar la excepcion a una
variable para despues trabajarla:

try:
   # Intenta ejecutar este código
except <tipo_de_excepcion> as <var>:
   # Si ocurre una excepción,detente
   # inmediatamente y ejecuta éste código

Por ejemplo:
"""
num1=int(input("Ingrese un número:"))
num2=int(input("Ingrese otro número:"))
try:
    resultado = num1 / num2
    print(f"{num1} / {num2} = ",resultado)
except ZeroDivisionError as e:
    print(f'Error: {e}')

# Tambien se puede trabajar con clausula else
"""
Ésta sirve como respaldo igual
que en los condicionales.

try:
   # Intenta ejecutar este código
except <tipo_de_excepcion> as <var>:
   # Si ocurre una excepción,detente
   # inmediatamente y ejecuta éste código
else:
    # Si no ocurrio una excepcion en 'try'
    # ejecuta este codigo.

Por ejemplo:
"""
num1=int(input("Ingrese un número:"))
num2=int(input("Ingrese otro número:"))
try:
    resultado=num1 / num2
    print(f"{num1}/{num2}=",resultado)
except ZeroDivisionError as e:
    print(e)
else:
    print("Else")

# Tambien se puede trabajar con clausula finally
"""
Esta nos permite ejecutar codigo
si ocurrio una excepcion o no,
es decir; se ocupa para algo que 
debe ocurrir siempre.

try:
    # Intenta ejecutar este código
except <tipo_de_excepción>:
    # Si ocurre una excepción de este tipo,
    # detente inmediatamente y ejecuta
    # éste código
else:
    # Si no ocurrio una excepcion en 'try'
    # ejecuta este codigo.
finally:
    # Luego, ejecuta este código

Por ejemplo:
"""
num1=int(input("Ingrese un número:"))
num2=int(input("Ingrese otro número:"))
try:
    resultado=num1 / num2
    print(f"{num1}/{num2}=",resultado)
except ZeroDivisionError as e:
    print(e)
else:
    print("Else")
finally:
    print('Finally')

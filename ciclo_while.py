# Ciclo while
"""
Ciclo que continua mientras una condicion es
verdadera y se detiene cuando es falsa.

Lo usamos cuando NO sabemos CUANTAS VECES debemos 
repetir ciertas instrucciones, es decir que no tiene
un numero fijo o predeterminado de iteracion.

Su sintaxis es:
while <condicion>:
    # Codigo
"""

x = 20
while x < 35:
    print(x)
    x += 3 # Al escribir esta linea la condicion en algun momento dejara de ser verdadera.
    
while x < 35:
    print(x) # Aqui la condicion siempre sera verdadera por lo tanto sera un ciclo infinito.
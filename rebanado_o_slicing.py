# Rebanada de una cadena de caracteres

"""
Para obtener una rebanada de una cadena de caracteres se hace de la siguiente manera:

<cadena>[inicio:] => Toma caracteres del inicio al final.
<cadena>[:fin] => Toma caracteres de inicio al final (*SIN INCLUIR EL FINAL).
<cadena>[:] => Toma carectares de principio a fin.

Por ejemplo:
"""
palabra = 'Python' # En la variable hay 6 letras que conforman la palabra "Python"
"De esa palabra quiero sacar solo las letras 'yth'"
print(palabra[1:4]) # Se imprime la rebanada 'yth'

# Otra forma de rebanar
"<cadena[inicio:fin:paso]>" # El paso define como saltar de un caracter al siguiente.

"Por ejemplo, para que solo obtener las letras 'Pto' se hace asi."
print(palabra[0:6:2])

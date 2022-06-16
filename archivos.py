# Sentencia 'with'
"""
Nos permite abrir un archivo y luego
cerrarlo automaticamente.>

Su sintaxis es:
with open('<nombre_archivo>.txt', 'r') as archivo:
    # Trabajar con el archivo

r: es el parametro por defecto 'read'
   por lo cual leera el archivo.

archivo: es una variable que nosotros escogemos
         se le asigna la representacion del archivo
         a la variable.

"""

# Trabajando con un archivo
with open('C:/Users/josep/Desktop/YouTube.txt', 'r') as archivo_youtube:
    for linea in archivo_youtube:
        print('=====Frase======')
        print(linea)

# Modos de Apertura de Archivos
"""
r (read-leer): solo para ver el contenido del
                 archivo.
w (write-escribir): reemplazar completamente el contenido
                    del archivo, es decir que borra lo que
                    el archivo ya tenia.
a (append-añadir): permite añadir contenido al final del
                   archivo sin modificar el contenido
                   existente.
Agregar un + incluye leer
Por ejemplo, w+ es leer y escribir.
"""

# Ejemplo con un diccionario
notas = {
    "Nora":87,
    "Gino":100,
    "Loretto":67,
    "Talina":45
}
with open("data_estudiantes.txt",'w') as archivo:
    for nombre,nota in notas.items(): # Iterando en el diccionario
        archivo.write(nombre+" - "+str(nota)+"\n")

# Agregando nuevas notas al archivo
nuevas_notas={
    "Emily":54,
    "Daniel":98,
    "Julienne":78
}
with open("data_estudiantes.txt",'a')as archivo:
    for nombre,nota in nuevas_notas.items():
        archivo.write(nombre+" - "+str(nota)+"\n")
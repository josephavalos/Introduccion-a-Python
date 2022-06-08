# Metodos Importantes
"""
.count(<elem>): Permite contar cuantas veces se repite un elemento en una lista.
.extend(<lista>): Permite extender una lista agregandole los elementos de otra.
.pop(): Elimina y retorna un elemento de la lista..
.reversa(): Reversa el orden actual de la lista.
.sort(): Ordena la lista en un orden especifico, ascendente o descendente.
"""
nums = [1, 2, 3, 4, 5, 5]

print(nums.count(5))
nums.extend(['jose', 'isaias', 'avalos', 'diaz'])
print(nums)
print(nums.pop())
nums.reverse()
print(nums)
nums.sort()
print(nums)
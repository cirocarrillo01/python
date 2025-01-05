print('----- manejo de sets -----')
#crear un conjunto
mi_set = {1,2,3,4,5,4}
print(f'mi set: {mi_set}')

#agregar elementos al set
mi_set.add(6)
mi_set.add(7)
print(f'mi set modificado1: {mi_set}')

# intebtamo agregar un elemento duplicado
mi_set.add(3)
print(f'mi set modificado2: {mi_set}')

# eliminar un elemento del conjunto
mi_set.remove(4)
print(f'mi set modificado3: {mi_set}')

# iterar los elementos del set
for elemento in mi_set:
    print(elemento, end=' ')

# comprobar si hay un elemento en el set
print(f'\nExiste el valor de 4 en el set? {1 in mi_set}')

#obtener la longitud del set
print(f'longitud del conjunto: {len(mi_set)}')
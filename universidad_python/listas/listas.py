# ----- manejo de listas --------------------------------------

mi_lista = [1, 2, 3, 4, 5]

print(f'{mi_lista} -> Lista original')

# largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al ultimo indice de la lista: {mi_lista[-1]}')

# modificar los elementos de una lista
mi_lista[1]=10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

# agregamos un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> se agrego el elemento 6')

# añadir un nuevo elemento en un indice especifico
mi_lista.insert(2, 15)
print(f'{mi_lista} -> se añadio el valor de 15 en el indice 2')

#eliminar elementos de una lista
# usado el metodo remove
mi_lista.remove(5)
print(f'{mi_lista} -> se removio el valor 5')

# removemos por indice con el metodo pop
mi_lista.pop(1) # remueve el elemento del indice 1
print(f'{mi_lista} -> se elimina el indice 1')

# eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista} -> se elimino el indice 2')

# obtener sublistas
sublista = mi_lista [1:3] # genera una sublista del indice 1 al 2 (3 no se incluye)
print(f'sublista [1:3]: {sublista}')

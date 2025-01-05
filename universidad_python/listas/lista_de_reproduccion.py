# ----- lista de reproducion ---------------------------
print('----- lista de reproduccion -----')

#creamos lista vacia
lista_reproduccion = []

numero_canciones = int(input('cuantas canciones deseas agregar: '))

# iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'proporcione la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# emepzamos a agregar canciones
#lista_reproduccion.append('Hotel california - Eagles')
#lista_reproduccion.append('Staying Alive - Bee gees')
#lista_reproduccion.append('Dream on - Aerosmith')

# ordenar la lista en orden alfabetico. sort
lista_reproduccion.sort()

# Mostrar la lista de canciones
#print(f'\n lista de reporduccion e orden alfabetico')
#print(lista_reproduccion)

# Mostrar lista iterando sus elementos
print()
print('iteramos la play list')
for cancion in lista_reproduccion:
    print(f' - {cancion}')


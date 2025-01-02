# ----- lista de reproducion ---------------------------
print('----- lista de reproduccion -----')

#creamos lista vacia
lista_reproduccion = []

# emepzamos a agregar canciones
lista_reproduccion.append('Hotel california - Eagles')
lista_reproduccion.append('Staying Alive - Bee gees')
lista_reproduccion.append('Dream on - Aerosmith')
lista_reproduccion.append('Me gustas - Young Tender')

# ordenar la lista en orden alfabetico. sort

lista_reproduccion.sort()

# Mostrar la lista de canciones
print(f'\n lista de reporduccion e orden alfabetico')
print(lista_reproduccion)

# Mostrar lista iterando sus elementos
print('iteramos la play list')
for cancion in lista_reproduccion:
    print(f' - {cancion}')


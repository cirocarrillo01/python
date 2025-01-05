# ----- tuplas --------------------------------------
print('----- manejo de tupla -----')
mi_tupla = (1,2,3,4,5)

# no podemos modificar una tupla
print(mi_tupla)
# No podemos modificar una tupla
for i in mi_tupla:
    print(i,end=' ')

# crear una tupla para una coordenada x,y
coordenada = (3, 5)
# Accedemos a cada elemento de la tupla
print(f'\ncoordenada en el eje x: {coordenada[0]}')
print(f'coordenada en el eje y: {coordenada[1]}')

# crear una tupla unitaria
tupla_un_elemento = 10,
print(f'tupla de un elemento: {tupla_un_elemento}')

# Tupla anidada
tupla_anidada = (1,(2,3),(4,5))
print(tupla_anidada)
print(f'segundo elemento de la tupla: {tupla_anidada[1]}')

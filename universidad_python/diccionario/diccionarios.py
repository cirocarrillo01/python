# ----- dicionarios ------------------------------------
print('----- diccionarios -----')
# creamos un dict de persona con clave y valor
persona = {
    'nombre':'ciro',
    'edad': 30,
    'ciudad': 'bogota'
}
print(f'dicionario de persona: {persona}')

# aceder a los elementos del dicionario
print(f'nombre: {persona['nombre']}')
print(f'edad: {persona.get('edad')}')
print(f'ciudad: {persona.get('ciudad')}')

# modificar un vaor del diccionario
persona['edad'] = 35
print(f'diccionario de persona: {persona}')

#agregamos un nuevo elemento
persona['profesion'] = 'ingeniero'
print(f'diccionario de persona: {persona}')

# eliminar un elemento
del persona['ciudad']
print(f'diccionario de persona: {persona}')
persona.pop('profesion')
print(f'diccionario de persona: {persona}')

# iterar los elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'llave: {llave}, valor: {valor}')

# obtener los valores
print('\nvalores del diccionario: ')
for valor in persona.values():
    print(f'- valor: {valor}')

print('\nllaves del diccionario: ')
for llave in persona.keys():
    print(f'- llave: {llave}')
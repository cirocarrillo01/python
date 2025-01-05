# ----- listas con diccionarios ----------------------
personas = [
    {
    'nombre':'regina',
    'apellido':'flores',
    'edad':21
    },
    {
    'nombre':'alejandro',
    'apellido':'reyes',
    'edad':32
    }
]
print(personas)
for elem in personas:
    print(elem)
# acceder a un diccionario desde una lista
print(f'''Nombre: {personas[0].get('nombre')}''')
print(f'''Apellido: {personas[0].get('apellido')}''')
print(f'''Edad: {personas[0].get('edad')}''')

# recorrer los elementos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'{contador+1} - persona: {persona}')

# ------ sistema de prestamo de libros ------
'''comentarios:
'''
# ------ comandos de entrada de datos -------
print('--- sistema de prestamo de libros ---')
usuario_1 = input('el usuario tiene credencias de estudiante (SI/NO)?: ').lower().strip()
usuario_2 = int(input('a cuantos kilometros vives de la biblioteca: '))

# ------ comandos de formulas de datos ------
DISTANCIA_PERMITIDA = 3

# ------ comandos de salida de datos --------
print('--- sistema de prestamo de libros ---')
elegible = (usuario_1 == 'si' or
                        usuario_2 <= DISTANCIA_PERMITIDA)
print(f'ERES elegible para prestamo de libros: {elegible} ')

# ------- fin ------------------------------
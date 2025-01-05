# ----- lista de suscriptores --------------------------

print(f'----- lista de susscriptores -----')

# definir el set inicial
#suscriptores = {} #aqui se define un diccionario vacio
suscriptores = set() #definimos un set vacio

numeros_suscriptores = int(input('Proporciona el numero de suscriptores iniciales: '))
for _ in range(numeros_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

print(f'lista de suscriptores inicial: {suscriptores}')

#verificar si un nuevo suscriptor ya esta en la lista
nuevo_suscriptor = input('proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya esta en la lista: {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista: {nuevo_suscriptor}')

#eliminar un suscriptor
suscriptor_eliminar = input('proporciona suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

# verificamos a cantidad total de suscriptores
print(f'cantidad total suscriptores: {len(suscriptores)}')

#mostrar todos los suscriptores
print('----- lista de suscriptores -----')
for suscriptor in suscriptores:
    print(f'-- {suscriptor}')

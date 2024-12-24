#--------- generador de id unico ---------
from random import randint

#------------ ingresar datos -------------
print('---------- sistema generador de ID unico -----------')
var_nombre = input('Ingresar nombre: ')
var_apellido = input('Ingresar apellido: ')
var_anio = input('Cual es tu año de nacimiento (YYYY)? ')

#------------ formular datos -------------
var_nombre_1 = var_nombre.strip().upper()[:2]
var_apellido_1 = var_apellido.strip().upper()[:2]
var_anio_1 = var_anio.strip()[-2:]
var_random = randint(1000,9999)

#------------ mostrar datos --------------
print()
print(f'Hola {var_nombre}')
print(f'\tTu nuevo numero de identificacion (ID) generado por el sistema es:')
print(f'\t{var_nombre_1}{var_apellido_1}{var_anio_1}{var_random}')
print(f'\tFelicitaciones!')

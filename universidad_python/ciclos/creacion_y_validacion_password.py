# ----- creacion y validacion de password ------------
'''comentario:
'''
# ----- constantes ------------------------------------
print('----- creacion y validacion de contraseña -----')
print('''Mensaje:
la contraseña debe tener almenos 6 caracteres.
''')
pas = input('ingrese vaor de contraseña: ')
# ----- ciclos ----------------------------------------
while len(pas) < 6:
    print('----- creacion y validacion de contraseña -----')
    print('''Mensaje: contraseña no cumple con requisitos,
    la contraseña debe tener almenos 6 caracteres.
    ''')
    pas = input('ingresa un nuevo valor para creacion de contraseña: ')
else:
    print('valor de contraseña es valido.')

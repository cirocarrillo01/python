print('---- sistema administrativo de cuentas ------')

salir = False

while not salir:
    print('''Menu:
    1. crear cuenta
    2. eliminar cuenta
    3. salir''')
    opcion = int(input('escoge una opcion: '))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('eliminando tu cuenta...\n')
    elif opcion == 3:
        print('saliendo del sistema. \n')
        salir = True
    else:
        print('opcion invalida, proporciona otra opcion \n')
else:
    print('terminando el sitema de administracion de cuentas')

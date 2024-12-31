# ----- cajero automatico ---------------------------
'''comentario:

'''
# ----- constantes -------------------------
SALDO = 1000
salir = False
# ----- ciclo ------------------------------
while not salir:
    print('--- aplicacion de cajero automatico -----')
    print('''MENU:
    1. depositar
    2. retirar
    3. consultar
    4. salir
    ''')
    opcion = int(input('ingresa opcion: '))
    if opcion == 1:
        print('Inicio de deposito: ')
        print(f'saldo actual: ${SALDO:.2f}')
        valor = float(input('ingresa monto: '))
        SALDO += valor
        print(f'nuevo saldo: ${SALDO:.2f}\n')
    elif opcion == 2:
        print('Inicio de retiro: ')
        print(f'saldo actual: ${SALDO:.2f}')
        valor = float(input('ingrese monto: '))
        if valor <= SALDO:
            SALDO -= valor
            print(f'nuevo saldo: ${SALDO:.2f}\n')
        else:
            print('error, retiro es mayor al saldo en la cuenta\n')
    elif opcion == 3:
        print(f'saldo actual: ${SALDO:.2f}\n')
    elif opcion == 4:
        salir = True
    else:
        print('error de opcion elegida, ingresa valores del MENU\n')
else:
    print('saliste del sistema del cajero')
    print(f'con un saldo: ${SALDO:.2f}')

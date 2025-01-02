# ----- aplicacion calculadora ------------------
'''comentario:
'''
# ----- constante -------------------------------
salir = False
# ----- ciclo -----------------------------------
while not salir:
    print('----- aplicacion calculadora -----')
    print('''Opciones:
    1. suma
    2. resta
    3. multiplicacion
    4. division
    5. salir''')
    operacion = input('ingrese opcion: ')
    if '1' <= operacion <= '4':
        num1 = float(input('ingrese primer valor: '))
        num2 = float(input('ingrese segundo valor: '))

    if operacion == '1':
        print('inicio de suma: ')
#        num1 = float(input('ingrese primer valor: '))
#        num2 = float(input('ingrese segundo valor: '))
        suma = num1 + num2
        print(f'suma: {suma:.2f}')
    elif operacion == '2':
        print('inicio de resta: ')
#        num1 = float(input('ingrese primer valor: '))
#        num2 = float(input('ingrese segundo valor: '))
        resta = num1 - num2
        print(f'resta: {resta:.2f}')
    elif operacion == '3':
        print('inicio de multiplicacion: ')
#        num1 = float(input('ingrese primer valor: '))
#        num2 = float(input('ingrese segundo valor: '))
        mult = num1 * num2
        print(f'multiplicacion: {mult:.2f}')
    elif operacion == '4':
        print('inicio de division: ')
#        num1 = float(input('ingrese primer valor: '))
#        num2 = float(input('ingrese segundo valor: '))
        div = num1 / num2
        print(f'division: {div:.2f}')
    elif operacion == '5':
        salir = True
    else:
        print('opcion invalida')
else:
    print('saliste de calculadora')

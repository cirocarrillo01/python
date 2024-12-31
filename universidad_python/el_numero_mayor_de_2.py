# ----- el mayor de 2 numeros ----------
'''comentario:
'''
# ----- constantes ---------------------

# ----- comando entrada de datos -------
print('ingrese numeros para compararlos')
num1 = int(input('ingrese primer valor: '))
num2 = int(input('ingrese segundo valor: '))
# ----- comando operacion de datos -----
if num1 > num2:
    comparacion = f'el primer valor es mayor, {num1}'
elif num1 == num2:
    comparacion = f'son iguales, los dos son {num1}'
else:
    comparacion = f'el segundo valor es mayor, {num2}'
# ----- comando salida de datos --------
print()
print(f'cual es el numero mayor: {comparacion}')

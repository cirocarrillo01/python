# operadores de asignacion
print('----- operadores de asignacion -----')
numero = 5
print(f'valor de numero: {numero}')
numero = 10
print(f'numero: {numero}')
cadena = 'saludos desde python'
print(f'valor de la cadena: {cadena}')

# operadores de asignacion multiple
x, y, z = 5,'hola',-9.15
print(f'valor de: x = {x}, y = {y} y z = {z}')

# asignacion encadenada.
a = b = c = 10
print(f'valor: a = {a}, b = {b} y c = {c}')

# intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'valores iniciales de x={x} y y={y}')
# aplicando el conceptio de asignacion multiple intercanbiamos valores
x,y = y,x
print(f'valores invertidos: x = {x}, y = {y}')


#recibir multiples valores de la entrada del usuario
nombre, apellido = input('ingresa tu nombre y apellido separado por una \',\' : ').split(',')
print(f'nombre es: {nombre.strip()} y apellidos es: {apellido.strip()}')

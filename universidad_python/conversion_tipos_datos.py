# conversion de tipos de datos

# convetir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'numero es: {numero_entero}')
print(type(numero_entero))

# convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'numero flotante: {numero_flotante}')
print(type(numero_flotante))

# convertir un numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'numero a cadena: {numero_cadena}')
print(type(numero_cadena))

# convertir a booleano
# tipo bool es Falso en los siguientes casos
# si el valor es 0, cadena vacia, o None, entonces regresa False
# resgresa True, si el valor es distinto de 0, si es distinto de cadena vacia
# y tambien si es distinto de None
numero_entero = 0
booleano = bool(numero_entero)
print(f'valor booleano de 0: {booleano}') # False, incluye 0, 0.0

numero_entero = 5
booleano = bool(numero_entero)
print(f'valor booleano de 5: {booleano}') # True

cadena = ''# el largo de cadena es 0,
booleano = bool(cadena)
print(f'valor booleano de cadena vacia: {booleano}') # Falso, incluye colecciones vacias

cadena = 'tiene un valor'
booleano = bool(cadena)
print(f'valor booleano de cadena NO vacia: {booleano}') # True

variable = None
booleano = bool(variable)
print(f'valor booleano de None: {booleano}') # False


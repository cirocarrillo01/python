#operadores de asignacion compuestos
print('--- operadores de asignacion compuestos ---')
a, b = 10,15
print(f'valor inicial a: {a}, b: {b}')

# operador compuesto de suma +=
a += b # a = a+b
print(f'operador a += b es: {a}')

# operador compuesto de resta -=
a = 10 # reiniciamos la variable a
a -= b # a = a - b
print(f'operador a -= b es: {a}')

# operadores compuestos de multiplicacion
a = 10 # reiniciamos el valor de a
a *= b
print(f'operador a *= b es: {a}')

# operador compuesto de division /=
a = 10 # reiniciamos el valor de a
a /= b #a = a / b
print(f'operador a /= b es: {a:.2f}')

# ------- valor dentro de un rango ---------
'''comentario:

'''
# ---------------- constantes ----------------
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

# ------- comando de entrada de datos -------
dato = int(input(f'ingrese un dato entre {VALOR_MINIMO} y {VALOR_MAXIMO}: ').strip())

# ------- comandos de operacion de datos ------
comparacion = 0 <= dato and dato <= 5
#comparacion = 0 <= dato <= 5

# ------- comando de salida de datos ---------
print(f'el dato esta entre (0 y 5): {comparacion}')
#print('verdadero'if comparacion else 'falso')
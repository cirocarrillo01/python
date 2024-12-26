# ---------- calcula el area y el perimetro de un rectangulo ----------
'''comentario:

'''
# ---------------- constantes -----------------

# ----------- comandos de entrada de datos ----------
print('------- calculadora de area y perimetro -------')
altura = float(input('ingrese altura del rectangulo: ').strip())
base = float(input('ingrese la base del rectangulo: ').strip())

# ----------- comandos de operacion de datos -----------
area = altura * base
perimetro = 2 *(altura + base)

# ----------- comandos de salida de datos ------------
print(f'el area del rectangulo es: {area}')
print(f'el perimetro del rectangulo es: {perimetro}')


# -------- reserva de hotel -----------
'''comentario:
'''
# -------- constantes -----------------
SIN_VISTA = 150.50
CON_VISTA = 190.50
# -------- comando entrada datos ------
nombre = input('ingrese nombre de cliente: ').lower().strip()
dias = float(input('ingrese dias de estadia: ').lower().strip())
cuarto = input('con vista al mar (SI/NO): ').lower().strip()
# -------- comando operacion datos ----
if cuarto == 'si':
    estadia = CON_VISTA * dias
else:
    estadia = SIN_VISTA * dias
# -------- comando salidad datos ------
print()
print(f'nombre de cliente: {nombre}')
print(f'dias de estadia: {int(dias)}')
print(f'cuarto con vista al mar: {cuarto}')
print(f'valor de estadia: ${estadia:.2f}')


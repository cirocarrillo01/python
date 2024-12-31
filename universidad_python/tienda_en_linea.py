#-------- tienda en linea ------------------------
'''comentario:


'''
# -------- constantes ----------------------------
COMPRA = 1000

# -------- comando de entradad de datos ----------
print('----- tienda en linea ------')
compra = float(input('ingrese el valor de la compra: '))
miembro = input('eres miembro de la tienda (SI/NO): ').lower()

# -------- comando de operacion de datos ---------
print()
if compra >= COMPRA and miembro == 'si':
    print('felicidades, has obtenido un descuento del 10%')
    descuento = 10
elif compra != COMPRA and miembro == 'si':
    print('felicidades, has obtenido un descuento del 5%')
    descuento = 5
elif compra >= COMPRA and miembro == 'no':
    print('felicidades, has obtenido un descuento del 5%')
    descuento = 5
else:
    descuento = 0
    print('tu descuento es del 0%')
    print('lo invitamos a ser miembro de la tiendad')
descuento = compra * descuento / 100    
descuento_final = compra - descuento

# -------- comanado de salidad -------------------
print(f'Monto de compra: ${compra:.2f}')
print(f'Monto de descuento: ${descuento:.2f}')
print(f'Monto final de la compra con descuento: ${descuento_final:.2f}')
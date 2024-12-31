#---------- aplicacion de salud y fitness ----------
'''comentario:

'''
# --------- constantes -----------------------------
META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO= 0.04

# --------- comando de entradad de datos ----------
nombre_del_usuario = input('ingrese nombre de usuario: ')
pasos_caminados = int(input('pasos caminados en el dia: '))

# --------- comando de operacion de datos --------
calorias_quemadas = pasos_caminados * CALORIAS_POR_PASO
meta_alcanzada = pasos_caminados >= META_PASOS_DIARIO
meta_alcanzada_txt = 'si' if meta_alcanzada else 'no'

# --------- comando de salidad de datos -----------
print()
print(f'usuario: {nombre_del_usuario}')
print(f'pasos dados en el dia: {pasos_caminados} pasos')
print(f'El usuario quemo: {calorias_quemadas:.2f} calorias')
print(f'meta de pasos diarios es: {META_PASOS_DIARIO} pasos')
#print(f'cumplio la meta' if meta_alcanzada else 'no cumplio la meta')
print(f'meta de pasos diarios alcanzada: {meta_alcanzada_txt}')


# --------- fin -----------------------------------
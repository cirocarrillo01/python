#------- sistema de envios -----------------
''' comanetario:
'''
# ----- constantes -------------------------
NACIONAL = 10
INTERNACIONAL = 20
# ----- comandos entrada datos -------------
destino = (input('el destino es (naciona o internacional): ').lower().strip())
peso = float(input('ingrese peso del paquete (kg): ').strip())
# ----- comando operacion datos ------------
costo = None
if destino == 'nacional':
    costo = peso * NACIONAL
elif destino == 'internacional':
    costo = peso * INTERNACIONAL
else:
    print('Destino no valido, ingresa el valor nacional o internacional')
# ----- comando salida datos ---------------
print()
if costo is not None:
    print(f'El costo de envio {destino} del paquete de {peso}kg es: ${costo:.2f}')

# --------- sistema bancario -------
print('----- bienvenido al sistema bancario ------')

salir_sistema_txt = input('Deseas salir del sistema (SI/NO): ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('continuamos dentro del sistema')
else:
    print('salimos del sistema')

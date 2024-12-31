# ----- sistema de autentificacion ------------------
'''
'''
# ----- constantes ----------------------------------
USUARIO = 'ciro123'
PASSWORD = 'ciro321'

# ----- comando entrada datos -----------------------
usuario = input('ingrese usuario: ')
password = input('ingrese password: ')
# ----- comando operacion datos ---------------------
if usuario == USUARIO and password == PASSWORD:
#    mensaje = 'bienvenido al sistema'
    print('bienvenido al sistema')
elif usuario != USUARIO and password == PASSWORD:
#    mensaje = 'usuario invalido'
    print('usuario invalido')
elif usuario == USUARIO and password != PASSWORD:
#    mensaje = 'password invalido'
    print('password invalido')
else:
#    mensaje = 'ususario y password invalidos'
    print('ususario y password invalidos')
# ----- comando salida datos ------------------------
#print(mensaje)

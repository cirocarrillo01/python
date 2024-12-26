#------- sistema de autentificacion -------
""" comentario:
"""
#---------- datos de constantes --------------------
USUARIO = 'ciro'
PASSWORD = 'ciro123'
#---------- comandos de entrada de datos ----------
print('----- sistema de autentificacion -----')
usuario = input('ingrese nombre de ususario: ').lower().strip()
password = input('ingrese contraseña de usuario: ').lower().strip()
#---------- comandos de operaciones de datos ----------
ingreso = usuario == USUARIO and password == PASSWORD
#---------- comanddo de salida de datos -----------
print(f'datos son: {ingreso}')
"""print("Ingresaste" if ingreso else "No ingresaste")
mensajes = {True: "Ingresaste", False: "No ingresaste"}
print(mensajes[ingreso])"""



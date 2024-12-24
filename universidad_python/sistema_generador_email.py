#---------- sistema generador de email ----------


#---------- ingresar datos ----------
print('---------- Sistema Generador de Email ----------')
var_nombre = input('Ingresar los nombres: ')
var_apellido = input('Ingresar apellidos: ')
var_empresa = input('Nombre de la empresa: ')
var_dominio = input('Ingresa dominio de tu emprese(ejemplo: .com.co): ')
#---------- formular datos ----------
print()

var_nombre_1 = var_nombre.strip().lower()
var_apellido_1 = var_apellido.strip().lower()
var_nombres = var_nombre_1.replace(' ','.')+'.'+var_apellido_1.replace(' ','.')

var_empresa_1 = var_empresa.strip().replace(' ','').lower()
var_dominio_1 = var_dominio.strip().replace(' ','.').lower()

email = f'{var_nombres}@{var_empresa_1}.{var_dominio_1}'
#---------- mostrar datos ----------
print()
print(f'''
Tu nuevo email generado por el sistema es:
    {email}
    Felicidades!''')




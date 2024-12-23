#--------------- generador de email ---------------
#------------------ variables ---------------------
nombre_usuario = ' Ciro Carrillo Mendoza '
empresa = 'Goblal Mentoring'
dominio = '.com.mx'
#------------------- formulas ---------------------
val = nombre_usuario.lower().strip()
val1 =val.replace(' ','.')
val2 = '@'+empresa.lower().replace(' ','')+dominio
#------------------- pantalla ---------------------
print('----- generador de email -----')
print(f'Nombre usuario: {val}')
print(f'Nombre usuario normalizado: {val1}')
print('')
print(f'Nombre de empresa: {empresa}')
print(f'Extension del dominio: {dominio}')
print(f'Dominion de email normalizado: {val2}')
print('')
print(f'Email final generado: {val1}{val2}')
#--------------------- fin ------------------------
# ------ sistema de calificacion -------------------
'''comentario: 
'''
# ------ constantes --------------------------------



# ------ comando ingreso datos ---------------------
mensaje='''calificacion:
A: igual a 10
A: igual o mayor a 9
B: menor a 9
B: igual o mayor a 8
C: menor a 8
C: igual o mayor a 7
D: menor a 7
D: igual o mayor a 6
F: menor a 6
F: igual o mayor 0
'''
print('----- sistema de calificacion -----')
#print(mensaje)
calificacion = float(input('ingese calificacion de (0 - 10): '))

# ------ comando opracion datos --------------------
if 10 >= calificacion >= 9:
    nota = 'A'
elif 9 > calificacion >= 8:
    nota = 'B'
elif 8 > calificacion >= 7:
    nota = 'C'
elif 7 > calificacion >= 6:
    nota = 'D'
elif 6 > calificacion >= 0:
    nota = 'F'
else:
    nota = 'valor desconocido'
# ------ comando salida datos ----------------------
print()
print(f'su calificacion {calificacion} es: {nota}')


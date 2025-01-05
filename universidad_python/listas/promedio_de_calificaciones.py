# ----- promedio de calificaciones ------------------------

# ----- ingreso de datos --------------------------
print('----- promedio de calificaciones -----')
calificacion = int(input('numero de calificaciones: '))
lista_notas = []
# ----- ciclos ------------------------------------
for indice in range(calificacion):
    nota = float(input(f'ingresa la nota [{indice +1}]: '))
    lista_notas.append(nota)

#imprimimos las calificaciones proporcionadas
print(f'\nlas calificaciones proporcionada son: {lista_notas}')

# calculamos el promedio de las calificaciones
# sum(iterable)
suma_notas = sum(lista_notas)
promedio = suma_notas/calificacion
print(f'\npromedio de las calificaciones: {promedio:.2f}')

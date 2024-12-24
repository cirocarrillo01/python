#----------------------------------
print('---- Sistema de Empleado ----')
nombre_empleado = input('Nombre del Empleado: ')
edad_empleado = int(input('Edad del Empleado: '))
salario_empleado = float(input('salraio del empleado: '))
es_jefe_departamento = input('¿es jefe de departamento (Si/No?) ')


#vamos a convertir a un numero bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

# imprimir los valores del empleado
print('\nDatos del empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')

print(f'Es jefe de departamento? {es_jefe_departamento}')
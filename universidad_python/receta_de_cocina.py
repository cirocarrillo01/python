#-------------- receta de cocina -------------
#------------------ entradas -----------------
print('---------- Receta de Cocina ----------')
var_nombre = input('ingrese el nombre del plato: ')
var_ingredientes = input('ingrese los ingredientes del plato: ')
var_tiempo = int(input('ingrese el tiempo preparacion(min): '))
var_dificultad = input('ingresa la dificultad: facil, medio o dificil: ')

#------------------- salida --------------------
print()
print('---------- Receta de Cocina ----------')
print(f'Nombre receta: {var_nombre}')
print(f'Ingredientes: {var_ingredientes}')
print(f'Tiempo de preparacion: {var_tiempo}')
print(f'Dificultad: {var_dificultad}')


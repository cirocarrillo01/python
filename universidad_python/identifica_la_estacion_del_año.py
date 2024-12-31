# ----- identifica la estacion del año -----
'''comentario:
'''
# ----- constantes -------------------------

# ----- comando ingresos datos -------------
print('identifica la estacion del año')
estacion = int(input('ingresa un mes del año (1 - 12): ').lower().strip())
estacion1 = None
# ----- comando operacion datos ------------
if estacion == 1 or estacion == 2 or estacion == 12:
    estacion1 = 'invierno'
elif estacion == 3 or estacion == 4 or estacion == 5:
    estacion1 = 'primavera'
elif estacion == 6 or estacion == 7 or estacion == 8:
    estacion1 = 'verano'
elif estacion == 9 or estacion == 10 or estacion == 11:
    estacion1 = 'otoño'
else:
    estacion1 = 'desconocida'
# ----- comando salidad datos --------------
print()
print(f'El mes {estacion} la estacion es {estacion1}')




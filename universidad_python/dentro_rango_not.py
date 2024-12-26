# revisar si una variable se encuantra dentro de rango entre 1 y 10
dato = int(input('proporciona un dato entero: '))

# revisamos si esta dentro de rango
#esta_dentro_rango = 1 <= dato <= 10
#print(f'Variable esta dentro de rango (entre 1 y 10)?: {esta_dentro_rango}')

# revisamos la logica inversa, si el dato esta fuera de rango
esta_fuera_rango = not(1 <= dato <= 10)
print(f'esta fuera de rango (entre 1 y 10)?: {esta_fuera_rango}')

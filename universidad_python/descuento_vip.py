print('----- Sistema de Descuento -----')
NO_PRODUCTOS_DESCUENTOS = 10
cantidad_productos = int(input('cuantos productos comprastes hoy?: '))
tienes_menbresia = input('Tienes la menbresia de la tienda (SI/NO)?: ').lower().strip()
es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTOS
                         and tienes_menbresia == 'si')
print(f'Tienes acceso al descuento VIP?: {es_elegible_descuento}')
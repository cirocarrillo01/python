#----- ticket venta ---------
print('----- generacion ticket de venta ------')

precio_leche = float(input('precio de leche: '))
precio_pan = float(input('precio de pan: '))
precio_lechuga = float(input('precio lechuga: '))
precio_platano = float(input('precio platano: '))
descuento_porcentaje = int(input('Aplicar algun descuento (%)? '))

# calculo del subtotal (sin impuesto)
sub_total = precio_pan+precio_platano+precio_leche+precio_lechuga

# aplicar el descuento
descuento = sub_total * (descuento_porcentaje/100)

#subtotal con descuento
sub_total_con_descuento = sub_total - descuento

#calculo con impuesto(16%)
impuesto = sub_total * 0.16

# calculo total de la compra (con impuestos)
costo_total_compra = sub_total_con_descuento + impuesto
print(f'''
subtotal: ${sub_total:.2f}
descuento: ${descuento} ({descuento_porcentaje}%)
subtotal con descuento: ${sub_total_con_descuento}
impuesto(16%): ${impuesto}
costo total de la compra: ${costo_total_compra}
''')


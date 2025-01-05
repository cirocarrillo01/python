print('cominacion de lista y tuplas')

# definir una lista que almacene tuplas de productos

productos = [
    ('p001', 'camiseta', 20.00),
    ('p002', 'jeans', 30.00),
    ('p003', 'sudadera', 40.00)
]
# imprimir la informacion de cada producto
# y ademas calculamos el precio total
precio_total = 0

print('informacion de los productos: ')
for producto in productos:
    #print(producto)
    id, descripcion, precio = producto#unpaking
    print(f'producto: id = {id}, descripcion = {descripcion}, precio = ${precio}')
    precio_total += precio #producto[2]

print(f'precio total: ${precio_total}')
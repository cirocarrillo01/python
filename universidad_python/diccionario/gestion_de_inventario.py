# ----- gestion de inventario ------------------------
print(' ----- gestion de inventario ----- ')
inventario =[ ]
ingreso = int(input('cuantos productos deseas agregar al inventario: '))
for indice in range(ingreso):
    print(f'proporcione los valores del producto {indice+1}')
    nombre = input('Nombre: ')
    precio = float(input('precio: '))
    cantidad = int(input('cantidad: '))
    # creamos el diccionario con el detalle del producto
    producto = {'id': indice+1, 'nombre': nombre, 'precio':precio, 'cantidad':cantidad}
    # agregamos un nuevo producto
    inventario.append(producto)

# mostrar el inventario inicial
print(f'\ninventario inicial: {inventario}')

# buscar un producto por id
id_buscar = int(input('\nIngresa el ID del producto a buscar: '))
producto_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break
if producto_encontrado is not None:
    print('informacion del producto encontrado: ')
    print(f'''id: {producto_encontrado.get('id')}
    nombre: {producto_encontrado.get('nombre')}
    precio: {producto_encontrado.get('precio')}
    cantidad: {producto_encontrado.get('cantidad')}''')

else:
    print(f'producto con id {id_buscar} no encontrado')

# mostrar el inventario detallado
print(f'\n--- inventario detallado ---')
for producto in inventario:
    print(f'''id: {producto.get('id')}
    nombre: {producto.get('nombre')}
    precio: {producto.get('precio')}
    cantidad: {producto.get('cantidad')}''')

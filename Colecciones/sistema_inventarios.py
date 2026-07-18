print('*** Sistema de Inventarios ***')

inventario = []
cantidad_productos = int(input('Ingrese la cantidad de productos que desea agregar: '))

for indice in range(cantidad_productos):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = input('Ingrese el nombre del producto que desea agregar: ')
    precio = float(input('Ingrese el precio: '))
    cantidad = int(input('Ingrese la cantidad: '))

    producto = {
        'id': indice,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad,
    }
    inventario.append(producto)

print(f'Inventario inicial: {inventario}')

# Buscar producto por id
id_producto_buscar = int(input('Ingrese el id del producto que desea buscar: '))
producto_encontrado = None

for producto in inventario:
    if producto.get('id') == id_producto_buscar:
        producto_encontrado = producto
        break
if producto_encontrado is not None:
    print('\n--- Detalle del Producto buscado ---')
    print(f'''Id: {producto_encontrado.get("id")}
    Nombre: {producto_encontrado.get("nombre")}
    Precio: {producto_encontrado.get("precio")}
    Cantidad: {producto_encontrado.get("cantidad")}''')
else:
    print(f'Producto con id {id_producto_buscar} no encontrado')

print('\n--- Inventario Detallado Actualizado ---')
for detalle in inventario:
    print(f'''Id {detalle.get("id")}: 
    Nombre: {detalle.get('nombre')},
    Precio: {detalle.get('precio')},
    Cantidad: {detalle.get('cantidad')}
''')

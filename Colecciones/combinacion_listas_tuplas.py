print('*** Listas y Tuplas ***')

# Definir una lista que almacena tuplas de productos
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00),
]

# Imprimir la información de cada producto y calcular el precio final
precio_total = 0

print('Información de los productos: ')
for producto in productos:
    #print(producto)
    id, descripcion, precio = producto
    print(f'Producto: id: {id}, descripción: {descripcion}, precio: $ {precio}')
    precio_total += precio
    # tambien puede ser
    # precio_total += producto[2]

print(f'Precio total de los productos: $ {precio_total}')

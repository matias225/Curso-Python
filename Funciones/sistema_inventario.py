from os import name

print('*** Sistema de inventario (con funciones) ***')

inventario = [
    {"id": 1, "nombre": "Camisa", "precio": 25.99, "cantidad": 50},
    {"id": 2, "nombre": "Pantalones", "precio": 39.99, "cantidad": 30},
    {"id": 3, "nombre": "Zapatos", "precio": 49.99, "cantidad": 20},
]
opcion = 0

def menu():
    print('''--- Menu ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por Id
        4. Salir
    ''')
    opcion = int(input('Proporciona una opcion (1-4): '))
    return opcion

def mostrar_inventario():
    print('\n*** Inventario ***')
    for producto in inventario:
        print(f'Id: {producto['id']}')
        print(f'Nombre: {producto["nombre"]}')
        print(f'Precio: $ {producto["precio"]}')
        print(f'Cantidad: {producto["cantidad"]}\n')

def agregar_producto(id_agregar):
    print('\n*** Agregar producto ***')
    nombre = input('Ingrese el nombre del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad de producto: '))
    nuevo_producto = {
        "id": id_agregar,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(nuevo_producto)
    print('\nProducto agregado con exito\n')
    return

def buscar_producto(id):
    print('\n*** Buscar producto ***')
    for producto in inventario:
        if producto["id"] == id:
            print('Informacion del producto encontrado: ')
            print(f'Id: {producto["id"]}, Nombre: {producto["nombre"]}, Precio: $ {producto["precio"]}, '
                  f'Cantidad: {producto["cantidad"]}\n')
            return
    print(f'No se encontro producto con el id: {id}\n')
    # Este return es opcional en python, ya que agrega uno al final de cualquier funcion
    return

# Programa principal
if __name__ == '__main__':
    while opcion != 4:
        opcion = menu()
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            id_agregar = int(input('Ingrese el id del producto a agregar: '))
            for producto in inventario:
                if producto["id"] == id_agregar:
                    print('Id ya existente, utilice otro id\n')
                    break
            else: # el else en un for, solo existe en python, se ejecuta cuando termina el ciclo sin un break
                agregar_producto(id_agregar)
        elif opcion == 3:
            id_buscar = int(input('Ingrese el id del producto a buscar: '))
            buscar_producto(id_buscar)
        elif opcion == 4:
            print('Saliendo...')
            break
        else:
            print('Opcion invalida. Proporciona una opcion valida.\n')

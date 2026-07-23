print('*** Máquina de Snacks ***')

# Lista de snacks
snacks = [
    {'id':1, 'nombre':'Caramelos', 'precio': 40.00},
    {'id':2, 'nombre':'Papas', 'precio': 59.99},
    {'id':3, 'nombre':'Sandwich', 'precio': 70.50}
]

productos = []

def menu():
    print('''Menú:
        1. Mostrar Snacks
        2. Comprar Snack
        3. Mostrar ticket
        4. Salir''')

def mostrar_snacks():
    print('--- Snacks Disponibles ---')
    for snack in snacks:
        print(f'Id: {snack["id"]} -> {snack.get('nombre')} - ${snack.get("precio")}')

def buscar_por_id(id_buscar):
    for snack in snacks:
        if snack['id'] == id_buscar:
            return snack
    return None

def comprar_snack():
    id = int(input('Que snack quieres comprar? (id): '))
    snack_encontrado = buscar_por_id(id)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}\n')
    else:
        print(f'Snack no disponible con el id:2 {id}')

def mostrar_ticket():
    ticket = f'\t--- Ticket de Compra ---'
    total = 0
    for item in productos:
        ticket += f'\n\t- {item.get("nombre")} - ${item.get("precio")}'
        total += item.get("precio")
    ticket += f'\n\tTOTAL -> ${total:.2f}\n'
    print(ticket)

# Programa principal
if __name__ == '__main__':
    while True:
        menu()
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Saliendo...')
            break
        else:
            print('Opción inválida. Seleccione otra opción')

print('*** Sistema de Administración de cuentas ***')

salir = False
opcion = 0

while not salir:
    print('''Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    opcion = int(input('Ingrese su opcion: '))

    if opcion == 1:
        print('Creando cuenta...\n')
    elif opcion == 2:
        print('\nEliminar cuenta')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto.')
        salir = True
    else:
        print('Opcion invalida. Proporciona otra opcion...')

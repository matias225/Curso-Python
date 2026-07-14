print('*** Aplicación de Cajero Automático ***')

saldo = 0.00
deposito = 0
retiro = 0
opcion = 0
salir = False

while not salir:
    print('''Operaciones que puedes realizar:
    1. Consultar saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Seleccione la opción: '))

    if opcion == 1:
        print('Consultando saldo...')
        print(f'Tu nuevo saldo es: $ {saldo:.2f}\n')
    elif opcion == 2:
        print('Retirar')
        retiro = float(input('Ingrese el monto que desea retirar: '))
        if retiro <= saldo:
            saldo -= retiro
            print(f'Tu nuevo saldo es: $ {saldo:.2f}')
        else:
            print(f'Saldo insuficiente. saldo actual: $ {saldo:.2f}\n')
    elif opcion == 3:
        print('Depositar')
        deposito = float(input('Ingrese el monto que desea depositar: '))
        saldo += deposito
        print(f'Tu nuevo saldo es: $ {saldo:.2f}\n')
    elif opcion == 4:
        print('Saliendo del cajero automatico. Hasta pronto!')
        salir = True
    else:
        print('Opción invalida. Selecciona otra opción.')
print('*** Calculadora en Python ***')

salir = False
opcion = 0

while not salir:
    print('''Opearciones que puede realizar:
        1. Suma
        2. Resta
        3. Multiplicar
        4. División
        5. Salir
    ''')
    opcion = int(input('Escoja una opción: '))

    if opcion == 1:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))
        resultado = num1 + num2
        print(f'El resultado de la suma {num1} + {num2} es: {resultado}\n')
    elif opcion == 2:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))
        resultado = num1 - num2
        print(f'El resultado de la resta {num1} - {num2} es: {resultado}\n')
    elif opcion == 3:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))
        resultado = num1 * num2
        print(f'El resultado de la multiplicación {num1} * {num2} es: {resultado}\n')
    elif opcion == 4:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))
        resultado = num1 / num2
        print(f'El resultado de la división {num1} / {num2} es: {resultado}\n')
    elif opcion == 5:
        print('Saliendo...')
        salir = True
    else:
        print('Opción invalida. Proporciona un número válido\n')
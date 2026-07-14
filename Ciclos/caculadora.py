print('*** Calculadora en Python ***')

salir = False
opcion = resultado = num1 = num2 = 0

while not salir:
    print('''Opearciones que puede realizar:
        1. Suma
        2. Resta
        3. Multiplicar
        4. División
        5. Salir
    ''')
    opcion = int(input('Escoja una opción: '))
    if 1 <= opcion <= 4:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))

    if opcion == 1:
        resultado = num1 + num2
        print(f'El resultado de la suma es: {resultado:.2f}\n')
    elif opcion == 2:
        resultado = num1 - num2
        print(f'El resultado de la resta es: {resultado:.2f}\n')
    elif opcion == 3:
        resultado = num1 * num2
        print(f'El resultado de la multiplicación es: {resultado:.2f}\n')
    elif opcion == 4:
        resultado = num1 / num2
        print(f'El resultado de la división es: {resultado:.2f}\n')
    elif opcion == 5:
        print('Saliendo...')
        salir = True
    else:
        print('Opción invalida. Proporciona un número válido\n')

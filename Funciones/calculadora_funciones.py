print('*** Calculadora con Funciones ***')

def menu():
    print('''Operaciones que puede realizar:
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir
    ''')
    return int(input('Escoja una opcion: '))

def sumar(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def pedir_valores():
    num1 = float(input('Ingrese el primer numero: '))
    num2 = float(input('Ingrese el segundo numero: '))
    return num1, num2

def ejecutar_operacion(opcion, salir):
    if 1 <= opcion <= 4:
        num1, num2 = pedir_valores()
    resultado = 0
    if opcion == 1:
        resultado = sumar(num1, num2)
        print(f'El resultado de la suma es: {resultado:.2f}\n')
    elif opcion == 2:
        resultado = resta(num1, num2)
        print(f'El resultado de la resta es: {resultado:.2f}\n')
    elif opcion == 3:
        resultado = multiplicacion(num1, num2)
        print(f'El resultado de la multiplicacion es: {resultado:.2f}\n')
    elif opcion == 4:
        if num2 == 0:
            print('Division por 0. No es posible calcularlo.\n')
        else:
            resultado = division(num1, num2)
            print(f'El resultado de la division es: {resultado:.2f}\n')
    elif opcion == 5:
        print('Saliendo de la calculadora')
        salir = True
    else:
        print('Opcion invalida.')
    return salir

# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = menu()
        salir = ejecutar_operacion(opcion, salir)

print('*** Convertidor de Temperatura ***')

def celcius_fahrenheit(celcius):
    return celcius * (9 / 5) + 32

def fahrenheit_celcius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

if __name__ == '__main__':
    print('Menu')
    print('1. De Celcius a Fahrenheit')
    print('2. De Fahrenheit a Celcius')
    print('3. Salir')
    opcion = int(input('Ingrese que conversion quiere realizar: '))
    if 1 <= opcion <= 2:
        temp = float(input('Ingresa el valor de la temperatura: '))
    if opcion == 1:
        print(f'La temperatura {temp} en Fahrenheit es: {celcius_fahrenheit(temp):.2f}')
    elif opcion == 2:
        print(f'La temperatura {temp} en Celcius es: {fahrenheit_celcius(temp):.2f}')
    elif opcion == 3:
        print('Saliendo...')
    else:
        print('Opcion no valida.')

print('*** Función Par ***')

# Función para saber si un número es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    numero = int(input('Ingrese un numero: '))
    print(f'¿Es par?: {es_par(numero)}')

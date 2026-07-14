print('*** Repetición de un Mensaje ***')

mensaje = input('Ingrese un mensaje a repetir: ')
numero_de_repeticiones = int(input('Ingrese el número de repeticiones: '))

for _ in range(numero_de_repeticiones):
    print(mensaje)

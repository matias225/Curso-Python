print('*** Suma Acumulativa ***')

# Sumar los primeros 5 números
MAXIMO = 5
numero = 1
acumulador_suma = 0

while numero <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f'acumulador_suma + numero -> {acumulador_suma} + {numero}')
    acumulador_suma += numero
    numero += 1
    print(f'Suma parcial acumulada: {acumulador_suma}\n')

print(f'Resultado de la suma acumulada: {acumulador_suma}')
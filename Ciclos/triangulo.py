print('*** Dibujar Triángulo Simétrico ***')

numero_filas = int(input('Proporcione el numero de filas: '))

for fila in range(1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila)
    asterisco = '*' * (2 * fila - 1)
    print(espacios_blanco + asterisco)

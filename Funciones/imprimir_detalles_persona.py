print('*** Imprimir detalles de una persona usando kwargs ***')

# Función que acepta argumentos variables en forma de dict
def imprimir_detalles_persona(**kwargs):
    print('\nValores obtenidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

# Llamamos a la función
imprimir_detalles_persona(nombre='Matias Romani', edad=33, ciudad='San Rafael')
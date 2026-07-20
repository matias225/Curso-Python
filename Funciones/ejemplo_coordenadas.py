print('*** Obtener coordenadas x, y, z ***')

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z

# Llamar la función
resultado = obtener_coordenadas()
print(resultado)

# Unpacking de la tupla
x1, y1, z1 = obtener_coordenadas()
print(f'Coordenada x = {x1}, y = {y1}, z = {z1}')

print('*** Validación Campo de un Formulario ***')

nombre_usuario = None

while not nombre_usuario:
    nombre_usuario = input('Introduce tu nombre del usuario: ')

print(f'Nombre de usuario válido: {nombre_usuario}')
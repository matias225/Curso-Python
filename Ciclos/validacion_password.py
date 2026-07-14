print('*** Creación y Validación de un Password ***')

password = input('Ingrese un password (debe tener al menos 6 caracteres): ')

while len(password) < 6:
    print('El password debe tener al menos 6 caracteres')
    password = input('Ingrese un nuevo password: ')
else:
    print('El valor del password es válido')

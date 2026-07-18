print('*** Agenda de contactos ***')

agenda = {
    'Matias': {
        'telefono': '334221232',
        'email': 'matias@gmail.com',
        'direccion': 'Calle Verde 332'
    },
    'Carlos': {
        'telefono': '559221232',
        'email': 'carlos@gmail.com',
        'direccion': 'Calle Principal 132'
    },
    'Maria': {
        'telefono': '665221232',
        'email': 'maria@gmail.com',
        'direccion': 'Avenida Central 456'
    },
    'Pedro': {
        'telefono': '445221232',
        'email': 'pedro@gmail.com',
        'direccion': 'Plaza Mayor 789'
    }
}
print(agenda)

# Acceder a la información de un contacto en específico
print(f'''Información del contacto de Maria:
    Telefono: {agenda['Maria']['telefono']}
    Email: {agenda.get('Maria').get('email')}
    Direccion: {agenda['Maria']['direccion']}''')

# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '334221232',
    'email': 'ana@gmail.com',
    'direccion': 'San Martin 532'
}

print(agenda)

# Eliminar un contacto existente
agenda.pop('Pedro')
# o tambien
# del agenda['Pedro']

print(agenda)

# MOstramos los contactos de la agenda
print('\nContactos en la Agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Telefono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}
''')

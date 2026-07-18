from Cadenas.concatenacion_cadenas import apellido

print('*** Combinación de Listas y Diccionarios ***')

personas = [
    {
        'nombre': 'Brisa',
        'apellido': 'Olate',
        'edad': 26
    },
    {
        'nombre': 'Matias',
        'apellido': 'Romani',
        'edad': 33,
    },
    {
        'nombre': 'Santiago',
        'apellido': 'Romani',
        'edad': 25,
    }
]
print(personas)

# Acceder a un diccionario desde una lista
print(f'''Detalle del primer elemento de la lista
Nombre: {personas[0].get('nombre')}
Apellido: {personas[0].get('apellido')}
Edad: {personas[0].get('edad')}''')

# Recorrer los elementos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'Persona - {contador}: {persona}')
    #print(f'Detalle: Nombre: {persona.get("nombre")}, Apellido: {persona.get('apellido')}\n')

print('*** Diccionarios ***')

# Creamos un dict de persona con clave y valor
persona = {
    'nombre': 'Matias',
    'edad': 33,
    'ciudad': 'San Rafael'
}
print(f'Diccionario: {persona}')

# Acceder a los elementos del diccionario
print(f'El nombre es: {persona["nombre"]}')
print(f'La edad es: {persona.get("edad")}')
print(f'La ciudad es: {persona.get("ciudad")}')

# Modificar un valor del diccionario
persona['edad'] = 34
print(f'La edad modificada es: {persona.get("edad")}')

# Agregar un nuevo elemento
persona['profesion'] = 'Ingeniero'
print(f'Diccionario: {persona}')

# Eliminar un elemento
del persona['ciudad']
print(f'Diccionario: {persona}')

persona.pop('profesion')
print(f'Diccionario: {persona}')

# Iterar los elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

# Obtener solo los valores
print('\nObtener los valores del diccionario')
for valor in persona.values():
    print(f'Valores del diccionario: {valor}')

# Obtener solo los valores
print('\nObtener las llaves')
for key in persona.keys():
    print(f'Valores del diccionario: {key}')

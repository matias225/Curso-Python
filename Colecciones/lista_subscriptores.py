print('*** Lista de subscriptores ***')

# Definimos el set inicial
# suscriptores = {} no se define asi porque asi se hacen los diccionarios
suscriptores = set() # Set vacio

numero_subscriptores = int(input('Ingrese el numero de suscriptores iniciales: '))
for _ in range(numero_subscriptores):
    suscriptores.add(input('Ingrese nuevo suscriptor (email): '))

print(f'Lista de suscriptores inicial: {suscriptores}')

# Verifica si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = input('Ingrese el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha añadido a la lista {nuevo_suscriptor}')

print(f'\nLista de suscriptores: {suscriptores}')

# Eliminamos un suscriptor
suscriptor_eliminar = input('Ingrese el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'\nEl suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')

print(f'Lista de suscriptores: {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'Cantidad total de suscriptores: {len(suscriptores)}')

# Mostramos todos los suscriptores
print('---- Lista de suscriptores ----')
for s in suscriptores:
    print(f'- {s}')

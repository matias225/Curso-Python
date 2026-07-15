print('*** Playlist de Canciones ***')

# Creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input("Introduce un número de canciones: "))

# Iteraos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f"Introduce la canción {indice + 1}: ")
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabetico, sort sin nada es ascendente
lista_reproduccion.sort()
# De forma descendente
#lista_reproduccion.sort(reverse=True)

# Mostrar al lista iterando sus elementos
print('\nIteramos el playlist')
for cancion in lista_reproduccion:
    print(f'- {cancion}')

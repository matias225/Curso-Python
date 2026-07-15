print('*** Manejo de Listas ***')

mi_lista = [1,2,3,4,5]
print(f'{mi_lista} -> Lista original')

# Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indices
print(f'Accedemos al valor del índice 4: {mi_lista[4]}')
print(f'Accedemos al último valor de la lista: {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'{mi_lista} -> Modificamos el valor del indice 1: ')

# Agregar un nuevo elemento al final de la lista
mi_lista.append(15)
print(f'{mi_lista} -> Se agregó el elemento 6 al final')

# Agregar un nuevo elemento en un indice especfico
mi_lista.insert(3,22)
print(f'{mi_lista} -> Se agrego el elemento 22 en el indice 3')

# Eliminar elementos de una lista, usando el método remove se pasa el elemento
mi_lista.remove(22)
print(f'{mi_lista} -> Se elimino el elemento 22 con remove')

# Removemos por indice con el metodo pop
mi_lista.pop(5)
print(f'{mi_lista} -> Se elimino el indice 5')

# Eliminamos usando la palabra
del mi_lista[2]
print(f'{mi_lista} -> Se elimino el indice 2')

# Obtener sublistas
sublista = mi_lista[1:3] # genera una lista entre los indices 1 y 2 (el 3 no se incluye)
print(f'{sublista} -> Sublista desde el indice 1 hasta el 2 equivalente a [1:3]')

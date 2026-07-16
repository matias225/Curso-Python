print('*** Manejo de Tuplas ***')
# Los parentesis son opcionales
mi_tupla = 1, 2, 3, 4, 5
print(mi_tupla)

# No podemos modificar una tupla
#mi_tupla[0] = 10
#mi_tupla.append(10)

# Iteramos los elementos de una tupla
for i in mi_tupla:
    print(i, end=' ')

# Crear una tupla para una coordenada x,y
cooordenada = (3, 5)
# Accedemos a cada elemento de la tupla
print(f'\nCoordenada en el eje x: {cooordenada[0]}\nCoordenada en el eje y: {cooordenada[1]}')

# Crear una tupla unitaria colocando la , despues del elemento
tupla_de_un_elemento = 10,
print(f'Tupla de un elemento: {tupla_de_un_elemento}')

# Tupla anidada
tuplas_anidadas = (1, (2,3), (4,5))
print(f'Tupla anidada: {tuplas_anidadas}')
print(f'Segndo elemento de tupla anidada: {tuplas_anidadas[1]}')
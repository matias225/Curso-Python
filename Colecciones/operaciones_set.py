print('*** Operaciones con Set ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# union = a.union(b)
union = a | b
print(f'Unión a | b: {union}')

interseccion = a & b
print(f'Interseccion a & b: {interseccion}')

dierencia = a - b
print(f'Diferencia a - b: {dierencia}')

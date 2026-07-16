print('*** Promedio de Calificaciones ***')

calificaciones = []
promedio_calificaciones = 0

num_calificaciones = int(input('Proporcione el n° de calificaciones a evaluar: '))

for c in range(num_calificaciones):
    calificacion = int(input(f'Ingrese calificacion {c+1}: '))
    calificaciones.append(calificacion)
    # Puedo guardar la sumatoria de la calificacion cada vez que agrego una
    # suma += calificaciones[c]

print(f'Las calificaciones proporcionadas son: {calificaciones}')

# Tambien se puede usar la funcion sum()
promedio_calificaciones = sum(calificaciones) / num_calificaciones

print(f'El promedio de las calificaciones proporcionadas es: {promedio_calificaciones:.2f}')

print('*** Ordenamiento ***')

# sintaxis: sorted(iterable, key=None, reverse=False)

empelados = ['Santiago', 'Matias', 'Brisa']
empleados_ordenados = sorted(empelados)
# Descendente
# empleados_ordenados = sorted(empelados, reverse=True)
print(f'Empleados ordenados: {empleados_ordenados}')

# Ordenar un diccionario (una llave)
empleados_dict = [
    {'nombre': 'Matias', 'salario': 45000},
    {'nombre': 'Santiago', 'salario': 20000},
    {'nombre': 'Brisa', 'salario': 50000}
]

empleados_ordenados_salario = sorted(empleados_dict, key=lambda x: x['salario'], reverse=True)
print(f'Empleados ordenados por salario: {empleados_ordenados_salario}')

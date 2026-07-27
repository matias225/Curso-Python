print('*** Comprensión de Listas ***')

# Filtrar solo los números pares y generar una nueva lista con estos valores

numeros = range(1, 10+1)
# Sin usar comprensión de listas
numeros_pares = []
# Iteramos cada elemento de la lista
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f'Numeros pares del 1 al 10: {numeros_pares}')

# Usar comprensión de listas
# Sintaxis: nueva_lista = [expresion for elemento in iterable if condicion]
numeros_pares_comprension = [numero for numero in numeros if numero % 2 == 0 ]
print(f'Numeros pares del 1 al 10: {numeros_pares_comprension}')

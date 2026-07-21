print('*** Potencia con Funciones recursivas ***')

# Definimos la funcion
def potencia(base,exponente):
    # Caso base
    if exponente == 0:
        return 1
    else: # Caso recursivo
        return base * potencia(base, exponente-1)

print(f'Resultado de 2 elevado a la 3: {potencia(2, 3)}')
print(f'Resultado de 4 elevado a la 6: {potencia(4, 6)}')
print(f'Resultado de 4 elevado a la 5: {potencia(2, 5)}')
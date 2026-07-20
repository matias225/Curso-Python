print('*** Alcance de Variables ***')

# Variable global
contador_global = 0

def incremento_contador():
    # Declaramos una variable local
    contador_local = 0

    # usar la variable global
    global contador_global
    # Incrementamos la variable global
    contador_global += 1

    # incrementamos la variablo local
    contador_local += 1

    # Imprimimos ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# Llamamos varias veces la función
incremento_contador()
incremento_contador()
incremento_contador()

# Terminamos el programa
print(f'Valor de contador global: {contador_global}')

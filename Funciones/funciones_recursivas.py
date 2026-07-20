print('*** Imprimir del 1 al 5 de forma recursiva ***')

# Definir la función recursiva
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' ') # 1 2 3 4 5
    else: # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

# Programa principal
funcion_recursiva(5)

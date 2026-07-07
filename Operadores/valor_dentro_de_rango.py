print("*** Dentro de Rango ***")

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

valor_ingresado = int(input(f"Ingrese el valor de ingresado entre {VALOR_MINIMO} y {VALOR_MAXIMO}: "))

# en_rango = valor_ingresado >= VALOR_MINIMO and valor_ingresado <= VALOR_MAXIMO
# Otra forma de hacerlo es condiciones encadenadas
en_rango = VALOR_MINIMO <= valor_ingresado <= VALOR_MAXIMO

print(f"¿El valor está dentro del rango {VALOR_MINIMO} y {VALOR_MAXIMO}? {en_rango}")

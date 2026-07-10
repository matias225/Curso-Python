print("*** Revisión de Valor Positivo ***")

numero = int(input("Proporciona un número: "))

if numero > 0:
    print(f"Valor positivo: {numero}")
elif numero < 0:
    print(f"Valor negativo: {numero}")
else:
    print(f"El valor es cero.")
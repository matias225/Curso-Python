print('*** Mayor número ***')
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

# Comparamos los números

if num1 > num2:
    print(f"El primer número es mayor: {num1}")
elif num2 > num1:
    print(f"El segundo número es mayor: {num2}")
else:
    print("Los números son iguales")

print("*** Operadores Asignacion Compuestos ***")
a, b = 10, 15
print(f"Valor inicial de a = {a}, b = {b}")

# Operador compuesto de suma +=
a += b  #  seria como a = a + b
print(f"Valor de a += b es: {a}")

# Operador compuesto de resta -=
a = 10 # reiniciamos la variable a
a -= b  # a = a - b
print(f"Valor de a -= b es: {a}")

# Operador compuesto de multiplicacion *=
a = 10 # reiniciamos la variable a
a *= b
print(f"Valor de a *= b es: {a}")

# Operador compuesto de division /=
a = 10
a /= b
print(f"Valor de a /= b es: {a:.3f}")
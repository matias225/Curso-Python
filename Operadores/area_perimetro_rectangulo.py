print("*** Cálculo de área y perímetro de un rectánguloo ***")
base = float(input(f"Ingrese el valor de base: "))
altura = float(input(f"Ingrese el valor de altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"El área del rectángulo de {base}x{altura} es {area} y el perímetro es {perimetro}")
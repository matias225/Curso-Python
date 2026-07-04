# Programa: Entrada datos
nombre = input("Ingrese su nombre: ")
print(f"Tu nombre es: {nombre}")

# Cuidado al trabajar ocn valores numéricos
# Envolver con int() o float() ya que input siempre devuelve un string,
# tambien se puede envolver cuando vayas a hacer la operacion

# Para enteros (edad, cantidad)
edad = input("Tu edad: ")
print(f"Tu edad es: {edad}")
print(int(edad) + 5)

# Para decimales (precio, altura)
altura = float(input("Tu altura: "))
print(f"Tu altura es: {altura}")
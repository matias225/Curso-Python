print("*** Sistema de Empleados ***")
nombre_empleado = input("Ingrese su nombre: ")
edad_empleado = int(input("Ingrese su edad: "))
salario_empleado = float(input("Ingrese su salario: "))
es_jefe_departamento = input("¿Es jefe de departamento (Si/No)?: ")

# Convertir a tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si"

# Imprimir los valores
print("\nDatos del Empleado")
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
# Poniendo ":" el numero de decimales y que es de tipo float con .2f, imprimimos 2 decimales
print(f"Salario: {salario_empleado:.2f}")
print(f"¿Es jefe de departamento?: {es_jefe_departamento}")
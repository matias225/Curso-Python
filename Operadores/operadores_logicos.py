print(f"*** Operador and ***")
# Regresa verdadero si ambos valores a evaluar son verdaderos
condicion1 = True
condicion2 = True
resultado = condicion1 and condicion2
print(f"Resultado {condicion1} and {condicion2}: {resultado}")
condicion1 = False
condicion2 = True
resultado = condicion1 and condicion2
print(f"Resultado {condicion1} and {condicion2}: {resultado}")
condicion1 = False
condicion2 = False
resultado = condicion1 and condicion2
print(f"Resultado {condicion1} and {condicion2}: {resultado}")

print(f"\n*** Operador or ***")
# Regresa verdadero si cualquiera de los operandos es verdadero
condicion1 = False
condicion2 = False
resultado = condicion1 or condicion2
print(f"Resultado {condicion1} or {condicion2}: {resultado}")
condicion1 = False
condicion2 = True
resultado = condicion1 or condicion2
print(f"Resultado {condicion1} or {condicion2}: {resultado}")
condicion1 = True
condicion2 = True
resultado = condicion1 or condicion2
print(f"Resultado {condicion1} or {condicion2}: {resultado}")

print(f"\n*** Operador not ***")
condicion1 = False
resultado = not condicion1
print(f"Resultado not {condicion1}: {resultado}")
condicion1 = True
resultado = not condicion1
print(f"Resultado not {condicion1}: {resultado}")

# Ejemplos NOT
# Revisar si una variable es cadena vacia
nombre = ""
es_cadena_vacia = not nombre
print(f"La variable no tiene valor: {es_cadena_vacia}")

# Revisar si una variable no tiene ningun valor asignado
variable = None
es_variable_sin_valor = not variable
print(f"La variable no tiene ningun valor asignado: {es_variable_sin_valor}")
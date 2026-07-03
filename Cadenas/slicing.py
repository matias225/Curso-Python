# Programa: Aplicar el concepto de slicing
texto = "Matias Romani"

# Por defecto el paso es 1
nombre = texto[0:6]
apellido = texto[7:13]

print(nombre)
print(apellido)
print(texto)

# Se puede contar desde atras con indices negativos, atajo hasta el final
apellido = texto[:-6]
print(apellido)
print()
texto1 = "PROGRAMACION"
# 1. Básico [inicio:fin]
print(texto1)
print(texto1[0:4]) # PROG (el indice fin nunca se incluye)

# 2. Atajo desde el inicio [:fin]
print(texto1[:4])  # PROG (asume inicio 0)

# 3. Atajo hasta el final [inicio:]
print(texto1[8:]) # "CION" (hasta el ultimo char)

# 4. Índices negativos
print(texto1[-4:]) # "CION" (los últimos 4)

# 5. Pasos [::paso] (Invertir la cadena)
print(texto1[::-1]) # "NOICAMARGORP"

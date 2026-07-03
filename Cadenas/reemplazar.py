# Programa : Reemplazar textos

mensaje = "Hola mundo, mundo"

# Reemplazar TODAS las apariciones
nuevo = mensaje.replace("mundo", "Python")
print(nuevo)

# Reemplazar solo UNA vez
uno_solo = mensaje.replace("mundo", "Dev", 1)
print(uno_solo)

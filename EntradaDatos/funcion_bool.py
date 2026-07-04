# Programa: Función bool

# 1. Números (int y float)
print(f"El 0 regresa: {bool(0)}")  # False
print(f"El 0.0 regresa: {bool(0.0)}")  # False
print(f"Cualquier número regresa: {bool(42)}") # True

# 2. Texto (Strings)
# Cadena vacia = Nada = False
print(f"La cadena vacia regresa: {bool("")}")

# Cadena con espacio o texto = Algo = True
print(f"Un espacio regresa: {bool(" ")}")    # True
print(f"Cualquier cadena regresa: {bool("Hola")}")

# 3. None (Ausencia total)
vacio = None
print(f"El valor de None regresa: {bool(vacio)}")
print(f"El valor False regresa: {bool(False)}")
print(f"El valor True regresa: {bool(True)}")

# Error común

respuesta_usuario = "False"
es_verdadero = bool(respuesta_usuario)
print(f"La respuesta usuario es {es_verdadero}")
# El String "False" tiene 5 letras, por lo tanto no esta vacio
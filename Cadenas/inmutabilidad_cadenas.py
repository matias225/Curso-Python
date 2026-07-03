# Ejemplo: Cadenas inmutables

animal = "Gato"

# animal[4] = "s"    # Provoca un error
# CORRECTO: Concatenar (sumar)
# Tomamos "Gato" + "s" y lo guardamos en una nueva variable
plural = animal + "s"

# Nuevo objeto
print(plural)

# La original sigue igual
print(animal)

# Con f string
plural = f"{animal}s"
print(plural)

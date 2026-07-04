# Valores aleatorios con la funcion randint

# Importar el módulo completo o solo la función
#import random
from random import randint

# Generar un número aleatorio entre 1 y 10, los valores estan incluidos
numero = randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero}")

# Simular un dado de seis caras
dado = randint(1, 6)
print(f"Resultado de lanzar un dado: {dado}")

# Simular un dado de 20 caras
dado20 = randint(1, 20)
print(f"Resultado de lanzar un d20: {dado20}")
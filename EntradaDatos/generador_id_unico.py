from random import randint

print("*** Generador de id único ***")
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
anio_nacimiento = input("Ingrese el año de nacimiento (yyyy): ")

# 1. Usar 2 primeras letras del nombre en mayusculas
# 2. Lo mismo para el apellido
# 3. Del valor de año, tomar los últimos 2 digitos
# 4. Un valor aleatorio de 4 digitos

# Normalizar los valores, puedo aplicar todos los metodos a la vez en distinto orden
nombre_modificado = nombre.strip().upper()[:2]
apellido = apellido.strip()[:2].upper()
anio_nacimiento = anio_nacimiento.strip()[2:]

# Genero un valor aleatorio de 4 digitos
numero_aleatorio = randint(1000, 9999)

# Genero el id único
id_unico = f"{nombre_modificado}{apellido}{anio_nacimiento}{numero_aleatorio}"
print(f"Hola {nombre.strip()},\n\tTu nuevo número de identificación (ID) generado por el sistema es:\n\t{id_unico}\n\t¡Felicidades!")

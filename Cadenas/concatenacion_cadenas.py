# Programa: Ejemplo de concatenación

# 1. Usando el operador +
nombre = "Brisa"
apellido = "Olate"
nombre_completo = nombre + " " + apellido
print("Usando +: " +nombre_completo)

# 2. Usando el metodo print
edad = 25
print("Usando comas:", "Nombre:",nombre_completo,", Edad:", edad)

# 3. Usando f-strings
ciudad = "San Rafael"
pais = "Argentina"
profesion = "Estudiante"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad +1} años y soy {profesion} en {ciudad}, {pais}"
print(presentacion)

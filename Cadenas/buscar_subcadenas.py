# Programa: Buscar subcadenas

cadena = "Hola, mundo!"
indice = cadena.find("mundo")
print(f"Indice de la subcadena mundo: {indice}")

indice = cadena.find("Hola")
print(f"Indice de la subcadena Hola: {indice}")

indice = cadena.find("!")
print(f"Indice de la subcadena !: {indice}")

# Si no la encuentra regresa -1
indice = cadena.find("Matias")
print(f"Indice de la subcadena Matias: {indice}")

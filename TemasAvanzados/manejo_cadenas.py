# Manejo de cadenas

# Dividir una cadena con split()
cadena = 'Hola mundo'
palabras = cadena.split()
print(palabras)

# Buscar con find
posicion = cadena.find('mundo') # Devuelve el valor de 5
print(f'Posicion de la cadena mundo: {posicion}')

# Reemplazar con replace
nueva_cadena = cadena.replace('mundo', 'amigo')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

# Multiplicacion de cadenas
cadena = 'Hola '
resultado_multiplicacion = cadena * 5
print(f'Resultado multiplicacion: {resultado_multiplicacion}')

# Strip - limpiar una cadena de espacios al principio y final
cadena = '       Hola mundo        '
cadena_limpia = cadena.strip()
print(f'Cadena limpia: {cadena_limpia}')

# Tambien puede limpiar otros caracteres
cadena = '------Matias-------------'
cadena_limpia = cadena.strip("-")
print(f'Cadena limpia: {cadena_limpia}')

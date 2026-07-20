print('*** Regresar una tupla de valores desde una función ***')

# Definimos la función
def persona_mayusculas(nombre, apellido, edad):
    print('Esta función regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

# Programa principal
nombre, apellido, edad = persona_mayusculas('matias', 'romani',33)
print(f'Nombre: {nombre}, apellido: {apellido}, edad: {edad}')

print('*** Función con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Nombre: {nombre}, apellido: {apellido}, edad: {edad}')

# Primero llamamos la función pasando los argumentos de manera posicional
imprimir_persona('Brisa', 'Olate', 26)

# Llamar la función usando argumentos por nombre
imprimir_persona(nombre='Matias', apellido='Romani', edad=33)

# Llamar la función usando argumentos por nombre pero intercambiando el orden
imprimir_persona(edad=25, apellido='Romani', nombre='Santiago')

# Argumentos con valores por default
imprimir_persona(nombre='Brisa')
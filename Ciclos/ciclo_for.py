print('*** Ciclo for ***')

cadena = 'Hola Mundo'

# Iteramos los caracteres, la opción end permite cambiar el salto de linea (por defecto)
print('Recorremos los caracteres de la cadena')
for letra in cadena:
    print(letra, end=' ')

print('\n\nRecorremos la lista de frutas')
frutas = ['Banana', 'Frutilla', 'Durazno']
for fruta in frutas:
    print(fruta, end=' ')
# Toma la cantidad de elementos de la lista mas pequenia
nombres = ['Matias', 'Brisa', 'Santiago', 'Fabrizio']
edades = [33, 26, 25]
ciudades = ['San Rafael', 'Alvear', 'Malargue']

# Combinar los elementos correspondientes usando la funcion zip
personas = zip(nombres, edades, ciudades)

# Iterar sobre el resultado de la funcion zip
for persona in personas:
    print(persona)
# *args - arguments - tupla
# *kwargs - keyword argumentos (key, value) como un dict
print('*** Argumentos variables en forma de dict ***')

def superheroe_superpoderes(nombre, *args, **kwargs): #los kwargs siempre van últimos, también son opcionales
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamamos la función
superheroe_superpoderes('Batman', 'inteligencia', edad=45, universo='DC')
superheroe_superpoderes('Ironman','Armadura', 'inteligencia', edad=45)
superheroe_superpoderes('Matias Romani')

print('Argumentos variables')

def superheroes_superpoderes(superheroe, nombre, *args): # Los argumentos variables siempre deben ser el ultimo argumento y son opcionales
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    # Iteramos la tupla
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

superheroes_superpoderes('Batman', 'Bruce Wayne','inteligencia', 'experto en todos los tipos de combate')
superheroes_superpoderes('Superman', 'Clark Kent', 'super fuerza', 'super velocidad', 'vision laser')
superheroes_superpoderes('Yo','Matias Romani')



from sistema_bibliotecas.biblioteca import Biblioteca
from sistema_bibliotecas.libro import Libro

bibiliotecaMoreno = Biblioteca('Mariano Moreno')
print(f'*** Bienvenidos a la bibliotecas {bibiliotecaMoreno.nombre} ***')

# Definicion de libros
libro1 = Libro('Cien anos de soledad', 'Gabriel Garcia Marquez', 'Ficcion')
libro2 = Libro('1984','George Orwell','Ficcion')
libro3 = Libro('Don Quijote de la Mancha','Miguel de Cervantes','Comedia')
libro4 = Libro('El amor en tiempos de colera','Gabriel Garcia Marquez','Ficcion')
libro5 = Libro('Pantaleon y las visitadoras', 'Mario Vargas Llosa', 'Comedia')
bibiliotecaMoreno.agregar_libro(libro1)
bibiliotecaMoreno.agregar_libro(libro2)
bibiliotecaMoreno.agregar_libro(libro3)
bibiliotecaMoreno.agregar_libro(libro4)
bibiliotecaMoreno.agregar_libro(libro5)

# Buscar libros por autor
autor = 'Gabriel Garcia Marquez'
print(f'\nLibros del autor: {autor}')
bibiliotecaMoreno.buscar_libros_autor(autor)

# Buscar libros por genero
genero = 'Ficcion'
print(f'\nibros del genero: {genero}')
bibiliotecaMoreno.buscar_libros_genero(genero)

genero = 'Comedia'
print(f'\nLibros del genero: {genero}')
bibiliotecaMoreno.buscar_libros_genero(genero)

# Mostrar todos los libros
bibiliotecaMoreno.mostrar_todos_los_libros()

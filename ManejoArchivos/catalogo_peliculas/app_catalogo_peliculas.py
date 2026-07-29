from ManejoArchivos.catalogo_peliculas.pelicula import Pelicula
from ManejoArchivos.catalogo_peliculas.servicio_peliculas import ServicioPeliculas

class AppCatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def catalogo_peliculas(self):
        salir = False
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Error: {e}')

    def mostrar_menu(self):
        print('''Opciones: 
        1. Agregar pelicula
        2. Listar peliculas
        3. Eliminar catalogo de peliculas
        4. Salir
        ''')
        return int(input('Escoja su opcion (1-4): '))

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            nombre = input('Ingresa el nombre de la pelicula: ')
            nueva_pelicula = Pelicula(nombre)
            self.servicio_peliculas.agregar_pelicula(nueva_pelicula)
        elif opcion == 2:
            self.servicio_peliculas.listar_peliculas()
        elif opcion == 3:
            self.servicio_peliculas.eliminar_archivo_peliculas()
        elif opcion == 4:
            print('Saliendo...')
            return True
        else:
            print('Opcion invalida. Introduce un numero del 1 al 4.')
        return False


# Programa principal
if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.catalogo_peliculas()

from os import remove

class ServicioPeliculas:
    NOMBRE_ARCHIVO = 'peliculas.txt'

    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula.nombre)
        print(f'Se agrega un pelicula:\n{pelicula.nombre}')
        with open(self.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def crear_archivo(self):
        open(self.NOMBRE_ARCHIVO, 'x').close()

    def obtener_peliculas(self):
        peliculas = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo:
                for linea in archivo:
                    nombre = linea.strip()
                    peliculas.append(nombre)
        except FileExistsError as e:
            print('Error al leer archivo: No existe el archivo, cargue una pelicula.')
        return peliculas

    def listar_peliculas(self):
        self.peliculas = self.obtener_peliculas()
        print('\n--- Catalogo de peliculas ---')
        for pelicula in self.peliculas:
            print(pelicula)
        print()

    def eliminar_archivo_peliculas(self):
        remove(ServicioPeliculas.NOMBRE_ARCHIVO)
        self.peliculas = []
        print(f'Archivo eliminado: {self.NOMBRE_ARCHIVO}')

    def get_peliculas(self):
        return self.peliculas

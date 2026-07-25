class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return (f'Id: {self.id_monitor}, Marca: {self.marca}, '
                f'Tamaño: {self.tamanio}')

if __name__ == '__main__':
    monitor1 = Monitor('LG', 27)
    print(monitor1)
    monitor2 = Monitor('Acer', 22)
    print(monitor2)
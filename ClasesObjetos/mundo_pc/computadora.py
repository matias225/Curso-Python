from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''

# Codigo principal
if __name__ == '__main__':
    teclado1 = Teclado('HyperX', 'USB')
    raton1 = Raton('Redragon', 'USB')
    monitor1 = Monitor('LG UltraGear', 27)
    computadora1 = Computadora('Matias PC', monitor1, teclado1, raton1)
    print(computadora1)

    teclado2 = Teclado('Machenike', 'USB')
    raton2 = Raton('Corsair', 'Bluetooth')
    monitor2 = Monitor('Asus', 15)
    computadora2 = Computadora('Matias Notebook', monitor2, teclado2, raton2)
    print(computadora2)

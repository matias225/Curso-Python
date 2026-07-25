from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

print('*** Mundo PC ***')

# Computadora 1
teclado1 = Teclado('HyperX', 'USB')
raton1 = Raton('Redragon', 'USB')
monitor1 = Monitor('LG UltraGear', 27)
computadora1 = Computadora('Matias PC', monitor1, teclado1, raton1)

# Computadora 2
teclado2 = Teclado('Machenike', 'USB')
raton2 = Raton('Corsair', 'Bluetooth')
monitor2 = Monitor('Asus', 15)
computadora2 = Computadora('Matias Notebook', monitor2, teclado2, raton2)

# Crear la lista de computadoras
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
# print(orden1)

teclado3 = Teclado('Redragon', 'USB')
raton3 = Raton('Logitech', 'Wireless')
monitor3 = Monitor('Acer', 24)
computadora3 = Computadora('PC 3', monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)

print(orden1)

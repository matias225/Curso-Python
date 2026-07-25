class Animal:
    def comer(self):
        print("Come muchas veces al dia")

    def dormir(self):
        print("Duermo muchas horas")

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

# Programa principal
print('*** Ejemplo de Herencia ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()

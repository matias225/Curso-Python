class Automovil:
    # Ejemplo con distintos atributos
    # def __init__(self, marca, modelo, color):
    #     self.marca = marca # Atributo publico
    #     self._modelo = modelo # Atributo protegido, python no lo protege es una convencion
    #     self.__color = color # Atributo privado

    # Estandarizados
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def conducir(self):
        print(f'''Conduciendo el automóvil: 
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}
        ''')

    # Definir los métodos de manera explicita
    # def get_marca(self):
    #     return self._marca

    # def set_marca(self, marca):
    #     self._marca = marca

    @property # Definir el metodo get de manera más pythonica
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

# Programa principal
if __name__ == '__main__':
    # Creación del primer automovil
    automovil1 = Automovil('Volkswagen','Gol', 'Rojo')
    automovil1.conducir()
    # No deberíamos acceder a los atributos que no sean públicos
    # automovil1._modelo = 'Yaris' # Esto se permite, pero no es una buena práctica
    # automovil1.__color = 'Azul' # Aca si Python ignora la modificación, por ser privado
    # automovil1.conducir()
    # automovil1._Automovil__color = 'Verde' # Se puede acceder igual así, pero es mala práctica
    # automovil1.set_marca('Toyota')
    # automovil1.set_modelo('Yaris')
    # automovil1.set_color('Azul')
    automovil1.marca = 'Toyota'
    automovil1.modelo = 'Yaris'
    automovil1.color = 'Azul'
    # Intentar agregar un nuevo atributo, solo se agrega al objeto elegido
    setattr(automovil1,'nuevo_atributo', 'Valor nuevo atributo')
    # También se puede agregar dinamicamente
    automovil1.nuevo_atributo2 = 'Valor nuevo atributo 2'
    automovil1.conducir()
    # Atributo de marca del automovil 1 con property
    print(f'Atributo marca automovil1: {automovil1.marca}')
    print(f'Atributo marca automovil1: {automovil1.modelo}')
    print(f'Atributo marca automovil1: {automovil1.color}')
    print(automovil1.nuevo_atributo)
    print(automovil1.nuevo_atributo2)
    print()
    # Segundo objeto
    automovil2 = Automovil('Pegueot','206', 'Blanco')
    automovil2.conducir()
    # Preguntarle a python por los atributos
    print(f'Atributos del automovil1: {automovil1.__dict__}')
    print(f'Atributos del automovil2: {automovil2.__dict__}')

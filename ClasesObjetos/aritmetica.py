class Aritmetica:

    # Python solamente toma el ultimo constructor
    # def __init__(self, operando1):
    #     self.operando1 = operando1

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado de la suma: {resultado}')

    def resta(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado de la resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado de la multiplicacion: {resultado}')

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado de la division: {resultado:.2f}')

# Programa principal
if __name__ == '__main__':
    print('--- Ejemplo Clase Aritmetica---')
    print('Primer objeto: Operando 1: 5, Operando 2: 7')
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.resta()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    # Segundo objeto
    print('\nSegundo objeto: Operando 1: 12, Operando 2: 16')
    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumar()
    aritmetica2.resta()
    aritmetica2.multiplicar()
    aritmetica2.dividir()
    # Tercer objeto
    print('\nTercer objeto: Operando 1: 7, Operando 2: 5')
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 5
    aritmetica3.sumar()
    # Cuarto objeto
    print('\nCuarto objeto: Operando 1: 2, Operando 2: 8')
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    aritmetica4.sumar()
    print('\nQuinto objeto: Operando 1: 4, Operando 2: 3')
    aritmetica5 = Aritmetica(operando2=3, operando1=4)
    aritmetica5.sumar()

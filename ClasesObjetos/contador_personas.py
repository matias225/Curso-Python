class Persona:
    # Atributo clase
    contador_persona = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_persona += 1
        self.id = Persona.contador_persona
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo estatico')
        return Persona.contador_persona

    @classmethod
    def get_contador_persona_clase(cls):
        print('Metodo de clase')
        return cls.contador_persona

# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Contador de Objetos de tipo Persona ***')
    persona1 = Persona('Matias', 'Romani')
    persona1.mostrar_persona()

    # Segundo objeto
    persona2 = Persona('Brisa', 'Olate')
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona: {Persona.contador_persona}')
    print(f'Contador objetos Persona (persona1): {persona1.contador_persona}')
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (clase): {Persona.get_contador_persona_clase()}')

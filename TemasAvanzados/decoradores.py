print('*** Decoradores ***')

def decorador(function):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la funcion de saludar')
        resultado = function(*args, **kwargs) # Llamamos a nuestra funcion
        print('Despues de llamar la funcion de saludar')
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Matias')

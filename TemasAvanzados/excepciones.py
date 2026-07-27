print('*** Manejo de Excepciones ***')

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception('No se puede dividir por 0')
        resultado = numerador / denominador
        print(f'Resutlado de la division {resultado}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    # except ZeroDivisionError:
    #     print('Error: No se puede dividir por 0')
    # except TypeError:
    #     print('Error: Los operandos deben ser numericos')
    else:
        print('No ocurrio ningun error')
    finally:
        print('Finalizando la excepcion\n')

# Ejemplo de uso
dividir(10, 2)
dividir(5, 0)
dividir(5, '2')

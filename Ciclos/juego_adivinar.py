from random import randint

print('Juego de Adivinar')

INTENTOS_MAX = 5
intentos = 0
ingresado = None
valor_secreto = randint(1, 10)

while ingresado != valor_secreto and intentos < INTENTOS_MAX:
    ingresado = int(input('Ingrese el numero a adivinar: '))
    if ingresado > valor_secreto:
        print('El numero a adivinar es menor')
    elif ingresado < valor_secreto:
        print('El numero a adivinar es mayor')
    intentos += 1

if ingresado == valor_secreto:
    print(f'Felicidades adivinaste el número, el valor era {valor_secreto}, lo adivinaste en {intentos} intentos')
else:
    print(f'Intentos terminados, perdiste, el valor era: {valor_secreto}')

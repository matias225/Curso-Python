print('*** Sistema de Envíos ***')

# Constantes
TARIFA_NACIONAL = 10
TARIFA_INTER = 20

destino = input('Ingrese el destino (nacional/internacional): ')
peso = float(input('Ingrese el peso del paquete (kg): '))
costo_envio = None

destino = destino.strip().lower()

if destino == 'nacional':
    costo_envio = TARIFA_NACIONAL * peso
elif destino == 'internacional':
    costo_envio = TARIFA_INTER * peso
else:
    print("Destino incorrecto. Ingresa si es nacional o internacional")

if costo_envio is not None:
    print(f"El costo del envio {destino} de un paquete de peso {peso} kg es: ${costo_envio:.2f}")

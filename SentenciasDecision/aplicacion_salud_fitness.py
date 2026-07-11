print('*** Aplicación de Salud y Fitness ***')

# Constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado, son kilocalorias

# Pedimos los valores al usuario
nombre_usuario = input("Ingrese su nombre del usuario: ")
pasos_diarios = int(input("Ingrese su numero de pasos diarios: "))

# Verificar si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

# Calculamos calorias quemadas
calorias_quemados = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la información
print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados hoy: {pasos_diarios} pasos')
print(f'Calorias quemados: {calorias_quemados} kcal')
print(f'Meta de pasos diarios alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos es: {META_PASOS_DIARIOS} pasos')
print("*** Sistema Calificaciones ***")

calificacion = float(input('Ingrese su nota (0-10): '))
calificacion_letra = ''

if 9 <= calificacion <= 10:
    calificacion_letra = 'A'
elif 8 <= calificacion < 9:
    calificacion_letra = 'B'
elif 7 <= calificacion < 8:
    calificacion_letra = 'C'
elif 6 <= calificacion < 7:
    calificacion_letra = 'D'
elif 0 <= calificacion < 6:
    calificacion_letra = 'F'
else:
    calificacion_letra = "Calificación incorrecta"

print(f"Su calificación es: {calificacion_letra}")


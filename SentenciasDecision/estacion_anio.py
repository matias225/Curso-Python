print("*** Estación del Año ***")

mes = int(input("Ingrese el mes (1-12): "))
estacion = None

if mes == 12 or mes == 1 or mes == 2:
    estacion = "Verano"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Otoño"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Invierno"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Primavera"
else:
    estacion = "Estación desconocida"

print(f"La estación para el mes {mes} es {estacion}")



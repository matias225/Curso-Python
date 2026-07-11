print("##### SISTEMA DE RESERVA DE HOTEL v2 #####")

tarifa_diaria_con_vista = 190.5
tarifa_diaria_sin_vista = 150.5

nombre_cliente = input('Ingrese su nombre: ')
dias_estadia = int(input('¿Cuántos días se va a quedar? '))
vista_al_mar_txt = input('¿Quiere vista al mar? (Si/No) ')
vista_al_mar = vista_al_mar_txt.strip().lower() == 'si'

# Cálculos
costo_vista = tarifa_diaria_con_vista if vista_al_mar_txt else tarifa_diaria_sin_vista
costo_total = costo_vista * dias_estadia

# Mostrar reserva modificada
print("\n--------- Detalles de la reservación ----------")
print(f"Cliente: {nombre_cliente}")
print(f"Días de estadía: {dias_estadia}")
print(f"Costo total: ${costo_total:.2f}")
print(f"¿Vista al mar?: {'Si' if vista_al_mar else 'No'}")

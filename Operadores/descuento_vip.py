print("*** Sistema de descuentos VIP ***")

NO_PRODUCTIOS_DESCUENTO = 10
cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))
tiene_membresia = input("¿Tienes membresia? (Si/No): ")

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTIOS_DESCUENTO
                         and tiene_membresia.strip().lower() == "si")

print(f"¿Tienes acceso al descuento VIP?: {es_elegible_descuento}")
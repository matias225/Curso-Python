print("*** Tienda en Linea ***")

MONTO_COMPRA_DESC = 1000

monto = float(input("¿Cual es su monto de compro? "))
es_miembro = input("¿Es miembro? (Si/No) ")
descuento = 0

if monto >= MONTO_COMPRA_DESC and es_miembro.strip().lower() == "si":
    descuento = 0.1
elif es_miembro.strip().lower() == "si":
    descuento = 0.05
elif monto >= MONTO_COMPRA_DESC:
    descuento = 0.03
else:
    descuento = 0

# Cálculos
if descuento != 0:
    monto_descuento = monto * descuento
    monto_total = monto - monto_descuento
    print(f"Felicidades has obtenido un descuento del {descuento * 100:.0f}%")
    print(f"Monto de la compra:                         ${monto:.2f}")
    print(f"Monto del descuento:                        ${monto_descuento:.2f}")
    print(f"Monto final de la compra con descueno:      ${monto_total:.2f}")
else:
    print("No has obtenido ningún descuento")
    print("Te invitamos a hacerte miembro de la tienda")
    print(f"Monto final de la compra con descueno:          ${monto:.2f}")

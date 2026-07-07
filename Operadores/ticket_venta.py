print("*** Generación Ticket Venta ***")
precio_leche = float(input("Ingrese el precio del leche: "))
precio_pan = float(input("Ingrese el precio del pan: "))
precio_lechuga = float(input("Ingrese el precio del lechuga: "))
precio_banana = float(input("Ingrese el precio del banana: "))
descuento_porcentaje = int(input("Ingrese el descuento (%): "))

# Calculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_lechuga + precio_pan + precio_banana

# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje/100)

# Calculo de subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calculo con impuestos (21%)
impuesto = subtotal_con_descuento * 0.21

# Calculo total de la compra (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f"""
Subtotal:               ${subtotal:.2f}
Descuento:              ${descuento} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento:.2f}
Impuesto (21%):         ${impuesto:.2f}
Costo total compra:     ${costo_total_compra:.2f}""")
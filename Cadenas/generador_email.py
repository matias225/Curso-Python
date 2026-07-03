# Generador de Email


# Variables: Nombre, Empresa, Dominio
nombre = " Brisa Candela Olate "
# Limpiamos espacios en blanco inicio y fin, directamente lo hace el metodo strip()
nombre_normalizado = nombre.strip()
# Reemplazamos espacios en blacno por punto
nombre_normalizado = nombre_normalizado.replace(" ",".")
# Convertimos a minusculas
nombre_normalizado = nombre_normalizado.lower()

####        Se puede hacer junto
# nombre_normalizado = nombre.strip().lower().replace(" ",".")

empresa = " Cruz Roja "
dominio = ".com.ar"
# A la vez en una linea el nombre de empresa y el dominio
dominio_email = f"@{empresa.lower().replace(" ","")}{dominio}"
# Unimos nombre y dominio emial
email_generado = f"{nombre_normalizado}{dominio_email}"

print(f"{'*'* 10} GENERADOR DE EMAIL {'*'* 10}")
print(f"Nombre de usuario: {nombre}")
print(f"Nombre de usuario normalizado: {nombre_normalizado}")
print(f"\nEmpresa: {empresa}")
print(f"Extensión del dominio: {dominio}")
print(f"Dominio de email normalizado: {dominio_email}")
print(f"\nEmail final generado: {email_generado}")

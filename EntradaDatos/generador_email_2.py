# Generador de Email mejorado

# Variables: Nombre, Empresa, Dominio
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
empresa = input("Ingrese su empresa: ")
pais = input("Ingrese su pais: ")

# Normalizamos los valores
nombre = nombre.strip().lower().replace(" ", ".")
apellido = apellido.strip().lower().replace(' ', '.')
empresa = empresa.strip().lower().replace(" ", "")
dominio = f".com.{pais.strip().lower()[:2]}"

nombre_completo = f"{nombre}.{apellido}"

# A la vez en una linea el nombre de empresa y el dominio
dominio_email = f"@{empresa}{dominio}"
# Unimos nombre y dominio emial
email_generado = f"{nombre_completo}{dominio_email}"

print(f"\n{'*'* 10} GENERADOR DE EMAIL 2.0 {'*'* 10}")
print(f"""
Tu nuevo email generado por el sistema es:
    {email_generado}
    ¡Felicidades!""")

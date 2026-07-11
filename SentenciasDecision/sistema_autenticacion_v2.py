print("*** Sistema Autenticacion v2 ***")

USUARIO_VALIDO = "matias225"
PASSWORD_VALIDO = "123456"

usuario = input("Ingrese su usuario: ")
contrasenia = input("Ingrese su contraseña: ")
usuario = usuario.strip().lower()
contrasenia = contrasenia.strip().lower()

if usuario == USUARIO_VALIDO and contrasenia == PASSWORD_VALIDO:
    print(f"¡Bienvenido {usuario}!")
elif usuario == USUARIO_VALIDO:
    print(f"Contraseña incorrecta")
elif contrasenia == PASSWORD_VALIDO:
    print(f"El usuario {usuario} no es valido")
else:
    print(f"El usuario y la contraseña no son válidos")

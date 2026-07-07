print("*** Sistema Autenticacion ***")

USUARIO_VALIDO = "matias225"
PASSWORD_VALIDO = "123456"

usuario = input("Ingrese su usuario: ")
contrasenia = input("Ingrese su contraseña: ")

datos_correctos = usuario.strip() == USUARIO_VALIDO and contrasenia.strip() == PASSWORD_VALIDO

print(f"¿Datos correctos? {datos_correctos}")
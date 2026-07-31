# Insertar registros desde Python a mysql
import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost", # 127.0.0.1
    user="root",
    password="admin",
    database="personas_db"
)

# Ejecutar la sentencia insert
cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES (%s , %s , %s)'
valores = ('Pipis', 'Trello', 1)
cursor.execute(sentencia_sql, valores)
personas_db.commit() # Guardar los cambios en la bd
print(f'Se ha agregado el nuevo registro a la base de datos: {valores}')
cursor.close()
personas_db.close()

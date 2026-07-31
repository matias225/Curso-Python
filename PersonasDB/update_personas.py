# Actualizar registros desde Python a mysql
from mysql import connector

personas_db = connector.connect(
    host="localhost", # 127.0.0.1
    user="root",
    password="admin",
    database="personas_db"
)

# Ejecutar la sentencia update
cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre = %s, apellido = %s, edad = %s WHERE id = %s'
valores = ('Pipis', 'Trello', 1, 6)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f'Se ha modifica el registro de la base de datos')
cursor.close()
personas_db.close()

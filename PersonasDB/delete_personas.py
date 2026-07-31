# Borrar registros desde Python a mysql
from mysql import connector

personas_db = connector.connect(
    host="localhost", # 127.0.0.1
    user="root",
    password="admin",
    database="personas_db"
)

# Ejecutar la sentencia delete
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id = %s'
valores = (6,) # Tengo que agregar la , para que sea una tupla
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f'Se ha eliminado el registro de la base de datos')
cursor.close()
personas_db.close()

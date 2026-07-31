# Seleccionar registros desde Python a mysql
from mysql import connector

personas_db = connector.connect(
    host="localhost", # 127.0.0.1
    user="root",
    password="admin",
    database="personas_db"
)

# Ejecutar la sentencia select
cursor = personas_db.cursor()
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()

for persona in resultado:
    print(persona)

cursor.close()
personas_db.close()

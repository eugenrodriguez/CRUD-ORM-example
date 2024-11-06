# db.py
import mariadb

# Configuración de la conexión a MariaDB
conn = mariadb.connect(
    user="root",
    password="12345",
    host="localhost"
)

cursor = conn.cursor()

# Crear la base de datos y la tabla de personas
cursor.execute("CREATE DATABASE IF NOT EXISTS personas_db")
cursor.execute("USE personas_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT
)
""")

conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Base de datos y tabla creadas exitosamente.")

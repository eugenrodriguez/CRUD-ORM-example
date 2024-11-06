import mariadb

# Conectar a MariaDB (sin especificar una base de datos inicialmente)
conn = mariadb.connect(
    user="root",
    password="12345",
    host="localhost"
)

# Crear un cursor
cursor = conn.cursor()

# Crear la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS personas_db")

# Seleccionar la base de datos recién creada
cursor.execute("USE personas_db")

# Crear la tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT
)
""")

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Base de datos y tabla creadas exitosamente.")

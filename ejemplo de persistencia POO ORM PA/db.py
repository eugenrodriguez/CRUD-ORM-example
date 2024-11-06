import mariadb

conn = mariadb.connect(
    user="root",
    password="12345",
    host="localhost"
)

cursor = conn.cursor()

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

cursor.close()
conn.close()

print("Base de datos y tabla creadas exitosamente.")

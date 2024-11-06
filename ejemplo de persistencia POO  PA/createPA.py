# createPA.py
import mariadb

# Conexión a la base de datos personas_db
conn = mariadb.connect(
    user="root",
    password="12345",
    host="localhost",
    database="personas_db"
)
cursor = conn.cursor()

# Crear procedimientos almacenados
cursor.execute("DROP PROCEDURE IF EXISTS insertar_persona;")
cursor.execute("DROP PROCEDURE IF EXISTS actualizar_persona;")
cursor.execute("DROP PROCEDURE IF EXISTS eliminar_persona;")
cursor.execute("DROP PROCEDURE IF EXISTS consultar_personas;")

cursor.execute("""
CREATE PROCEDURE insertar_persona(IN p_nombre VARCHAR(100), IN p_edad INT)
BEGIN
    INSERT INTO personas (nombre, edad) VALUES (p_nombre, p_edad);
END;
""")

cursor.execute("""
CREATE PROCEDURE actualizar_persona(IN p_id INT, IN p_nombre VARCHAR(100), IN p_edad INT)
BEGIN
    UPDATE personas SET nombre = p_nombre, edad = p_edad WHERE id = p_id;
END;
""")

cursor.execute("""
CREATE PROCEDURE eliminar_persona(IN p_id INT)
BEGIN
    DELETE FROM personas WHERE id = p_id;
END;
""")

cursor.execute("""
CREATE PROCEDURE consultar_personas()
BEGIN
    SELECT * FROM personas;
END;
""")

conn.commit()

cursor.close()
conn.close()

print("Procedimientos almacenados creados exitosamente.")

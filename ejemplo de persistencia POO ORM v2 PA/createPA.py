import mariadb

# Conectar a la base de datos
conn = mariadb.connect(
    user="root",
    password="12345",
    host="localhost",
    database="personas_db"
)

# Crear un cursor
cursor = conn.cursor()

# Eliminar los procedimientos si ya existen (esto evitará errores al intentar crear procedimientos existentes)
cursor.execute("DROP PROCEDURE IF EXISTS insertar_persona;")
cursor.execute("DROP PROCEDURE IF EXISTS actualizar_persona;")
cursor.execute("DROP PROCEDURE IF EXISTS eliminar_persona;")
cursor.execute("DROP PROCEDURE IF EXISTS consultar_personas;")

# Crear procedimiento almacenado para insertar una persona
cursor.execute("""
CREATE PROCEDURE insertar_persona(IN p_nombre VARCHAR(100), IN p_edad INT)
BEGIN
    INSERT INTO personas (nombre, edad) VALUES (p_nombre, p_edad);
END;
""")

# Crear procedimiento almacenado para actualizar una persona
cursor.execute("""
CREATE PROCEDURE actualizar_persona(IN p_id INT, IN p_nombre VARCHAR(100), IN p_edad INT)
BEGIN
    UPDATE personas SET nombre = p_nombre, edad = p_edad WHERE id = p_id;
END;
""")

# Crear procedimiento almacenado para eliminar una persona
cursor.execute("""
CREATE PROCEDURE eliminar_persona(IN p_id INT)
BEGIN
    DELETE FROM personas WHERE id = p_id;
END;
""")

# Crear procedimiento almacenado para consultar todas las personas
cursor.execute("""
CREATE PROCEDURE consultar_personas()
BEGIN
    SELECT * FROM personas;
END;
""")

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Procedimientos almacenados creados exitosamente.")

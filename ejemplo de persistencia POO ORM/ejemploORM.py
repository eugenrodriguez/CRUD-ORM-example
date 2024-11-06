from db import BaseDeDatos


class InterfazUsuario:
    def __init__(self, db):
        self.db = db

    def mostrar_menu(self):
        while True:
            print("\n--- MENÚ DE OPERACIONES CRUD ---")
            print("1. Insertar Persona")
            print("2. Consultar Personas")
            print("3. Actualizar Persona")
            print("4. Eliminar Persona")
            print("5. Salir")

            opcion = input("Selecciona una opción (1-5): ")

            if opcion == "1":
                nombre = input("Ingrese el nombre de la persona: ")
                edad = int(input("Ingrese la edad de la persona: "))
                self.db.insertar_persona(nombre, edad)
            elif opcion == "2":
                self.db.consultar_personas()
            elif opcion == "3":
                id_persona = int(
                    input("Ingrese el ID de la persona a actualizar: "))
                nombre = input("Ingrese el nuevo nombre: ")
                edad = int(input("Ingrese la nueva edad: "))
                self.db.actualizar_persona(id_persona, nombre, edad)
            elif opcion == "4":
                id_persona = int(
                    input("Ingrese el ID de la persona a eliminar: "))
                self.db.eliminar_persona(id_persona)
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")


class BaseDeDatosORM(BaseDeDatos):
    def __init__(self, user, password, host, database):
        super().__init__(user, password, host, database)
        # Creación de la tabla Persona si no existe
        self.crear_tabla_persona()

    def crear_tabla_persona(self):
        query = """
        CREATE TABLE IF NOT EXISTS personas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            edad INT
        );
        """
        self.ejecutar(query)

    def insertar_persona(self, nombre, edad):
        query = "INSERT INTO personas (nombre, edad) VALUES (%s, %s)"
        self.ejecutar(query, (nombre, edad))
        print(f"Persona {nombre} agregada correctamente.")

    def consultar_personas(self):
        query = "SELECT * FROM personas"
        self.ejecutar(query)
        personas = self.obtener_resultados()
        for persona in personas:
            print(f"{persona[0]}: {persona[1]}, {persona[2]} años")

    def actualizar_persona(self, id, nuevo_nombre, nueva_edad):
        query = "UPDATE personas SET nombre = %s, edad = %s WHERE id = %s"
        self.ejecutar(query, (nuevo_nombre, nueva_edad, id))
        print(f"Persona con ID {id} actualizada.")

    def eliminar_persona(self, id):
        query = "DELETE FROM personas WHERE id = %s"
        self.ejecutar(query, (id,))
        print(f"Persona con ID {id} eliminada.")


# Configuración de la base de datos
DATABASE_CONFIG = {
    'user': 'root',
    'password': '12345',
    'host': 'localhost',
    'database': 'personas_db'
}

# Crear la instancia de la base de datos y la interfaz de usuario
db = BaseDeDatosORM(**DATABASE_CONFIG)
interfaz = InterfazUsuario(db)

# Ejecutar el menú
interfaz.mostrar_menu()

# Cerrar la conexión a la base de datos al salir
db.cerrar()

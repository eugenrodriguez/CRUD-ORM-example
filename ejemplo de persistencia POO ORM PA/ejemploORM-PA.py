import mariadb


class BaseDeDatos:
    def __init__(self, user, password, host, database):
        self.conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
        self.cursor = self.conn.cursor()

    def ejecutar_proc(self, proc_name, params):
        try:
            self.cursor.callproc(proc_name, params)
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error al ejecutar el procedimiento {proc_name}: {e}")

    def obtener_resultados(self):
        results = []
        for result in self.cursor.stored_results():
            results = result.fetchall()
        return results

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()


class Persona:
    def __init__(self, db):
        self.db = db

    def insertar_persona(self, nombre, edad):
        self.db.ejecutar_proc('insertar_persona', (nombre, edad))
        print(f"Persona {nombre} agregada correctamente.")

    def consultar_personas(self):
        self.db.ejecutar_proc('consultar_personas', ())
        personas = self.db.obtener_resultados()
        if personas:
            for persona in personas:
                print(f"{persona[0]}: {persona[1]}, {persona[2]} años")
        else:
            print("No hay personas registradas.")

    def actualizar_persona(self, p_id, nombre, edad):
        self.db.ejecutar_proc('actualizar_persona', (p_id, nombre, edad))
        print(f"Persona con ID {p_id} actualizada.")

    def eliminar_persona(self, p_id):
        self.db.ejecutar_proc('eliminar_persona', (p_id,))
        print(f"Persona con ID {p_id} eliminada.")


# Conectar a la base de datos
db = BaseDeDatos(user="root", password="12345",
                 host="localhost", database="personas_db")

# Crear un objeto de la clase Persona y realizar operaciones
persona = Persona(db)

# Menú de operaciones


def mostrar_menu():
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
            persona.insertar_persona(nombre, edad)
        elif opcion == "2":
            persona.consultar_personas()
        elif opcion == "3":
            p_id = int(input("Ingrese el ID de la persona a actualizar: "))
            nombre = input("Ingrese el nuevo nombre de la persona: ")
            edad = int(input("Ingrese la nueva edad de la persona: "))
            persona.actualizar_persona(p_id, nombre, edad)
        elif opcion == "4":
            p_id = int(input("Ingrese el ID de la persona a eliminar: "))
            persona.eliminar_persona(p_id)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el menú
mostrar_menu()

# Cerrar la conexión
db.cerrar_conexion()

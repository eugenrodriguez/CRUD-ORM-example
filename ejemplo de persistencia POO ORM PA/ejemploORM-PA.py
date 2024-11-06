# ejemploORM-PA.py
from sqlalchemy.orm import sessionmaker
from db import engine, Persona
import mariadb

# Conectar directamente a MariaDB para usar procedimientos almacenados
conn = mariadb.connect(
    user="root",
    password="12345",
    host="localhost",
    database="personas_db"
)
cursor = conn.cursor()

# Crear una sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


class PersonaCRUD:
    def __init__(self):
        self.conn = conn
        self.cursor = cursor

    def insertar_persona(self, nombre, edad):
        try:
            self.cursor.callproc('insertar_persona', (nombre, edad))
            self.conn.commit()
            print(f"Persona {nombre} agregada correctamente.")
        except mariadb.Error as e:
            print(f"Error al insertar persona: {e}")

    def consultar_personas(self):
        try:
            self.cursor.callproc('consultar_personas')
            for result in self.cursor.stored_results():
                personas = result.fetchall()
                for persona in personas:
                    print(f"{persona[0]}: {persona[1]}, {persona[2]} años")
        except mariadb.Error as e:
            print(f"Error al consultar personas: {e}")

    def actualizar_persona(self, p_id, nombre, edad):
        try:
            self.cursor.callproc('actualizar_persona', (p_id, nombre, edad))
            self.conn.commit()
            print(f"Persona con ID {p_id} actualizada.")
        except mariadb.Error as e:
            print(f"Error al actualizar persona: {e}")

    def eliminar_persona(self, p_id):
        try:
            self.cursor.callproc('eliminar_persona', (p_id,))
            self.conn.commit()
            print(f"Persona con ID {p_id} eliminada.")
        except mariadb.Error as e:
            print(f"Error al eliminar persona: {e}")

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()


# Instancia de PersonaCRUD
crud = PersonaCRUD()


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
            crud.insertar_persona(nombre, edad)
        elif opcion == "2":
            crud.consultar_personas()
        elif opcion == "3":
            p_id = int(input("Ingrese el ID de la persona a actualizar: "))
            nombre = input("Ingrese el nuevo nombre de la persona: ")
            edad = int(input("Ingrese la nueva edad de la persona: "))
            crud.actualizar_persona(p_id, nombre, edad)
        elif opcion == "4":
            p_id = int(input("Ingrese el ID de la persona a eliminar: "))
            crud.eliminar_persona(p_id)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el menú
mostrar_menu()
crud.cerrar_conexion()

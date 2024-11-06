# main.py
from ejemploORM import BaseDeDatosORM


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


DATABASE_URL = "mariadb+mariadbconnector://root:12345@localhost/personas_db"
db = BaseDeDatosORM(DATABASE_URL)
interfaz = InterfazUsuario(db)

interfaz.mostrar_menu()

db.cerrar()

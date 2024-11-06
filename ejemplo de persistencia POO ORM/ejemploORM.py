import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db import BaseDeDatos  # Importar la clase desde db.py

Base = declarative_base()


class Persona(Base):
    __tablename__ = 'personas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)


class BaseDeDatosORM:
    def __init__(self, database_url):
        self.engine = create_engine(database_url, echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def insertar_persona(self, nombre, edad):
        nueva_persona = Persona(nombre=nombre, edad=edad)
        self.session.add(nueva_persona)
        self.session.commit()
        print(f"Persona {nombre} agregada correctamente.")

    def consultar_personas(self):
        personas = self.session.query(Persona).all()
        for persona in personas:
            print(f"{persona.id}: {persona.nombre}, {persona.edad} años")

    def actualizar_persona(self, id, nuevo_nombre, nueva_edad):
        persona = self.session.query(Persona).filter(Persona.id == id).first()
        if persona:
            persona.nombre = nuevo_nombre
            persona.edad = nueva_edad
            self.session.commit()
            print(f"Persona con ID {id} actualizada.")

    def eliminar_persona(self, id):
        persona = self.session.query(Persona).filter(Persona.id == id).first()
        if persona:
            self.session.delete(persona)
            self.session.commit()
            print(f"Persona con ID {id} eliminada.")

    def cerrar(self):
        self.session.close()


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


# Configuración de la base de datos
DATABASE_URL = "mariadb+mariadbconnector://root:12345@localhost/personas_db"

# Crear la instancia de la base de datos y la interfaz de usuario
db = BaseDeDatosORM(DATABASE_URL)
interfaz = InterfazUsuario(db)

# Ejecutar el menú
interfaz.mostrar_menu()

# Cerrar la conexión a la base de datos al salir
db.cerrar()

import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

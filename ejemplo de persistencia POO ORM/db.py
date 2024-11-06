from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Persona(Base):
    __tablename__ = 'personas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)


def inicializar_base_datos(database_url):
    engine = create_engine(database_url, echo=True)
    Base.metadata.create_all(engine)
    print("Base de datos y tabla creadas exitosamente.")

# db.py
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar la base de datos con SQLAlchemy
DATABASE_URL = "mariadb+mariadbconnector://root:12345@localhost/personas_db"

# Crear motor y sesión
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definir la clase Persona como un modelo de SQLAlchemy


class Persona(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)

# Crear la base de datos y la tabla si no existen


def crear_tabla():
    Base.metadata.create_all(bind=engine)
    print("Base de datos y tabla creadas exitosamente.")


# Llamar a la función para crear la tabla
if __name__ == "__main__":
    crear_tabla()

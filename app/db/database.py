from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#url de la base de datos
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/apiHoteles"
# CREAR MOTOR DE CONEXION QUE INTERACTUARA CON LA BD UTILIZANDO LA URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# CONFIGURA UN GENERADOR DE SESIONS
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# CREAR BASE PARA DEFINIR LOS MODELOS DE LA TABLA BD
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
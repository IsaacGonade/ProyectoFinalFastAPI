from app.db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from sqlalchemy.orm import relationship

"""TABLA USUARIO"""
class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)

# CREATE TABLE user (
#      id INT AUTO_INCREMENT PRIMARY KEY,
#      username VARCHAR(255) NOT NULL,
#      password VARCHAR(255) NOT NULL
# );

"""TABLA HOTEL"""
class Hotel(Base):
    __tablename__ = "hotel"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(String)
    categoria = Column(String)
    piscina = Column(Boolean, default=False)
    localidad = Column(String)
    habitacion = relationship("Habitacion", backref="hotel", cascade="delete,merge")


# CREATE TABLE hotel (
#      id INT AUTO_INCREMENT PRIMARY KEY,
#      nombre VARCHAR(255) NOT NULL,
#      descripcion VARCHAR(255) NOT NULL,
#      categoria VARCHAR(255) NOT NULL,
#      piscina BOOLEAN,
#      localidad VARCHAR(255) NOT NULL
# );

"""TABLA HABITACION"""
class Habitacion(Base):
    __tablename__ = "habitacion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tamanio = Column(Integer)
    precio = Column(Integer)
    desayuno = Column(Boolean, default=False)
    ocupada = Column(Boolean, default=False)
    id_hotel = Column(Integer, ForeignKey("hotel.id", ondelete="CASCADE"))

# CREATE TABLE habitacion (
#      id INT AUTO_INCREMENT PRIMARY KEY,
#      tamanio INT NOT NULL,
#      precio INT NOT NULL,
#      desayuno BOOLEAN default false,
#      ocupada BOOLEAN default false,
#      id_hotel INT NOT NULL,
#      FOREIGN KEY (id_hotel) REFERENCES hotel(id) ON DELETE CASCADE
# );
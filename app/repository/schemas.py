from pydantic import BaseModel


# CREATE TABLE user (
#      id INT AUTO_INCREMENT PRIMARY KEY,
#      username VARCHAR(255) NOT NULL,
#      password VARCHAR(255) NOT NULL
# );
class User(BaseModel):
    username: str
    password: str


# CREATE TABLE hotel (
#      id INT AUTO_INCREMENT PRIMARY KEY,
#      nombre VARCHAR(255) NOT NULL,
#      descripcion VARCHAR(255) NOT NULL,
#      categoria VARCHAR(255) NOT NULL,
#      piscina BOOLEAN,
#      localidad VARCHAR(255) NOT NULL
# );
class Hotel(BaseModel):
    nombre: str
    descripcion: str
    categoria: str
    piscina: bool
    localidad: str


# CREATE TABLE habitacion (
#      id INT AUTO_INCREMENT PRIMARY KEY,
#      tamanio INT NOT NULL,
#      precio INT NOT NULL,
#      desayuno BOOLEAN default false,
#      ocupada BOOLEAN default false,
#      id_hotel INT NOT NULL,
#      FOREIGN KEY (id_hotel) REFERENCES hotel(id) ON DELETE CASCADE
# );
class Habitacion(BaseModel):
    tamanio: int
    precio: int
    desayuno: bool
    ocupada: bool

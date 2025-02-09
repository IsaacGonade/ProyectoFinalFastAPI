from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.repository import schemas
from app.db import models
from app.db.database import get_db

router = APIRouter(prefix="/api/habitaciones", tags=["Habitaciones"])

@router.get("/")
def get_all(db:Session = Depends(get_db)):
    habitaciones = db.query(models.Habitacion).all()
    return habitaciones


@router.post("/nueva/{id_hotel}/habitacion")
def insert_habitacion(id_hotel: int, habitacion: schemas.Habitacion, db: Session = Depends(get_db)):
    hotel = db.query(models.Hotel).filter(models.Hotel.id == id_hotel).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel no encontrado")

    newHabitacion = models.Habitacion()
    newHabitacion.tamanio = habitacion.tamanio
    newHabitacion.precio = habitacion.precio
    newHabitacion.desayuno = habitacion.desayuno
    newHabitacion.ocupada = habitacion.ocupada
    newHabitacion.id_hotel = habitacion.id_hotel

    db.add(newHabitacion)
    db.commit()
    db.refresh(newHabitacion)

    return newHabitacion
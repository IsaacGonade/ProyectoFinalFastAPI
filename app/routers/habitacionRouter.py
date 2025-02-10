from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.repository import schemas
from app.db import models
from app.db.database import get_db
from app.security import JWTAuth

router = APIRouter(prefix="/api/habitaciones", tags=["Habitaciones"])

@router.get("/")
def get_all(db:Session = Depends(get_db), token:str = Depends(JWTAuth.oauth2_scheme)):
    habitaciones = db.query(models.Habitacion).all()
    return habitaciones


@router.post("/nueva/{id_hotel}/habitacion")
def insert_habitacion(id_hotel: int, habitacion: schemas.Habitacion, db: Session = Depends(get_db), token:str = Depends(JWTAuth.oauth2_scheme)):
    hotel = db.query(models.Hotel).filter(models.Hotel.id == id_hotel).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel no encontrado")

    newHabitacion = models.Habitacion()
    newHabitacion.tamanio = habitacion.tamanio
    newHabitacion.precio = habitacion.precio
    newHabitacion.desayuno = habitacion.desayuno
    newHabitacion.ocupada = habitacion.ocupada
    newHabitacion.id_hotel = id_hotel

    db.add(newHabitacion)
    db.commit()
    db.refresh(newHabitacion)

    return newHabitacion

@router.delete("/borrar/{id_habitacion}")
def delete_habitacion(id_habitacion:int, db:Session = Depends(get_db), token:str = Depends(JWTAuth.oauth2_scheme)):
    habitacion = db.query(models.Habitacion).filter(models.Habitacion.id == id_habitacion).first()
    if habitacion:
        db.delete(habitacion)
        db.commit()
        return {"Mensaje": "Habitacion borrada"}
    else:
        raise HTTPException(status_code=404, detail="Habitacion no encontrada")


@router.put("/editar/{id_habitacion}")
def update_habitacion(id_habitacion:int, habitacion:schemas.Habitacion, db:Session = Depends(get_db), token:str = Depends(JWTAuth.oauth2_scheme)):
    newHabitacion = db.query(models.Habitacion).filter(models.Habitacion.id == id_habitacion).first()
    if newHabitacion:
        newHabitacion.tamanio = habitacion.tamanio
        newHabitacion.precio = habitacion.precio
        newHabitacion.desayuno = habitacion.desayuno
        newHabitacion.ocupada = habitacion.ocupada

        db.commit()
        return newHabitacion
    else:
        raise HTTPException(status_code=404, detail="Habitacion no encontrada")

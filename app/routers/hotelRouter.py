from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session, joinedload

from app.repository import schemas
from app.db import models
from app.db.database import get_db
from app.security import JWTAuth

router = APIRouter(prefix="/api/hoteles", tags=["Hoteles"])

@router.get("/")
def get_all(db:Session = Depends(get_db), token:str = Depends(JWTAuth.oauth2_scheme)):
    hoteles = db.query(models.Hotel).options(joinedload(models.Hotel.habitaciones)).all()
    return hoteles


@router.get("/localidad/{localidad}")
def get_hotel_by_localidad(localidad:str, db:Session = Depends(get_db)):
    hoteles = db.query(models.Hotel).filter(models.Hotel.localidad.ilike(f"%{localidad}%")).all()
    return hoteles


@router.get("/categoria/{categoria}")
def get_hotel_by_categoria(categoria:str, db:Session = Depends(get_db)):
    hoteles = db.query(models.Hotel).filter(models.Hotel.categoria.ilike(f"%{categoria}%")).all()
    return hoteles


@router.post("/nuevoHotel")
def insert_hotel(hotel:schemas.Hotel, db: Session = Depends(get_db), token:str = Depends(JWTAuth.oauth2_scheme)):
    newHotel = models.Hotel()
    newHotel.nombre = hotel.nombre
    newHotel.descripcion = hotel.descripcion
    newHotel.categoria = hotel.categoria
    newHotel.piscina = hotel.piscina
    newHotel.localidad = hotel.localidad
    db.add(newHotel)
    db.commit()
    return newHotel



from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.db import models
from app.db.database import get_db

router = APIRouter(prefix="/api/habitaciones", tags=["Habitaciones"])

@router.get("/")
def get_all(db:Session = Depends(get_db)):
    habitaciones = db.query(models.Habitacion).all()
    return habitaciones
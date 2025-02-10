from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.repository import schemas
from app.db import models
from app.db.database import get_db
from app.security import JWTAuth

router = APIRouter(prefix="/api/users", tags=["Usuarios"])

@router.get("/")
def get_all(db:Session = Depends(get_db), token:str = Depends(JWTAuth.oauth2_scheme)):
    users = db.query(models.User).all()
    return users


@router.post("/crearUsuario")
def create_user(user:schemas.User, db: Session = Depends(get_db)):
    newUser = models.User()
    newUser.username = user.username
    newUser.password = user.password

    db.add(newUser)
    db.commit()
    return newUser

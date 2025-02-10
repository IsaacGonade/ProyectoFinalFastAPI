import hashlib
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy import and_

from sqlalchemy.orm import Session
from app.db.models import User
from app.db.database import get_db

router = APIRouter(prefix="/api", tags=["Token Gen"])

oauth2_scheme = OAuth2PasswordBearer("/api/token")

SECRET_KEY = "secreta_clave"
ALGORITHM = "HS256"

def create_token(data: dict):
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return  token

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(User).filter(and_(User.username == form_data.username, User.password == hashlib.sha256(form_data.password.encode()).hexdigest())).first()
    if user:
        token = create_token(data={"sub":user.username})
        return {
            "access_token": token,
            "token_type":"bearer"
        }

@router.get("/getToken")
def get_token(token:str = Depends(oauth2_scheme)):
    return token
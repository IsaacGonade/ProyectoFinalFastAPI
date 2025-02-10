from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/api", tags=["Token Gen"])

oauth2_scheme = OAuth2PasswordBearer("/api/token")
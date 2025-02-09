from fastapi import FastAPI
import uvicorn
from app.db.database import Base, engine
from app.routers import userRouter, hotelRouter, habitacionRouter


#Funcion para crear todas las tablas
def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

app = FastAPI()
app.include_router(userRouter.router)
app.include_router(hotelRouter.router)
app.include_router(habitacionRouter.router)

if __name__ ==  "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
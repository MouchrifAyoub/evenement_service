from fastapi import FastAPI
from app.config.database import database
from app.api.evenement_controller import router as evenement_router

app = FastAPI(title="Evenement Service")

# Connexion à la base
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# API Root
@app.get("/")
async def read_root():
    return {"message": "Evenement Service API is running"}

# Inclusion du contrôleur
app.include_router(evenement_router, prefix="/api")

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import database
from app.api.demande_evenement_controller import router as demande_router
from app.api.evenement_controller import router as evenement_router
from app.api.budget_controller import router as budget_router
from app.api.logistique_controller import router as logistique_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(title="Evenement Service", root_path="/evenement", lifespan=lifespan)

# API Root
@app.get("/")
async def read_root():
    return {"message": "Evenement Service API is running"}

# Inclusion des contrôleurs
app.include_router(demande_router, prefix="/api")
app.include_router(evenement_router, prefix="/api")
app.include_router(budget_router, prefix="/api")
app.include_router(logistique_router, prefix="/api")

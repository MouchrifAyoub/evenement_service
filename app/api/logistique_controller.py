from fastapi import APIRouter, HTTPException, status
from app.config.database import database
from app.schemas.logistique import LogistiqueCreate
from app.repositories.logistique_repository import LogistiqueRepository
from app.services.logistique_service import LogistiqueService

router = APIRouter()

@router.post("/logistiques")
async def ajouter_logistique(payload: LogistiqueCreate):
    repo = LogistiqueRepository(db=database)
    service = LogistiqueService(repo)
    try:
        return await service.ajouter_logistique(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/logistiques/{id}/modifier")
async def modifier_logistique(id: int, materiel: str, transport: str):
    repo = LogistiqueRepository(db=database)
    service = LogistiqueService(repo)
    try:
        return await service.modifier_logistique(id, materiel, transport)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

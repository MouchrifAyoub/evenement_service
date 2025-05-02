from fastapi import APIRouter, HTTPException, status
from app.config.database import database
from app.schemas.evenement import EvenementCreate, EvenementRead, StatutEvenementEnum
from app.repositories.evenement_repository import EvenementRepository
from app.services.evenement_service import EvenementService

router = APIRouter()

@router.post("/evenements", response_model=EvenementRead, status_code=status.HTTP_201_CREATED)
async def creer_evenement(payload: EvenementCreate):
    repo = EvenementRepository(db=database)
    service = EvenementService(repo)
    try:
        return await service.creer_evenement(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/evenements/{id}/statut")
async def changer_statut_evenement(id: int, statut: StatutEvenementEnum):
    repo = EvenementRepository(db=database)
    service = EvenementService(repo)
    try:
        return await service.modifier_statut(id, statut)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

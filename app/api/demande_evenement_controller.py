from fastapi import APIRouter, HTTPException, status
from typing import List
from app.config.database import database
from app.schemas.demande_evenement import DemandeEvenementCreate, DemandeEvenementRead, StatutDemandeEnum
from app.repositories.demande_evenement_repository import DemandeEvenementRepository
from app.services.demande_evenement_service import DemandeEvenementService

router = APIRouter()
UTILISATEUR_ID_TEST = 1  # à remplacer par auth plus tard

@router.post("/demandes-evenements", response_model=DemandeEvenementRead, status_code=status.HTTP_201_CREATED)
async def creer_demande_evenement(payload: DemandeEvenementCreate):
    repo = DemandeEvenementRepository(db=database)
    service = DemandeEvenementService(repo)
    try:
        return await service.creer_demande(payload, UTILISATEUR_ID_TEST)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/mes-demandes-evenements", response_model=List[DemandeEvenementRead])
async def lister_mes_demandes_evenements():
    repo = DemandeEvenementRepository(db=database)
    return await repo.get_by_user(UTILISATEUR_ID_TEST)

@router.put("/demandes-evenements/{id}/traiter")
async def traiter_demande_evenement(id: int, statut: StatutDemandeEnum, motif_refus: str = None):
    repo = DemandeEvenementRepository(db=database)
    service = DemandeEvenementService(repo)
    try:
        return await service.traiter_demande(id, statut, motif_refus)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

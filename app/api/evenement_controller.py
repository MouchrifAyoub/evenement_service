from fastapi import APIRouter, HTTPException, status
from typing import List

from app.config.database import database
from app.schemas.evenement import (
    EvenementCreate,
    EvenementRead,
    EvenementTraiter,
    EventStatutEnum,
    EvenementUpdateStatut,
)
from app.services.evenement_service import EvenementService
from app.repositories.evenement_repository import EvenementRepository

router = APIRouter()
UTILISATEUR_ID_TEST = 1  # à remplacer par l'ID utilisateur réel plus tard


@router.post("/evenements", response_model=EvenementRead, status_code=status.HTTP_201_CREATED)
async def creer_evenement(payload: EvenementCreate):
    repository = EvenementRepository(db=database)
    service = EvenementService(repository)
    try:
        return await service.creer_evenement(payload, UTILISATEUR_ID_TEST)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/mes-evenements", response_model=List[EvenementRead])
async def lister_mes_evenements():
    repository = EvenementRepository(db=database)
    return await repository.get_by_user(UTILISATEUR_ID_TEST)


@router.get("/evenements-valides", response_model=List[EvenementRead])
async def lister_evenements_valides():
    repository = EvenementRepository(db=database)
    return await repository.get_validated()


@router.patch("/evenements/{id}/statut")
async def changer_statut_evenement(id: int, payload: EvenementUpdateStatut):
    repository = EvenementRepository(db=database)
    service = EvenementService(repository)
    try:
        return await service.modifier_statut(id, payload.statut)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/evenements/{id}/traiter")
async def traiter_evenement(id: int, traitement: EvenementTraiter):
    repository = EvenementRepository(db=database)
    service = EvenementService(repository)
    try:
        return await service.traiter_evenement(id, traitement)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

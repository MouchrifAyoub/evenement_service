from fastapi import APIRouter, HTTPException, status
from app.config.database import database
from app.schemas.budget import BudgetCreate
from app.repositories.budget_repository import BudgetRepository
from app.services.budget_service import BudgetService

router = APIRouter()

@router.post("/budgets")
async def ajouter_budget(payload: BudgetCreate):
    repo = BudgetRepository(db=database)
    service = BudgetService(repo)
    try:
        return await service.ajouter_budget(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/budgets/{id}/valider")
async def valider_budget(id: int, montant_valide: int):
    repo = BudgetRepository(db=database)
    service = BudgetService(repo)
    try:
        return await service.valider_budget(id, montant_valide)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

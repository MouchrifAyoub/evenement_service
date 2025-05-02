from app.schemas.budget import BudgetCreate
from app.repositories.budget_repository import BudgetRepository

class BudgetService:
    def __init__(self, repository: BudgetRepository):
        self.repository = repository

    async def ajouter_budget(self, data: BudgetCreate):
        return await self.repository.create(data)

    async def valider_budget(self, budget_id: int, montant_valide: int):
        success = await self.repository.update_validation(budget_id, montant_valide, True)
        if not success:
            raise ValueError("Impossible de valider le budget.")
        return {"message": "Budget validé avec succès."}

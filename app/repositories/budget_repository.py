from typing import Optional
from databases import Database
from sqlalchemy import insert, select, update
from app.models.budget import Budget
from app.schemas.budget import BudgetCreate

class BudgetRepository:
    def __init__(self, db: Database):
        self.db = db

    async def create(self, data: BudgetCreate):
        query = (
            insert(Budget)
            .values(
                montant_estime=data.montant_estime,
                montant_valide=data.montant_valide,
                valide_par_service_financier=data.valide_par_service_financier,
                evenement_id=data.evenement_id,
            )
            .returning(Budget)
        )
        return await self.db.fetch_one(query)

    async def get_by_evenement(self, evenement_id: int) -> Optional[Budget]:
        query = select(Budget).where(Budget.evenement_id == evenement_id)
        return await self.db.fetch_one(query)

    async def update_validation(self, budget_id: int, montant_valide: int, valide: bool) -> bool:
        query = (
            update(Budget)
            .where(Budget.id == budget_id)
            .values(montant_valide=montant_valide, valide_par_service_financier=valide)
            .returning(Budget.id)
        )
        result = await self.db.fetch_one(query)
        return result is not None

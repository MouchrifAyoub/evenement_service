from typing import Optional
from databases import Database
from sqlalchemy import insert, select, update
from app.models.logistique import Logistique
from app.schemas.logistique import LogistiqueCreate

class LogistiqueRepository:
    def __init__(self, db: Database):
        self.db = db

    async def create(self, data: LogistiqueCreate):
        query = (
            insert(Logistique)
            .values(
                materiel_necessaire=data.materiel_necessaire,
                transport_necessaire=data.transport_necessaire,
                evenement_id=data.evenement_id,
            )
            .returning(Logistique)
        )
        return await self.db.fetch_one(query)

    async def get_by_evenement(self, evenement_id: int) -> Optional[Logistique]:
        query = select(Logistique).where(Logistique.evenement_id == evenement_id)
        return await self.db.fetch_one(query)

    async def update(self, logistique_id: int, materiel: str, transport: str) -> bool:
        query = (
            update(Logistique)
            .where(Logistique.id == logistique_id)
            .values(materiel_necessaire=materiel, transport_necessaire=transport)
            .returning(Logistique.id)
        )
        result = await self.db.fetch_one(query)
        return result is not None

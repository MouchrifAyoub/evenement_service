from typing import List, Optional
from databases import Database
from sqlalchemy import select, insert, update
from app.models.evenement import Evenement, StatutEvenementEnum
from app.schemas.evenement import EvenementCreate

class EvenementRepository:
    def __init__(self, db: Database):
        self.db = db

    async def create(self, data: EvenementCreate):
        query = (
            insert(Evenement)
            .values(
                titre=data.titre,
                date_evenement=data.date_evenement,
                lieu=data.lieu,
                nb_participants=data.nb_participants,
                demande_id=data.demande_id,
                status=StatutEvenementEnum.EN_PREPARATION,
            )
            .returning(Evenement)
        )
        return await self.db.fetch_one(query)

    async def get_by_id(self, evenement_id: int) -> Optional[Evenement]:
        query = select(Evenement).where(Evenement.id == evenement_id)
        return await self.db.fetch_one(query)

    async def update_status(self, evenement_id: int, status: StatutEvenementEnum) -> bool:
        query = (
            update(Evenement)
            .where(Evenement.id == evenement_id)
            .values(status=status)
            .returning(Evenement.id)
        )
        result = await self.db.fetch_one(query)
        return result is not None

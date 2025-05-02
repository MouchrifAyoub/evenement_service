from typing import List, Optional
from databases import Database
from sqlalchemy import select, insert, update
from app.models.demande_evenement import DemandeEvenement, StatutDemandeEnum
from app.schemas.demande_evenement import DemandeEvenementCreate

class DemandeEvenementRepository:
    def __init__(self, db: Database):
        self.db = db

    async def create(self, data: DemandeEvenementCreate, user_id: int):
        query = (
            insert(DemandeEvenement)
            .values(
                titre=data.titre,
                description=data.description,
                lieux=data.lieux,
                date_evenement=data.date_evenement,
                cree_par=user_id,
                statut=StatutDemandeEnum.EN_ATTENTE,
            )
            .returning(DemandeEvenement)
        )
        return await self.db.fetch_one(query)

    async def get_by_user(self, user_id: int) -> List[DemandeEvenement]:
        query = select(DemandeEvenement).where(DemandeEvenement.cree_par == user_id)
        return await self.db.fetch_all(query)

    async def get_by_id(self, demande_id: int) -> Optional[DemandeEvenement]:
        query = select(DemandeEvenement).where(DemandeEvenement.id == demande_id)
        return await self.db.fetch_one(query)

    async def traiter(self, demande_id: int, statut: StatutDemandeEnum, motif_refus: Optional[str] = None) -> bool:
        values = {
            "statut": statut,
            "motif_refus": motif_refus if statut == StatutDemandeEnum.REFUSEE else None,
        }
        query = (
            update(DemandeEvenement)
            .where(DemandeEvenement.id == demande_id)
            .values(**values)
            .returning(DemandeEvenement.id)
        )
        result = await self.db.fetch_one(query)
        return result is not None

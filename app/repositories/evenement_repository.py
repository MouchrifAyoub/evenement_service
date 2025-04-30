from typing import List, Optional
from databases import Database
from sqlalchemy import select, insert, update
from app.models.evenement import Evenement, EventStatutEnum
from app.schemas.evenement import EvenementCreate, EvenementTraiter

class EvenementRepository:
    def __init__(self, db: Database):
        self.db = db

    async def create(self, data: EvenementCreate, user_id: int):
        query = (
            insert(Evenement)
            .values(
                nom=data.nom,
                description=data.description,
                date_evenement=data.date_evenement,
                lieu=data.lieu,
                budget_estime=data.budget_estime,
                besoins_logistiques=data.besoins_logistiques,
                cree_par=user_id,
                est_etudiant=data.est_etudiant,
                statut=EventStatutEnum.EN_ATTENTE,
            )
            .returning(Evenement)
        )
        return await self.db.fetch_one(query)

    async def get_by_user(self, user_id: int) -> List[Evenement]:
        query = select(Evenement).where(Evenement.cree_par == user_id)
        return await self.db.fetch_all(query)

    async def get_validated(self) -> List[Evenement]:
        query = select(Evenement).where(Evenement.statut == EventStatutEnum.VALIDE)
        return await self.db.fetch_all(query)

    async def get_by_id(self, evenement_id: int) -> Optional[Evenement]:
        query = select(Evenement).where(Evenement.id == evenement_id)
        return await self.db.fetch_one(query)

    async def update_statut(self, evenement_id: int, statut: EventStatutEnum) -> bool:
        query = (
            update(Evenement)
            .where(Evenement.id == evenement_id)
            .values(statut=statut)
            .returning(Evenement.id)
        )
        result = await self.db.fetch_one(query)
        return result is not None

    async def traiter(self, evenement_id: int, traitement: EvenementTraiter) -> bool:
        values = {
            "statut": traitement.statut,
            "commentaire_refus": traitement.commentaire_refus if traitement.statut == EventStatutEnum.REFUSE else None,
        }
        query = (
            update(Evenement)
            .where(Evenement.id == evenement_id)
            .values(**values)
            .returning(Evenement.id)
        )
        result = await self.db.fetch_one(query)
        return result is not None

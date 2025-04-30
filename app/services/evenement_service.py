from datetime import date, timedelta
from app.schemas.evenement import EvenementCreate, EvenementTraiter
from app.models.evenement import EventStatutEnum
from app.repositories.evenement_repository import EvenementRepository


class EvenementService:
    def __init__(self, repository: EvenementRepository):
        self.repository = repository

    async def creer_evenement(self, data: EvenementCreate, user_id: int):
        if data.date_evenement < date.today() + timedelta(weeks=6):
            raise ValueError("La date de l'événement doit être au moins 6 semaines après aujourd’hui.")

        result = await self.repository.create(data, user_id)
        return result

    async def traiter_evenement(self, evenement_id: int, traitement: EvenementTraiter):
        evenement = await self.repository.get_by_id(evenement_id)
        if not evenement:
            raise ValueError("Événement introuvable.")

        if traitement.statut not in [EventStatutEnum.VALIDE, EventStatutEnum.REFUSE]:
            raise ValueError("Seuls les statuts 'valide' ou 'refuse' sont autorisés.")

        if traitement.statut == EventStatutEnum.REFUSE and not traitement.commentaire_refus:
            raise ValueError("Un commentaire est requis en cas de refus.")

        success = await self.repository.traiter(evenement_id, traitement)
        if not success:
            raise ValueError("Échec du traitement de la demande.")

        return {"message": "Traitement effectué avec succès."}

    async def modifier_statut(self, evenement_id: int, nouveau_statut: EventStatutEnum):
        evenement = await self.repository.get_by_id(evenement_id)
        if not evenement:
            raise ValueError("Événement introuvable.")

        success = await self.repository.update_statut(evenement_id, nouveau_statut)
        if not success:
            raise ValueError("Impossible de modifier le statut de l’événement.")

        return {"message": f"Statut mis à jour vers {nouveau_statut}."}

from datetime import date, timedelta
from app.schemas.demande_evenement import DemandeEvenementCreate
from app.models.demande_evenement import StatutDemandeEnum
from app.repositories.demande_evenement_repository import DemandeEvenementRepository

class DemandeEvenementService:
    def __init__(self, repository: DemandeEvenementRepository):
        self.repository = repository

    async def creer_demande(self, data: DemandeEvenementCreate, user_id: int):
        if data.date_evenement < date.today() + timedelta(weeks=6):
            raise ValueError("La date de l'événement doit être au moins 6 semaines après aujourd’hui.")
        return await self.repository.create(data, user_id)

    async def traiter_demande(self, demande_id: int, statut: StatutDemandeEnum, motif_refus: str = None):
        demande = await self.repository.get_by_id(demande_id)
        if not demande:
            raise ValueError("Demande introuvable.")

        if statut not in [StatutDemandeEnum.VALIDE, StatutDemandeEnum.REFUSEE]:
            raise ValueError("Seuls les statuts 'valide' ou 'refusée' sont autorisés.")

        if statut == StatutDemandeEnum.REFUSEE and not motif_refus:
            raise ValueError("Un motif est requis en cas de refus.")

        success = await self.repository.traiter(demande_id, statut, motif_refus)
        if not success:
            raise ValueError("Échec du traitement de la demande.")

        return {"message": "Traitement effectué avec succès."}

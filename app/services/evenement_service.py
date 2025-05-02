from app.schemas.evenement import EvenementCreate
from app.models.evenement import StatutEvenementEnum
from app.repositories.evenement_repository import EvenementRepository

class EvenementService:
    def __init__(self, repository: EvenementRepository):
        self.repository = repository

    async def creer_evenement(self, data: EvenementCreate):
        return await self.repository.create(data)

    async def modifier_statut(self, evenement_id: int, nouveau_statut: StatutEvenementEnum):
        evenement = await self.repository.get_by_id(evenement_id)
        if not evenement:
            raise ValueError("Événement introuvable.")

        success = await self.repository.update_status(evenement_id, nouveau_statut)
        if not success:
            raise ValueError("Impossible de modifier le statut de l’événement.")

        return {"message": f"Statut mis à jour vers {nouveau_statut}."}

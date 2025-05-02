from app.schemas.logistique import LogistiqueCreate
from app.repositories.logistique_repository import LogistiqueRepository

class LogistiqueService:
    def __init__(self, repository: LogistiqueRepository):
        self.repository = repository

    async def ajouter_logistique(self, data: LogistiqueCreate):
        return await self.repository.create(data)

    async def modifier_logistique(self, logistique_id: int, materiel: str, transport: str):
        success = await self.repository.update(logistique_id, materiel, transport)
        if not success:
            raise ValueError("Impossible de mettre à jour la logistique.")
        return {"message": "Logistique mise à jour avec succès."}

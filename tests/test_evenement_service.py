import pytest
from app.services.evenement_service import EvenementService
from app.repositories.evenement_repository import EvenementRepository
from app.models.evenement import StatutEvenementEnum
from unittest.mock import AsyncMock

@pytest.fixture
def fake_repo():
    return AsyncMock(spec=EvenementRepository)

@pytest.mark.asyncio
async def test_creer_evenement(fake_repo):
    service = EvenementService(fake_repo)
    data = type('obj', (), {
        "titre": "Conférence",
        "date_evenement": "2025-10-01",
        "lieu": "Salle B",
        "nb_participants": 100,
        "demande_id": 1
    })
    fake_repo.create.return_value = {"id": 1}
    result = await service.creer_evenement(data)
    assert result["id"] == 1

@pytest.mark.asyncio
async def test_modifier_statut_evenement(fake_repo):
    service = EvenementService(fake_repo)
    fake_repo.get_by_id.return_value = {"id": 1}
    fake_repo.update_status.return_value = True
    result = await service.modifier_statut(1, StatutEvenementEnum.PRET)
    assert "Statut mis à jour" in result["message"]

@pytest.mark.asyncio
async def test_modifier_statut_evenement_inexistant(fake_repo):
    service = EvenementService(fake_repo)
    fake_repo.get_by_id.return_value = None
    with pytest.raises(ValueError, match="introuvable"):
        await service.modifier_statut(999, StatutEvenementEnum.ANNULE)

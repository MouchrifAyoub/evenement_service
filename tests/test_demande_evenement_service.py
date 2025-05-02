import pytest
from datetime import date, timedelta
from app.services.demande_evenement_service import DemandeEvenementService
from app.repositories.demande_evenement_repository import DemandeEvenementRepository
from app.models.demande_evenement import StatutDemandeEnum
from unittest.mock import AsyncMock

@pytest.fixture
def fake_repo():
    return AsyncMock(spec=DemandeEvenementRepository)

@pytest.mark.asyncio
async def test_creer_demande_valide(fake_repo):
    service = DemandeEvenementService(fake_repo)
    data = type('obj', (), {
        "titre": "Conférence",
        "description": "Conf 2025",
        "lieux": "Salle 1",
        "date_evenement": date.today() + timedelta(weeks=7),
        "est_etudiant": True
    })
    fake_repo.create.return_value = {"id": 1}
    result = await service.creer_demande(data, user_id=1)
    assert result["id"] == 1

@pytest.mark.asyncio
async def test_creer_demande_date_invalide(fake_repo):
    service = DemandeEvenementService(fake_repo)
    data = type('obj', (), {
        "titre": "Conférence",
        "description": "Conf 2025",
        "lieux": "Salle 1",
        "date_evenement": date.today() + timedelta(weeks=2),
        "est_etudiant": True
    })
    with pytest.raises(ValueError, match="6 semaines"):
        await service.creer_demande(data, user_id=1)

@pytest.mark.asyncio
async def test_traiter_demande_refusee_sans_motif(fake_repo):
    service = DemandeEvenementService(fake_repo)
    fake_repo.get_by_id.return_value = {"id": 1}
    with pytest.raises(ValueError, match="motif"):
        await service.traiter_demande(1, StatutDemandeEnum.REFUSEE)

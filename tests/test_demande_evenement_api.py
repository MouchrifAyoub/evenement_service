import pytest
from datetime import date, timedelta

@pytest.mark.asyncio
async def test_creer_demande_evenement(async_client):
    payload = {
        "titre": "Test Event",
        "description": "Un super événement",
        "lieux": "Salle A",
        "date_evenement": str(date.today() + timedelta(weeks=7)),
        "est_etudiant": True
    }
    response = await async_client.post("/api/demandes-evenements", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["titre"] == "Test Event"

@pytest.mark.asyncio
async def test_refuser_demande_date_invalid(async_client):
    payload = {
        "titre": "Test Fail Event",
        "description": "Mauvaise date",
        "lieux": "Salle B",
        "date_evenement": str(date.today() + timedelta(weeks=2)),
        "est_etudiant": False
    }
    response = await async_client.post("/api/demandes-evenements", json=payload)
    assert response.status_code == 400
    assert "6 semaines" in response.json()["detail"]

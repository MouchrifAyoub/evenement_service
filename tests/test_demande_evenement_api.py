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

# Test pour consulter ses demandes (GET /api/mes-demandes-evenements)
# @pytest.mark.asyncio
# async def test_get_mes_demandes_evenements(async_client):
#     response = await async_client.get("/api/mes-demandes-evenements")
#     assert response.status_code == 200
#     data = response.json()
#     assert isinstance(data, list)

# Test pour consulter les événements validés (GET /api/evenements-valides)
# @pytest.mark.asyncio
# async def test_get_evenements_valides(async_client):
#     response = await async_client.get("/api/evenements-valides")
#     assert response.status_code == 200
#     data = response.json()
#     assert isinstance(data, list)

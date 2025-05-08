import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from app.main import app

@pytest.fixture
async def async_client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as client:
            yield client

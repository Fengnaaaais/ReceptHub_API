import pytest
from httpx import AsyncClient, ASGITransport

from main import app


# @pytest.mark.asyncio
# async def test_get_categoryies():
#     async with AsyncClient(
#         transport=ASGITransport(app=app),
#         base_url="http://test",
#     ) as ac:
#         response = await ac.get("/api/v1/categories/")
#         assert response.status_code == 200
#         data = response.json()
#         assert data != []


@pytest.mark.asyncio
async def test_create_category():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        response = await ac.post(
            "/api/v1/categories/create/",
            json={
                "name": "fsdfasdfsdasdfdsa",
                "image": "path/imaasfdge",
            },
        )
        assert response.status_code == 200
        data = response.json()

# tests/test_main.py
import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from main import app

@pytest.mark.anyio
async def test_home():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI app deployed via CI/CD on Render!  ***** to test if it changes without manually deploy"}



@pytest.mark.anyio
async def test_get_tasks():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        response = await ac.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "title" in data[0]


@pytest.mark.anyio
async def test_add_task():
    transport = ASGITransport(app=app)
    new_task = {"id": 3, "title": "Write tests"}
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        response = await ac.post("/tasks", json=new_task)
    assert response.status_code in [200, 201]


@pytest.mark.anyio
async def test_update_task():
    transport = ASGITransport(app=app)
    update_data = {"title": "Updated task"}
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        response = await ac.put("/tasks/3", json=update_data)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_delete_task():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        response = await ac.delete("/tasks/3")
    assert response.status_code == 200

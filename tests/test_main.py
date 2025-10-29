import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_home():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

@pytest.mark.asyncio
async def test_get_tasks():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "title" in data[0]

@pytest.mark.asyncio
async def test_add_task():
    new_task = {"id": 3, "title": "Write tests"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/tasks", json=new_task)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Write tests"

@pytest.mark.asyncio
async def test_update_task():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/tasks/1")
    assert response.status_code == 200
    data = response.json()
    assert data["done"] is True

@pytest.mark.asyncio
async def test_delete_task():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/tasks/2")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted"

from fastapi.testclient import TestClient
from app.main import app
from app.manager import task_service

client = TestClient(app)


def setup_function():
    task_service._tasks = []


def test_crud_lifecycle():
    resp = client.post("/tasks", json={"title": "Buy milk"})
    assert resp.status_code == 201

    resp = client.get("/tasks")
    assert len(resp.json()) == 1

    resp = client.put("/tasks/1", json={"title": "Buy eggs", "status": "DONE"})
    print(resp.json())
    assert resp.json()["title"] == "Buy eggs"

    resp = client.delete("/tasks/1")
    assert resp.status_code == 200
    assert len(task_service.get_all()) == 0


def test_get_non_existent_task():
    resp = client.get("/tasks/999")
    assert resp.status_code == 405


def test_update_non_existent_task():
    resp = client.put("/tasks/999", json={"title": "No task", "status": "DONE"})
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Task not found"


def test_delete_non_existent_task():
    resp = client.delete("/tasks/999")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Task not found"


def test_create_task_invalid_data():
    resp = client.post("/tasks", json={})
    assert resp.status_code == 422

    resp = client.post("/tasks", json={"title": 12345})
    resp = client.post("/tasks", json={"title": {"nested": "value"}})
    assert resp.status_code == 422
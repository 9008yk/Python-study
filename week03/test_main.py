"""FastAPI 待办 API 的 pytest 测试。"""

import pytest
from fastapi.testclient import TestClient

from main import app, todos


@pytest.fixture()
def client():
    todos.clear()
    return TestClient(app)


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"]


def test_create_todo(client):
    response = client.post("/todos", json={"task": "学习 FastAPI"})
    assert response.status_code == 200
    data = response.json()
    assert data["task"] == "学习 FastAPI"
    assert data["done"] is False
    assert data["id"] == 1


def test_list_todos(client):
    client.post("/todos", json={"task": "第一条"})
    client.post("/todos", json={"task": "第二条", "done": True})
    response = client.get("/todos")
    assert len(response.json()) == 2


def test_get_one_todo(client):
    client.post("/todos", json={"task": "学习 Python"})
    response = client.get("/todos/1")
    assert response.json()["task"] == "学习 Python"

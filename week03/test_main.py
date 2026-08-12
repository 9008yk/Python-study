"""FastAPI 待办 API 的 pytest 测试。"""

import pytest
from fastapi.testclient import TestClient

import main


@pytest.fixture()
def client():
    main.todos.clear()
    main.next_id = 1
    return TestClient(main.app)


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


def test_create_todo_validation(client):
    response = client.post("/todos", json={"task": ""})
    assert response.status_code == 422


def test_list_todos(client):
    client.post("/todos", json={"task": "第一条"})
    client.post("/todos", json={"task": "第二条", "done": True})
    response = client.get("/todos")
    assert len(response.json()) == 2


def test_filter_todos_by_done(client):
    client.post("/todos", json={"task": "第一条", "done": True})
    client.post("/todos", json={"task": "第二条"})
    response = client.get("/todos", params={"done": "true"})
    result = response.json()
    assert len(result) == 1
    assert result[0]["task"] == "第一条"


def test_limit(client):
    client.post("/todos", json={"task": "第一条"})
    client.post("/todos", json={"task": "第二条"})
    client.post("/todos", json={"task": "第三条"})
    response = client.get("/todos", params={"limit": 2})
    assert len(response.json()) == 2


def test_get_one_todo(client):
    client.post("/todos", json={"task": "学习 Python"})
    response = client.get("/todos/1")
    assert response.json()["task"] == "学习 Python"


def test_get_not_found(client):
    response = client.get("/todos/999")
    assert response.status_code == 404


def test_update_todo(client):
    client.post("/todos", json={"task": "学习 Python"})
    response = client.put("/todos/1", json={"done": True})
    data = response.json()
    assert data["task"] == "学习 Python"
    assert data["done"] is True


def test_delete_todo(client):
    client.post("/todos", json={"task": "要删除的待办"})
    response = client.delete("/todos/1")
    assert response.status_code == 204
    assert client.get("/todos/1").status_code == 404

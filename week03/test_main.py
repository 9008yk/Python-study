"""FastAPI 待办 API 的 pytest 测试。"""

import sqlite3

import pytest
from fastapi.testclient import TestClient

import database
import main


def register_and_login(client, username="xiaoming", password="secret123"):
    client.post(
        "/auth/register",
        json={"username": username, "password": password},
    )
    response = client.post(
        "/auth/login",
        json={"username": username, "password": password},
    )
    return response.json()["access_token"]


@pytest.fixture()
def client():
    database.conn.close()
    database.conn = sqlite3.connect(":memory:", check_same_thread=False)
    database.init_db()
    return TestClient(main.app)


@pytest.fixture()
def user_headers(client):
    token = register_and_login(client)
    return {"Authorization": f"Bearer {token}"}


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"]


def test_create_todo(client, user_headers):
    response = client.post("/todos", json={"task": "学习 FastAPI"}, headers=user_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["task"] == "学习 FastAPI"
    assert data["done"] is False
    assert data["id"] == 1


def test_create_todo_validation(client, user_headers):
    response = client.post("/todos", json={"task": ""}, headers=user_headers)
    assert response.status_code == 422


def test_list_todos(client, user_headers):
    client.post("/todos", json={"task": "第一条"}, headers=user_headers)
    client.post("/todos", json={"task": "第二条", "done": True}, headers=user_headers)
    response = client.get("/todos", headers=user_headers)
    assert len(response.json()) == 2


def test_filter_todos_by_done(client, user_headers):
    client.post("/todos", json={"task": "第一条", "done": True}, headers=user_headers)
    client.post("/todos", json={"task": "第二条"}, headers=user_headers)
    response = client.get("/todos", params={"done": "true"}, headers=user_headers)
    result = response.json()
    assert len(result) == 1
    assert result[0]["task"] == "第一条"


def test_limit(client, user_headers):
    client.post("/todos", json={"task": "第一条"}, headers=user_headers)
    client.post("/todos", json={"task": "第二条"}, headers=user_headers)
    client.post("/todos", json={"task": "第三条"}, headers=user_headers)
    response = client.get("/todos", params={"limit": 2}, headers=user_headers)
    assert len(response.json()) == 2


def test_get_one_todo(client, user_headers):
    client.post("/todos", json={"task": "学习 Python"}, headers=user_headers)
    response = client.get("/todos/1", headers=user_headers)
    assert response.json()["task"] == "学习 Python"


def test_get_not_found(client, user_headers):
    response = client.get("/todos/999", headers=user_headers)
    assert response.status_code == 404


def test_update_todo(client, user_headers):
    client.post("/todos", json={"task": "学习 Python"}, headers=user_headers)
    response = client.put("/todos/1", json={"done": True}, headers=user_headers)
    data = response.json()
    assert data["task"] == "学习 Python"
    assert data["done"] is True


def test_delete_todo(client, user_headers):
    client.post("/todos", json={"task": "要删除的待办"}, headers=user_headers)
    response = client.delete("/todos/1", headers=user_headers)
    assert response.status_code == 204
    assert client.get("/todos/1", headers=user_headers).status_code == 404


def test_register(client):
    response = client.post(
        "/auth/register",
        json={"username": "xiaoming", "password": "secret123"},
    )
    assert response.status_code == 201
    assert response.json()["username"] == "xiaoming"


def test_register_duplicate(client):
    data = {"username": "xiaoming", "password": "secret123"}
    client.post("/auth/register", json=data)
    response = client.post("/auth/register", json=data)
    assert response.status_code == 400


def test_login_and_me(client):
    client.post(
        "/auth/register",
        json={"username": "xiaoming", "password": "secret123"},
    )
    response = client.post(
        "/auth/login",
        json={"username": "xiaoming", "password": "secret123"},
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    me = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me.status_code == 200
    assert me.json()["username"] == "xiaoming"


def test_login_wrong_password(client):
    client.post(
        "/auth/register",
        json={"username": "xiaoming", "password": "secret123"},
    )
    response = client.post(
        "/auth/login",
        json={"username": "xiaoming", "password": "wrong123"},
    )
    assert response.status_code == 401


def test_me_without_token(client):
    response = client.get("/auth/me")
    assert response.status_code == 401


def test_todo_isolation(client):
    token_a = register_and_login(client, "user_a")
    token_b = register_and_login(client, "user_b")
    headers_a = {"Authorization": f"Bearer {token_a}"}
    headers_b = {"Authorization": f"Bearer {token_b}"}

    created = client.post("/todos", json={"task": "A 的待办"}, headers=headers_a)
    assert created.status_code == 201
    todo_id = created.json()["id"]

    assert client.get("/todos", headers=headers_b).json() == []
    assert client.get(f"/todos/{todo_id}", headers=headers_b).status_code == 404
    assert (
        client.put(
            f"/todos/{todo_id}",
            json={"done": True},
            headers=headers_b,
        ).status_code
        == 404
    )
    assert client.delete(f"/todos/{todo_id}", headers=headers_b).status_code == 404

    assert client.get(f"/todos/{todo_id}", headers=headers_a).status_code == 200

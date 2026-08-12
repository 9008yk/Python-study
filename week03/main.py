"""FastAPI 入门：待办 API。"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Todo API")

todos = []


class TodoCreate(BaseModel):
    task: str
    done: bool = False


class Todo(TodoCreate):
    id: int


@app.get("/")
def read_root():
    return {"message": "Todo API 运行中"}


@app.get("/todos")
def list_todos():
    return todos


@app.post("/todos")
def create_todo(item: TodoCreate):
    todo = Todo(id=len(todos) + 1, **item.model_dump())
    todos.append(todo)
    return todo


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "找不到这个待办"}

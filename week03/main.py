"""FastAPI 待办 API：SQLite 持久化版本。"""

import os
import sys

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field

sys.path.insert(0, os.path.dirname(__file__))

import database

tags_metadata = [
    {"name": "todos", "description": "待办管理接口"},
    {"name": "meta", "description": "服务信息"},
]

app = FastAPI(title="Todo API", version="0.3.0", openapi_tags=tags_metadata)
database.init_db()


class TodoCreate(BaseModel):
    task: str = Field(min_length=1, max_length=50)
    done: bool = False


class TodoUpdate(BaseModel):
    task: str | None = Field(default=None, min_length=1, max_length=50)
    done: bool | None = None


class TodoOut(BaseModel):
    id: int
    task: str
    done: bool


def get_todo_or_404(todo_id: int) -> dict:
    todo = database.get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="找不到这个待办")
    return todo


# 根路径
@app.get("/", tags=["meta"])
def read_root():
    return {"message": "Todo API 运行中"}


# 待办列表路径,学习查询参数和分页参数
@app.get("/todos", response_model=list[TodoOut], tags=["todos"])
def list_todos(
    done: bool | None = Query(default=None, description="按完成状态过滤"),
    limit: int = Query(default=10, ge=1, le=100),
):
    return database.list_todos(done=done, limit=limit)


# 创建待办路径
@app.post("/todos", response_model=TodoOut, status_code=201, tags=["todos"])
def create_todo(item: TodoCreate):
    return database.create_todo(task=item.task, done=item.done)


# 获取待办路径,学习路径参数
@app.get("/todos/{todo_id}", response_model=TodoOut, tags=["todos"])
def get_todo(todo_id: int = Path(..., ge=1)):
    return get_todo_or_404(todo_id)


# 更新待办路径
@app.put("/todos/{todo_id}", response_model=TodoOut, tags=["todos"])
def update_todo(todo_id: int, item: TodoUpdate):
    get_todo_or_404(todo_id)
    data = item.model_dump(exclude_unset=True)
    return database.update_todo(todo_id=todo_id, data=data)


# 删除待办路径
@app.delete("/todos/{todo_id}", status_code=204, tags=["todos"])
def delete_todo(todo_id: int):
    get_todo_or_404(todo_id)
    database.delete_todo(todo_id)

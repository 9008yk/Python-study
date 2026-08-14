"""FastAPI 待办 API：完整增删改查。"""

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Todo API", version="0.2.0")

todos = []
next_id = 1


class TodoCreate(BaseModel):
    task: str = Field(min_length=1, max_length=50)
    done: bool = False


class TodoUpdate(BaseModel):
    task: str | None = Field(default=None, min_length=1, max_length=50)
    done: bool | None = None


class Todo(TodoCreate):
    id: int


def find_todo(todo_id: int) -> Todo:
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="找不到这个待办")

# 根路径
@app.get("/")
def read_root():
    return {"message": "Todo API 运行中"}

# 待办列表路径,学习查询参数和分页参数
@app.get("/todos")
def list_todos(
    done: bool | None = Query(default=None, description="按完成状态过滤"),
    limit: int = Query(default=10, ge=1, le=100),
):
    result = todos
    if done is not None:
        result = [todo for todo in todos if todo.done == done]
    return result[:limit]

# 创建待办路径
@app.post("/todos")
def create_todo(item: TodoCreate):
    global next_id
    todo = Todo(id=next_id, **item.model_dump())
    todos.append(todo)
    next_id += 1
    return todo

# 获取待办路径,学习路径参数
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int = Path(..., ge=1)):
    return find_todo(todo_id)

# 更新待办路径
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, item: TodoUpdate):
    todo = find_todo(todo_id)
    data = item.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(todo, key, value)
    return todo

# 删除待办路径
@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    todo = find_todo(todo_id)
    todos.remove(todo)

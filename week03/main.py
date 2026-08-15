"""FastAPI 待办 API：SQLite 持久化版本。"""

import os
import sys

from fastapi import Depends, FastAPI, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field

sys.path.insert(0, os.path.dirname(__file__))

import database
import security

tags_metadata = [
    {"name": "todos", "description": "待办管理接口"},
    {"name": "meta", "description": "服务信息"},
    {"name": "auth", "description": "用户注册和登录"},
]

app = FastAPI(title="Todo API", version="0.4.0", openapi_tags=tags_metadata)
database.init_db()
bearer_scheme = HTTPBearer()

cors_origins = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "*").split(",")
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=6, max_length=64)


class UserOut(BaseModel):
    id: int
    username: str


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


def get_todo_or_404(todo_id: int, user_id: int) -> dict:
    todo = database.get_todo(todo_id, user_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="找不到这个待办")
    return todo

# 解析 token、查数据库、判断是否有效、返回用户信息
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict:
    try:
        payload = security.decode_token(credentials.credentials)
    except security.TokenError:
        raise HTTPException(status_code=401, detail="无效的登录凭证")
    user = database.get_user_by_username(payload.get("sub"))
    if user is None:
        raise HTTPException(status_code=401, detail="用户不存在")
    return user


# 根路径
@app.get("/", tags=["meta"])
def read_root():
    return {"message": "Todo API 运行中"}


# 注册路径
@app.post("/auth/register", response_model=UserOut, status_code=201, tags=["auth"])
def register(user: UserCreate):
    password_hash = security.hash_password(user.password)
    user_id = database.create_user(user.username, password_hash)
    if user_id is None:
        raise HTTPException(status_code=400, detail="用户名已被使用")
    return {"id": user_id, "username": user.username}


# 登录路径
@app.post("/auth/login", response_model=TokenOut, tags=["auth"])
def login(user: UserCreate):
    stored = database.get_user_by_username(user.username)
    if stored is None or not security.verify_password(
        user.password, stored["password_hash"]
    ):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    token = security.create_access_token(user.username)
    return {"access_token": token, "token_type": "bearer"}


# 获取当前登录用户路径
@app.get("/auth/me", response_model=UserOut, tags=["auth"])
def me(current_user: dict = Depends(get_current_user)):
    return {"id": current_user["id"], "username": current_user["username"]}


# 待办列表路径,学习查询参数和分页参数
@app.get("/todos", response_model=list[TodoOut], tags=["todos"])
def list_todos(
    current_user: dict = Depends(get_current_user),
    done: bool | None = Query(default=None, description="按完成状态过滤"),
    limit: int = Query(default=10, ge=1, le=100),
):
    return database.list_todos(done=done, limit=limit, user_id=current_user["id"])


# 创建待办路径
@app.post("/todos", response_model=TodoOut, status_code=201, tags=["todos"])
def create_todo(item: TodoCreate, current_user: dict = Depends(get_current_user)):
    return database.create_todo(
        task=item.task,
        done=item.done,
        user_id=current_user["id"],
    )


# 获取待办路径,学习路径参数
@app.get("/todos/{todo_id}", response_model=TodoOut, tags=["todos"])
def get_todo(
    todo_id: int = Path(..., ge=1),
    current_user: dict = Depends(get_current_user),
):
    return get_todo_or_404(todo_id, current_user["id"])


# 更新待办路径
@app.put("/todos/{todo_id}", response_model=TodoOut, tags=["todos"])
def update_todo(
    todo_id: int,
    item: TodoUpdate,
    current_user: dict = Depends(get_current_user),
):
    get_todo_or_404(todo_id, current_user["id"])
    data = item.model_dump(exclude_unset=True)
    return database.update_todo(
        todo_id=todo_id,
        data=data,
        user_id=current_user["id"],
    )


# 删除待办路径
@app.delete("/todos/{todo_id}", status_code=204, tags=["todos"])
def delete_todo(
    todo_id: int,
    current_user: dict = Depends(get_current_user),
):
    get_todo_or_404(todo_id, current_user["id"])
    database.delete_todo(todo_id, current_user["id"])

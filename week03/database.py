"""SQLite 数据库操作封装。"""

import sqlite3

DB_FILE = "todos.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)


def init_db():
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
        """
    )
    conn.commit()


def row_to_todo(row):
    return {"id": row[0], "task": row[1], "done": bool(row[2])}


def create_todo(task, done=False):
    cur = conn.execute(
        "INSERT INTO todos (task, done) VALUES (?, ?)",
        (task, int(done)),
    )
    conn.commit()
    return get_todo(cur.lastrowid)


def list_todos(done=None, limit=10):
    sql = "SELECT id, task, done FROM todos"
    params = []
    if done is not None:
        sql += " WHERE done = ?"
        params.append(int(done))
    sql += " ORDER BY id LIMIT ?"
    params.append(limit)
    rows = conn.execute(sql, params).fetchall()
    return [row_to_todo(row) for row in rows]


def get_todo(todo_id):
    row = conn.execute(
        "SELECT id, task, done FROM todos WHERE id = ?",
        (todo_id,),
    ).fetchone()
    if row is None:
        return None
    return row_to_todo(row)


def update_todo(todo_id, data):
    fields = []
    values = []
    if "task" in data:
        fields.append("task = ?")
        values.append(data["task"])
    if "done" in data:
        fields.append("done = ?")
        values.append(int(data["done"]))
    if fields:
        values.append(todo_id)
        conn.execute(
            f"UPDATE todos SET {', '.join(fields)} WHERE id = ?",
            values,
        )
        conn.commit()
    return get_todo(todo_id)


def delete_todo(todo_id):
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()

# 注册用户,返回用户 ID
def create_user(username, password_hash):
    try:
        cur = conn.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash),
        )
        conn.commit()
        return cur.lastrowid
    except sqlite3.IntegrityError:
        return None

# 根据用户名查询用户,返回带有哈希密码的用户信息
def get_user_by_username(username):
    row = conn.execute(
        "SELECT id, username, password_hash FROM users WHERE username = ?",
        (username,),
    ).fetchone()
    if row is None:
        return None
    return {"id": row[0], "username": row[1], "password_hash": row[2]}

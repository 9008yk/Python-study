"""待办清单 V2 的 pytest 测试。"""

import os

from todo_v2 import Todo, TodoList


def test_todo_default_not_done():
    todo = Todo("学习 Python")
    assert todo.done is False


def test_mark_done():
    todo = Todo("写作业")
    todo.mark_done()
    assert todo.done is True


def test_todo_line_round_trip():
    todo = Todo("学习 Python", done=True)
    restored = Todo.from_line(todo.to_line())
    assert restored.task == "学习 Python"
    assert restored.done is True


def test_todo_list_add_and_save(tmp_path):
    filename = tmp_path / "todo.txt"
    todo_list = TodoList(filename=str(filename))
    todo_list.add("学习 Python")
    assert len(todo_list.todos) == 1
    assert os.path.exists(filename)


def test_todo_list_complete_and_remove(tmp_path):
    filename = tmp_path / "todo.txt"
    todo_list = TodoList(filename=str(filename))
    todo_list.add("学习 Python")
    todo_list.add("写作业")
    todo_list.complete(0)
    assert todo_list.todos[0].done is True
    removed = todo_list.remove(1)
    assert removed.task == "写作业"
    assert len(todo_list.todos) == 1

"""待办清单 V2：用类、异常处理和模块化重写第一周的 CLI 工具。"""

TODO_FILE = "todo.txt"


class Todo:
    def __init__(self, task, done=False):
        self.task = task
        self.done = done

    def mark_done(self):
        self.done = True

    def to_line(self):
        done = "1" if self.done else "0"
        return f"{self.task}|{done}"

    @classmethod
    def from_line(cls, line):
        task, done = line.strip().split("|")
        return cls(task, done == "1")

    def show(self, index):
        mark = "[x]" if self.done else "[ ]"
        return f"{index}. {mark} {self.task}"


class TodoList:
    def __init__(self, filename=TODO_FILE):
        self.filename = filename
        self.todos = self._load()

    def _load(self):
        todos = []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        todos.append(Todo.from_line(line))
        except FileNotFoundError:
            pass
        return todos

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for todo in self.todos:
                f.write(todo.to_line() + "\n")

    def add(self, task):
        self.todos.append(Todo(task))
        self.save()

    def complete(self, index):
        self.todos[index].mark_done()
        self.save()

    def remove(self, index):
        removed = self.todos.pop(index)
        self.save()
        return removed

    def show(self):
        if not self.todos:
            return "暂无待办"
        return "\n".join(
            todo.show(index)
            for index, todo in enumerate(self.todos, start=1)
        )


def get_choice():
    while True:
        try:
            return int(input("请选择："))
        except ValueError:
            print("请输入数字")


def get_index(todos, prompt):
    while True:
        text = input(prompt)
        if not text.isdigit():
            print("请输入数字")
            continue
        index = int(text) - 1
        if 0 <= index < len(todos):
            return index
        print("序号不存在")


def main():
    todo_list = TodoList()
    while True:
        print()
        print("===== 待办清单 V2 =====")
        print(todo_list.show())
        print()
        print("1. 添加  2. 完成  3. 删除  0. 退出")
        choice = get_choice()
        if choice == 1:
            task = input("请输入待办内容：").strip()
            if task:
                todo_list.add(task)
                print("已添加")
            else:
                print("内容不能为空")
        elif choice == 2:
            if todo_list.todos:
                index = get_index(todo_list.todos, "输入要完成的序号：")
                todo_list.complete(index)
                print("已完成")
            else:
                print("暂无待办")
        elif choice == 3:
            if todo_list.todos:
                index = get_index(todo_list.todos, "输入要删除的序号：")
                removed = todo_list.remove(index)
                print(f"已删除：{removed.task}")
            else:
                print("暂无待办")
        elif choice == 0:
            todo_list.save()
            print("已保存，再见！")
            break
        else:
            print("请输入 0-3")


if __name__ == "__main__":
    main()

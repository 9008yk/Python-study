# Day 7：待办清单小项目
#
# 运行方式：
#   python week01/day07_todo.py
#
# 今天会把这一周学的东西串起来：
#   input / 条件判断 / while 循环 / 列表和字典 / 函数 / 文件读写
#
# 功能：
#   1. 添加待办
#   2. 查看待办
#   3. 标记完成
#   4. 删除待办
#   0. 退出并保存

import os

TODO_FILE = "todo.txt"


def load_tasks():
    """从文件读取待办，每行格式：任务|完成状态"""
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    task, done = line.split("|")
                    tasks.append({"task": task, "done": done == "1"})
    return tasks


def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        for item in tasks:
            done = "1" if item["done"] else "0"
            f.write(f"{item['task']}|{done}\n")


def show_tasks(tasks):
    if not tasks:
        print("暂无待办")
        return
    for index, item in enumerate(tasks, start=1):
        mark = "[x]" if item["done"] else "[ ]"
        print(f"{index}. {mark} {item['task']}")


def add_task(tasks):
    task = input("请输入待办内容：").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("已添加")
    else:
        print("内容不能为空")


def complete_task(tasks):
    show_tasks(tasks)
    choice = input("输入要完成的序号：")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("已完成")
        else:
            print("序号不存在")
    else:
        print("请输入数字")


def delete_task(tasks):
    show_tasks(tasks)
    choice = input("输入要删除的序号：")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"已删除：{removed['task']}")
        else:
            print("序号不存在")
    else:
        print("请输入数字")


def main():
    tasks = load_tasks()
    while True:
        print()
        print("===== 待办清单 =====")
        print("1. 添加  2. 查看  3. 完成  4. 删除  0. 退出")
        choice = input("请选择：")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            save_tasks(tasks)
            print("已保存，再见！")
            break
        else:
            print("请输入 0-4")


if __name__ == "__main__":
    main()

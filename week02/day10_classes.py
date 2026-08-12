# Day 10：类和对象
#
# 运行方式：
#   python week02/day10_classes.py
#
# 今天要理解：
#   1. 类 class：图纸 / 模板
#   2. 对象 object：按图纸造出来的实例
#   3. __init__ 构造方法：创建对象时自动执行
#   4. self：代表“对象自己”
#   5. 方法：类里面定义的函数

print("===== 最简单的类 =====")
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name}：汪汪！"

dog1 = Dog("旺财")
dog2 = Dog("来福")
print(dog1.bark())
print(dog2.bark())

print()
print("===== 带更多属性的类 =====")
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def level(self):
        if self.score >= 90:
            return "优秀"
        elif self.score >= 80:
            return "良好"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"

    def show(self):
        return f"{self.name}：{self.score} 分，{self.level()}"

s1 = Student("小明", 95)
s2 = Student("小红", 58)
print(s1.show())
print(s2.show())

print()
print("===== 练习 1：方法修改属性 =====")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{self.owner} 存入 {amount}，余额 {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "余额不足"
        self.balance -= amount
        return f"{self.owner} 取出 {amount}，余额 {self.balance}"

account = BankAccount("小明", 100)
print(account.deposit(50))
print(account.withdraw(200))
print(account.withdraw(30))

print()
print("===== 练习 2：列表存对象 =====")
students = [
    Student("小明", 95),
    Student("小红", 58),
    Student("小刚", 82),
]
for student in students:
    print(student.show())

print()
print("===== 挑战：给待办类加默认值和方法 =====")
class Todo:
    def __init__(self, task, done=False):
        self.task = task
        self.done = done

    def mark_done(self):
        self.done = True

    def show(self):
        mark = "[x]" if self.done else "[ ]"
        return f"{mark} {self.task}"

todo1 = Todo("学习 Python")
todo2 = Todo("写作业", done=True)
print(todo1.show())
print(todo2.show())
todo1.mark_done()
print(todo1.show())

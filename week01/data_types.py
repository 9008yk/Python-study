# Python 数据类型参考
#
# 运行方式：
#   python week01/data_types.py
#
# 用 type() 可以查看一个数据的类型

print("===== 基本类型 =====")

name = "小明"          # str 字符串
age = 25              # int 整数
height = 1.75         # float 浮点数
is_student = True     # bool 布尔值
nothing = None        # NoneType 空值

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(nothing, type(nothing))

print()
print("===== 容器类型 =====")

hobbies = ["篮球", "编程", "音乐"]     # list 列表：有序，可修改
favorite = ("Python", 3.13)           # tuple 元组：有序，不可修改
skills = {"Python": 80, "Git": 50}    # dict 字典：键值对
languages = {"Python", "Java", "C"}   # set 集合：不重复，无序

print(hobbies, type(hobbies))
print(favorite, type(favorite))
print(skills, type(skills))
print(languages, type(languages))

print()
print("===== 类型转换 =====")

score_text = "90"
score = int(score_text)
print(score + 5)

pi_text = "3.14"
pi = float(pi_text)
print(pi * 2)

number = 42
print(str(number) + " 是答案")

print(bool(0), bool(1), bool(""), bool("Python"))

print()
print("===== 可变与不可变 =====")

# list 可变：可以增删改
hobbies.append("摄影")
hobbies[0] = "跑步"
print(hobbies)

# tuple 不可变：不能修改
# favorite[0] = "Go"  # 运行这行会报错

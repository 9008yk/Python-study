# Day 9：列表推导式和 lambda
#
# 运行方式：
#   python week02/day09.py
#
# 今天要理解：
#   1. 列表推导式：用一行代码生成新列表
#   2. lambda：没有名字的匿名小函数
#   3. sorted 搭配 lambda 自定义排序
#   4. map / filter 快速处理列表

print("===== 普通写法 vs 列表推导式 =====")
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("普通写法：", squares)

squares2 = [i ** 2 for i in range(1, 6)]
print("列表推导式：", squares2)

print()
print("===== 带条件的列表推导式 =====")
evens = [i for i in range(1, 11) if i % 2 == 0]
print("1 到 10 的偶数：", evens)

print()
print("===== lambda 匿名函数 =====")
add = lambda a, b: a + b
print(add(3, 5))

print()
print("===== 练习 1：把字符串列表转成大写 =====")
words = ["python", "git", "github"]
upper_words = [word.upper() for word in words]
print(upper_words)

print()
print("===== 练习 2：过滤出长度大于 3 的单词 =====")
words = ["cat", "dog", "python", "code", "go"]
long_words = [word for word in words if len(word) > 3]
print(long_words)

print()
print("===== 练习 3：sorted 自定义排序 =====")
students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 85},
    {"name": "小刚", "score": 95},
]
by_score = sorted(students, key=lambda s: s["score"], reverse=True)
for student in by_score:
    print(student["name"], student["score"])

print()
print("===== 练习 4：map 和 filter =====")
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

print()
print("===== 挑战：1 到 20 中能被 3 整除的数的平方 =====")
result = [i ** 2 for i in range(1, 21) if i % 3 == 0]
print(result)

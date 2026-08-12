# 字典 dict 参考
#
# 运行方式：
#   python week01/dict_reference.py

print("===== 创建字典 =====")
empty = {}
student = {"name": "小明", "age": 25, "city": "上海"}
print(empty, student)

print()
print("===== 取值 =====")
print(student["name"])
print(student.get("score", 0))   # 键不存在时返回默认值，不会报错

print()
print("===== 添加和修改 =====")
student["score"] = 90    # 键不存在就是新增
student["age"] = 26      # 键存在就是修改
print(student)

print()
print("===== 删除 =====")
student.pop("city")
print(student)

print()
print("===== 遍历 =====")
for key in student:
    print(key, "=", student[key])

for key, value in student.items():
    print(key, ":", value)

print(student.keys())
print(student.values())

print()
print("===== 判断键是否存在 =====")
print("name" in student)
print("city" in student)

print()
print("===== 常用场景：统计单词次数 =====")
text = "hello world hello python hello"
words = text.split()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
print(counts)

print()
print("===== 字典和列表组合 =====")
students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 85},
]
for student in students:
    print(student["name"], student["score"])

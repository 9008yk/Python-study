# Day 5：列表 list 和字典 dict
#
# 运行方式：
#   python week01/day05.py
#
# 今天要理解：
#   1. 列表：有序、可修改，用 []，下标从 0 开始
#   2. 字典：键值对，用 {}，通过键取值
#   3. 常用操作：append、remove、len、keys、values、items

print("===== 列表 list =====")
hobbies = ["篮球", "编程", "音乐"]
print("第一个元素：", hobbies[0])
print("最后一个元素：", hobbies[-1])
print("长度：", len(hobbies))

hobbies.append("摄影")
print("追加后：", hobbies)

hobbies.remove("篮球")
print("删除后：", hobbies)

for hobby in hobbies:
    print("我喜欢", hobby)

print()
print("===== 切片 =====")
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])    # 从下标 1 到 3
print(numbers[:3])     # 前三个
print(numbers[::2])    # 隔一个取一个
print(numbers[0:4:3])

print()
print("===== 字典 dict =====")
student = {"name": "小明", "age": 25, "city": "上海"}
print("名字：", student["name"])
print("所有键：", student.keys())
print("所有值：", student.values())

student["score"] = 90
print("添加键后：", student)

student["age"] = 26
print("修改后：", student)

for key in student:
    print(key, "=", student[key])

for key, value in student.items():
    print(f"{key}: {value}")
    
print()
print("===== 练习 1：统计成绩 =====")
scores = {"语文": 90, "数学": 85, "英语": 88}
total = 0
for score in scores.values():
    total += score
print("三科总分：", total)
print("平均分：", total / len(scores))

print()
print("===== 练习 2：找出最高分 =====")
best_subject = ""
best_score = 0
for subject, score in scores.items():
    if score > best_score:
        best_score = score
        best_subject = subject
print("最高分科目：", best_subject, best_score)

print()
print("===== 挑战：列表套字典 =====")
students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 85},
    {"name": "小刚", "score": 95},
]
for student in students:
    print(f"{student['name']} 的分数是 {student['score']}")

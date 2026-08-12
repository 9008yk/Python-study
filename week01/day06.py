# Day 6：函数
#
# 运行方式：
#   python week01/day06.py
#
# 今天要理解：
#   1. def 定义函数
#   2. 参数：函数接收的输入
#   3. return：函数返回的输出
#   4. 默认参数
#   5. 调用函数

print("===== 示例：定义并调用 =====")
def greet(name):
    return "你好，" + name

print(greet("小明"))

print()
print("===== 练习 1：加法函数 =====")
def add(a, b):
    return a + b

print(add(3, 5))

print()
print("===== 练习 2：判断成绩等级 =====")
def score_level(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

print(score_level(95))
print(score_level(45))

print()
print("===== 练习 3：默认参数 =====")
def introduce(name, city="上海"):
    return f"我是{name}，来自{city}"

print(introduce("小明"))
print(introduce("小红", "北京"))

print()
print("===== 练习 4：返回多个值 =====")
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 1, 4, 1, 5]
small, big = get_min_max(nums)
print("最小值", small, "最大值", big)

print()
print("===== 挑战：1 加到 n =====")
def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_to(100))

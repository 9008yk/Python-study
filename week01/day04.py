# Day 4：循环 for 和 while
#
# 运行方式：
#   python week01/day04.py
#
# 今天要理解：
#   1. for 循环：遍历一个序列，比如 range(1, 11)
#   2. while 循环：条件成立就一直执行
#   3. break：提前结束整个循环
#   4. continue：跳过这一次，继续下一次
#   5. range(start, stop)：从 start 到 stop-1

print("===== for 循环示例 =====")
for i in range(1, 6):
    print(i)

print()
print("===== 练习 1：1 加到 100 =====")
total = 0
for i in range(1, 101):
    total += i
print("1 到 100 的和：", total)

print()
print("===== while 循环示例 =====")
n = 1
while n <= 5:
    print(n)
    n += 1

print()
print("===== 练习 2：while 计算 1 加到 100 =====")
total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print("while 计算的和：", total)

print()
print("===== 练习 3：遍历字符串和列表 =====")
name = "Python"
for ch in name:
    print(ch)

hobbies = ["篮球", "编程", "音乐"]
for hobby in hobbies:
    print("我喜欢", hobby)

print()
print("===== 练习 4：break 提前结束 =====")
for i in range(1, 101):
    print(i)
    if i == 5:
        break

print()
print("===== 练习 5：continue 跳过偶数 =====")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print()
print("===== 挑战：找出 1 到 100 中能被 7 整除的数 =====")
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=" ")
print()

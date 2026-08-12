# 列表 list 参考
#
# 运行方式：
#   python week01/list_reference.py

print("===== 创建列表 =====")
empty = []
fruits = ["苹果", "香蕉", "橙子"]
mixed = [1, "Python", True, 3.14]
print(empty, fruits, mixed)

print()
print("===== 按下标访问 =====")
print(fruits[0])
print(fruits[-1])
fruits[1] = "西瓜"
print(fruits)

print()
print("===== 常用操作 =====")
fruits.append("葡萄")
fruits.insert(1, "草莓")
print(fruits)
print(len(fruits))
print("苹果" in fruits)

fruits.remove("西瓜")
popped = fruits.pop()
print(fruits, "弹出的元素：", popped)

numbers = [3, 1, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

print()
print("===== 切片 =====")
nums = [10, 20, 30, 40, 50]
print(nums[1:4])
print(nums[::2])
print(nums[::-1])

print()
print("===== 遍历 =====")
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

print()
print("===== 嵌套列表 =====")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
print(matrix[0][1])

print()
print("===== 复制 =====")
a = [1, 2, 3]
b = a          # 这不是复制，b 和 a 指向同一个列表
b.append(4)
print("直接赋值：", a)

c = a.copy()   # 这才是复制
c.append(5)
print("copy 后：", a, c)

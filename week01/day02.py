# Day 2：变量和数字
#
# 运行方式：
#   python week01/day02.py
#
# 今天要理解四件事：
#   1. 变量就是给数据起名字，用 = 赋值
#   2. 整数 int：1, 100；浮点数 float：1.5, 3.14
#   3. 常见运算：+ - * / // % **
#   4. f-string 里可以直接放变量和计算结果

# 变量示例
name = "小明"
age = 25
height = 1.75
print(f"{name}今年{age}岁，身高{height}米")

# 数字运算示例
a = 10
b = 3
print("10 + 3 =", a + b)
print("10 / 3 =", a / b)
print("10 // 3 =", a // b)
print("10 % 3 =", a % b)
print("10 ** 3 =", a ** b)

# 练习 1：定义你的三个信息，用 f-string 输出
my_name = "你的名字"
my_age = 18
my_height = 1.70
print(f"我是{my_name}，今年{my_age}岁，身高{my_height}米")

# 练习 2：计算购物总价
price = 25.5
quantity1 = 3
total = price * quantity1
print(f"单价{price}元，买了{quantity1}个，共{total}元")

# 练习 3：摄氏温度转华氏温度，公式 F = C * 9 / 5 + 32
celsius = 26
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}摄氏度 = {fahrenheit}华氏度")

# 挑战：计算 BMI，保留两位小数
weight = 65
height_m = 1.75
bmi = weight / (height_m ** 2)
print(f"BMI 是 {bmi:.2f}")
print(f"BMI 是 {bmi:.0f}")
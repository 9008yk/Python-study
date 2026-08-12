# Day 11：模块、pip 和虚拟环境
#
# 运行方式：
#   python week02/day11_modules.py
#
# 今天要理解：
#   1. 模块：一个 .py 文件就是一个模块
#   2. import 导入模块
#   3. 标准库：Python 自带的模块
#   4. pip：安装第三方库
#   5. 虚拟环境：每个项目独立的依赖空间

print("===== 导入自己写的模块 =====")
import my_math

print(my_math.add(3, 5))
print(my_math.multiply(4, 6))
print(my_math.is_even(10))

print()
print("===== 按需导入 =====")
from my_math import add

print(add(1, 2))

print()
print("===== 标准库模块 =====")
import math
import random

print("16 的平方根：", math.sqrt(16))
print("圆周率：", math.pi)
print("1 到 10 的随机数：", random.randint(1, 10))
print("随机选一个：", random.choice(["石头", "剪刀", "布"]))

print()
print("===== 给模块起别名 =====")
import datetime as dt

today = dt.date.today()
print("今天的日期：", today)

print()
print("===== __name__ 的作用 =====")
if __name__ == "__main__":
    print("直接运行本文件时，这里会执行")

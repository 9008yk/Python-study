# Day 8：异常处理 try / except
#
# 运行方式：
#   python week02/day08_exceptions.py
#
# 今天要理解：
#   1. try：尝试执行可能出错的代码
#   2. except：捕获并处理错误
#   3. else：没有出错时才执行
#   4. finally：无论是否出错都会执行

print("===== 什么是异常 =====")
# 直接运行下面这行程序会崩溃：
# number = int("abc")

print()
print("===== 捕获异常 =====")
try:
    number = int("abc")
except ValueError:
    print("输入的不是数字")

print("程序继续运行")

print()
print("===== 多个 except =====")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以 0")
except Exception as e:
    print("其他错误：", e)

print()
print("===== else 和 finally =====")
try:
    number = int("123")
except ValueError:
    print("不是数字")
else:
    print("转换成功：", number)
finally:
    print("无论如何都会执行")

print()
print("===== 练习 1：安全除法 =====")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "除数不能为 0"

print(safe_divide(10, 2))
print(safe_divide(10, 0))

print()
print("===== 练习 2：安全的数字输入 =====")
def get_number(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print("请输入数字")

age = get_number("请输入年龄：")
print("年龄是", age)

print()
print("===== 挑战：读取不存在的文件 =====")
try:
    with open("not_exist.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在")

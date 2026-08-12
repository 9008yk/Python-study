# Day 3：条件判断 if / elif / else
#
# 运行方式：
#   python week01/day03.py
#
# 今天要理解：
#   1. if 条件成立时执行里面的代码
#   2. elif 检查上一个条件不成立时的下一个条件
#   3. else 所有条件都不成立时执行
#   4. 比较运算符：== != > < >= <=

score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 练习 1：判断年龄是否成年
age = 17
if age >= 18:
    print("已成年")
else:
    print("未成年")

# 练习 2：判断奇偶，% 是取余
number = 7
if number % 2 == 0:
    print("偶数")
else:
    print("奇数")

# 练习 3：温度提醒
temperature = 35
if temperature >= 35:
    print("注意防暑")
elif temperature >= 15:
    print("天气舒适")
else:
    print("注意保暖")

# 挑战：让用户输入分数再判断等级
# input() 得到的是字符串，要先用 int() 转成整数
user_score = input("请输入你的分数：")
user_score = int(user_score)
if user_score >= 90:
    print("优秀")
elif user_score >= 80:
    print("良好")
elif user_score >= 60:
    print("及格")
else:
    print("不及格")

"""我的数学工具模块。"""


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def is_even(n):
    return n % 2 == 0


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

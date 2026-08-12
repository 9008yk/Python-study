"""第一周练习题，每天完成一个函数。"""


def greet(name: str) -> str:
    """Day 1-2: 返回一句问候语，例如 greet("小明") -> "你好，小明！"。"""
    # 在这里写你的代码
    return ""


def score_level(score: float) -> str:
    """Day 3: 90 分以上返回 A，80~89 返回 B，60~79 返回 C，60 以下返回 D。"""
    # 在这里写你的代码
    return ""


def sum_to(n: int) -> int:
    """Day 4: 返回 1 加到 n 的结果。"""
    # 在这里写你的代码
    return 0


def count_words(text: str) -> int:
    """Day 5: 用字典统计一个英文句子中每个单词出现的次数，返回出现最多的次数。"""
    # 在这里写你的代码
    return 0


def make_todo(task: str) -> dict:
    """Day 6: 把一条待办事项转换成字典 {"task": task, "done": False}。"""
    # 在这里写你的代码
    return {}


if __name__ == "__main__":
    print(greet("小明"))
    print(score_level(85))
    print(sum_to(100))
    print(count_words("hello world hello python"))
    print(make_todo("学习 Python"))

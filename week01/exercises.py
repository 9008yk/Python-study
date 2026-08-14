"""第一周练习题，每天完成一个函数。"""


def greet(name: str) -> str:
    """Day 1-2: 返回一句问候语，例如 greet("小明") -> "你好，小明！"。"""
    # 在这里写你的代码
    return f"你好，{name}!"


def score_level(score: float) -> str:
    """Day 3: 90 分以上返回 A，80~89 返回 B，60~79 返回 C，60 以下返回 D。"""
    # 在这里写你的代码
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


def sum_to(n: int) -> int:
    """Day 4: 返回 1 加到 n 的结果。"""
    # 在这里写你的代码
    total=0
    for i in range(1,n+1):
        total+=i
    return total


def count_words(text: str) -> int:
    """Day 5: 用字典统计一个英文句子中每个单词出现的次数，返回出现最多的次数。"""
    # 在这里写你的代码
    word_count={}
    words=text.split()
    for word in words:
        if word in word_count:
           word_count[word]+=1
        else:
           word_count[word]=1
    return max(word_count.values())

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

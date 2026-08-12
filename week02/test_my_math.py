"""pytest 单元测试示例。"""

from my_math import add, average, is_even, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False


def test_average():
    assert average([1, 2, 3]) == 2.0
    assert average([]) == 0

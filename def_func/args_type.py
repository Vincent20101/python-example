# coding:utf-8


from typing import List


def add_numbers(a: int, b: int) -> int:
    return a + b


def concatenate_strings(strings: List[str]) -> str:
    return ''.join(strings)


# 使用这两个函数
result1 = add_numbers(3, 4)  # 输出 7
print("Result1:", result1)

result1 = add_numbers("hello", "4")
print("Result1:", result1)

result2 = concatenate_strings(['Hello', ' ', 'world!'])  # 输出 'Hello world!'
print("Result2:", result2)

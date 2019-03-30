# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: Count Consecutive Summers.py
# @Time: 2019/2/11 23:14
# @Software: PyCharm


def count_consecutive_summers(num):
    p = 0
    for i in range(1, num // 2 + 1):
        s = 0
        for j in range(i, num):
            s += j
            if s == num:
                p += 1
            elif s > num:
                break
    return p + 1


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(99))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")

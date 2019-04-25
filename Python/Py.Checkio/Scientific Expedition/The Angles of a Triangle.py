# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: The Angles of a Triangle.py
# @time: 2019/04/24 14:26:40
# @contact: lodgeinwh@gmail.com
# @version: 1.0

from typing import List


def checkio(a: int, b: int, c: int) -> List[int]:
    from math import acos, degrees
    cosA = (a * a - b * b - c * c) / (-2 * b * c)
    cosB = (b * b - a * a - c * c) / (-2 * a * c)
    cosC = (c * c - a * a - b * b) / (-2 * a * b)
    cos_list = [cosA, cosB, cosC]
    if not all(-1 <= i <= 1 for i in cos_list):
        return [0, 0, 0]
    result = []
    for i in cos_list:
        result.append(round(degrees(acos(i))))
    return sorted(result)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")

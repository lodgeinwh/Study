# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: The Square Chest.py
# @time: 2019/04/24 16:49:26
# @contact: lodgeinwh@gmail.com
# @version: 1.0

from typing import List


def checkio(lines):
    points = ([1, 2, 3, 5, 6, 7, 9, 10, 11], [1, 2, 5, 6], [1])
    lines = [set(line) for line in lines]

    def has_square(start, n):
        for off in 1, 4, -1, -4:
            for step in range(n):
                if {start, start + off} not in lines:
                    return False
                start += off
        return True

    return sum(has_square(p, n+1) for n in range(3) for p in points[n])


if __name__ == '__main__':
    print("Example:")
    print(
        checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6,
                                                                  7], [7, 8],
                 [6, 10], [7, 11], [8, 12], [10, 11], [10, 14], [12, 16],
                 [14, 15], [15, 16]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11], [10, 14],
                     [12, 16], [14, 15],
                     [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8], [6, 7], [5, 9],
                     [6, 10], [7, 11], [8, 12], [9, 13], [10, 11], [12, 16],
                     [13, 14], [14, 15],
                     [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6],
                     [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10],
                     [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10], [10, 14],
                     [14, 13], [13, 9]]) == 0), "Fifth, snake"
    print("Coding complete? Click 'Check' to earn cool rewards!")

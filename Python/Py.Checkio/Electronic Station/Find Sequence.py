# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Find Sequence.py
# @time: 2019/01/31 14:45:48
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def ishorizontal(m):
    row = len(m)
    for i in range(row):
        for j in range(row - 3):
            if m[i][j] == m[i][j + 1] == m[i][j + 2] == m[i][j + 3]:
                return True
    return False


def isvertical(m):
    row = len(m)
    for i in range(row - 3):
        for j in range(row):
            if m[i][j] == m[i + 1][j] == m[i + 2][j] == m[i + 3][j]:
                return True
    return False


def isdiagonal(m):
    row = len(m)
    for i in range(row - 3):
        for j in range(row - 3):
            if m[i][j] == m[i + 1][j + 1] == m[i + 2][j + 2] == m[i + 3][j +
                                                                         3]:
                return True
    return False


def isrediagonal(m):
    row = len(m)
    for i in range(row - 3):
        for j in range(3, row):
            if m[i][j] == m[i + 1][j - 1] == m[i + 2][j - 2] == m[i + 3][j -
                                                                         3]:
                return True
    return False


def checkio(matrix):
    if isdiagonal(matrix) or ishorizontal(matrix) or isrediagonal(
            matrix) or isvertical(matrix):
        return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6],
                    [1, 7, 2, 5]]) == True, "Vertical"
    assert checkio([[7, 1, 4, 1], [1, 2, 5, 2], [3, 4, 1, 3],
                    [1, 1, 8, 1]]) == False, "Nothing here"
    assert checkio([[2, 1, 1, 6, 1], [1, 3, 2, 1, 1], [4, 1, 1, 3, 1],
                    [5, 5, 5, 5, 5], [1, 1, 3, 1,
                                      1]]) == True, "Long Horizontal"
    assert checkio([[7, 1, 1, 8, 1, 1], [1, 1, 7, 3, 1, 5], [2, 3, 1, 2, 5, 1],
                    [1, 1, 1, 5, 1, 4], [4, 6, 5, 1, 3, 1],
                    [1, 1, 9, 1, 2, 1]]) == True, "Diagonal"

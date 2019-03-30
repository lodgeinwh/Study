# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Moore Neighbourhood.py
# @time: 2019/1/4 23:05


def count_neighbours(grid, row, col):
    row_start, row_end = row - 1, row + 2
    if row_start < 0:
        row_start = 0
    if row_end > len(grid):
        row_end = len(grid)

    col_start, col_end = col - 1, col + 2
    if col_start < 0:
        col_start = 0
    if col_end > len(grid[0]):
        col_end = len(grid[0])

    sum = 0
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            sum += grid[i][j]

    return sum - grid[row][col]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"

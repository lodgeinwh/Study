# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Creat Intervals.py
# @time: 2019/03/14 22:08:26
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def create_intervals(data):
    return list(zip(sorted(x for x in data if x - 1 not in data), sorted(x for x in data if x + 1 not in data)))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')

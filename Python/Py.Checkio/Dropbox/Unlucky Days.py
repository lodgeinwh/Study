# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Unlucky Days.py
# @time: 2019/1/5 18:41


from calendar import weekday


def checkio(year):
    s = 0
    for i in range(1, 13):
        w = weekday(year, i, day=13)
        if w == 4:
            s += 1
    return s


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"

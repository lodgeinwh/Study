# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Min and Max.py
# @time: 2018-11-18 16:21


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    args = args[0] if len(args) == 1 else args
    value = None
    for i in args:
        temp = i if not key else key(i)
        if value is None or value < temp:
            value = temp
            ans = i
    return ans


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    args = args[0] if len(args) == 1 else args
    value = None
    for i in args:
        temp = i if not key else key(i)
        if value is None or value > temp:
            value = temp
            ans = i
    return ans


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Long Repeat.py
# @time: 2018-11-18 16:24


def long_repeat(line):
    if line == "":
        return 0
    else:
        lst = []
        count = 1
        for i in range(1, len(line)):
            if line[i] == line[i - 1]:
                count += 1
            else:
                lst.append(count)
                count = 1
        lst.append(count)
        return max(lst)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')

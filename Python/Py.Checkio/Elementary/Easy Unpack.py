#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Easy Unpack.py
# @time: 2018/12/26 21:16


def easy_unpack(elements):
    lst = []
    lst.append(elements[0])
    lst.append(elements[2])
    lst.append(elements[-2])
    lst = tuple(lst)
    return lst


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')

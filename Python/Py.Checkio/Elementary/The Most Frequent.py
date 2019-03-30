# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: The Most Frequent.py
# @time: 2018/12/26 21:15


def most_frequent(data):
    dic = {}
    set1 = set(data)
    for i in set1:
        dic[i] = data.count(i)
    lst = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    return lst[0][0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')

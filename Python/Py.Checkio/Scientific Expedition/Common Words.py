# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Common Words.py
# @time: 2019/04/24 14:03:35
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def checkio(first, second):
    first = set(first.split(','))
    second = set(second.split(','))
    result = ','.join(sorted(first & second))
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three",
                   "four,five,one,two,six,three") == "one,three,two", "1 2 3"

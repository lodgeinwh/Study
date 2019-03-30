# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Long Non Repeat.py
# @time: 2018/12/29 22:35


def non_repeat(line):
    result = ''
    for i in range(len(line)):
        temp = ''
        j = 0
        while i + j < len(line) and line[i + j] not in temp:
            temp += line[i + j]
            j += 1
        if len(temp) > len(result):
            result = temp
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')

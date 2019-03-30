# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Three Words.py
# @time: 2018/12/26 21:06


def checkio(words):
    lst = words.split(' ')
    count = 0
    for i in lst:
        if i.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print(
        "Coding complete? Click 'Check' to review your tests and earn cool rewards!"
    )

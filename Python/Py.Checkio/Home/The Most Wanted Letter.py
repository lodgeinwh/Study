# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: The Most Wanted Letter.py
# @time: 2018-11-18 16:14


import string

'''
def checkio(text):
    return min([(-1 * text.lower().count(ch), ch) for ch in string.ascii_lowercase])[1]
'''


def checkio(text):
    return max(string.ascii_lowercase, key=text.lower().count)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

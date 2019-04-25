# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodgeinwh
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Monkey Typing.py
# @time: 2018-11-18 16:19


import string


def count_words(text, words):
    t = 0
    text = text.lower()
    for i in string.punctuation:
        text = text.replace(i, '')
    text = set(text.split(' '))
    for j in words:
        for k in text:
            if j in k:
                t += 1
    return t


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

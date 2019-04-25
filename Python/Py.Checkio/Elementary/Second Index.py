# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: lodge
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: lodgeinwh@gmail.com
# @file: Second Index.py
# @time: 2018/12/24 22:56


def second_index(text: str, symbol: str) -> [int, None]:
    text = text.replace(symbol, '', 1)
    return text.find(symbol) + 1 if text.find(symbol) != -1 else None


'''
def second_index(text: str, symbol: str):
    index1 = text.find(symbol)
    if index1 == -1:
        return None
    else:
        new_text = text[index1 + 1:]
        index2 = new_text.find(symbol)
        if index2 == -1:
            return None
        else:
            return index1 + index2 + 1


def second_index(text: str, symbol: str):
    i=text.find(symbol)
    j=text.find(symbol,i+1)
    if j>i:
        return j
    else:
        return None
'''

if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
